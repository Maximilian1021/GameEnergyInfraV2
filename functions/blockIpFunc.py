import paramiko


def add_ip_to_docker_user_chain(server_ip, server_port, ssh_key_path, username, ip_to_add):
    # Erstellen eines SSH-Clients
    ssh = paramiko.SSHClient()
    # Automatisches Hinzufügen von Server-Schlüsseln
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Verbindung zum SSH-Server herstellen
    try:
        ssh.connect(server_ip, port=server_port, username=username, key_filename=ssh_key_path)
        print("------------")
        print(f"Connected on Server {server_ip}")
    except Exception as e:
        print(f"Error connecting to server: {e}")
        return

    # Prüfen, ob die IP-Adresse in der DOCKER-USER-Kette ist
    stdin, stdout, stderr = ssh.exec_command("sudo iptables -L DOCKER-USER -n")
    output = stdout.read().decode()
    if ip_to_add in output:
        print(f"The IP address {ip_to_add} is already in the DOCKER-USER chain on Server {server_ip}")
    else:
        # Hinzufügen der IP-Adresse zur DOCKER-USER-Kette
        add_command = f"sudo iptables -A DOCKER-USER -s {ip_to_add} -j DROP"
        stdin, stdout, stderr = ssh.exec_command(add_command)
        print(f"IP address {ip_to_add} has been added to the DOCKER-USER chain on Server {server_ip}.")

    # SSH-Verbindung schließen
    ssh.close()
    print("Connection closed")
    print("------------")
