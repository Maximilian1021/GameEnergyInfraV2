import paramiko

from config import config


def add_ip_to_docker_user_chain(server_ip, server_port, ssh_key_path, username, ip_to_add):
    table, ssh = get_table(server_ip, server_port, ssh_key_path, username)
    if ip_to_add in table:
        print(f"The IP address {ip_to_add} is already in the PREROUTING chain in the raw table on Server {server_ip}")
    else:
        # Hinzufügen der IP-Adresse zur PREROUTING-Kette der Raw-Tabelle
        add_command = f"sudo iptables -t raw -A PREROUTING -s {ip_to_add} -j DROP"
        stdin, stdout, stderr = ssh.exec_command(add_command)
        print(f"IP address {ip_to_add} has been added to the PREROUTING chain in the raw table on Server {server_ip}.")

    # SSH-Verbindung schließen
    ssh.close()
    print("Connection closed")
    print("------------")


def block(ip):
    for i in config.get("servers"):
        add_ip_to_docker_user_chain(i, "2811", "key.pem", "root", ip)


def remove_ip_from_docker_user_chain(server_ip, server_port, ssh_key_path, username, ip_to_remove):
    table, ssh = get_table(server_ip, server_port, ssh_key_path, username)
    if ip_to_remove not in table:
        print(f"The IP address {ip_to_remove} is not in the PREROUTING chain in the raw table on Server {server_ip}")
    else:
        # Entfernen der IP-Adresse aus der PREROUTING-Kette der Raw-Tabelle
        remove_command = f"sudo iptables -t raw -D PREROUTING -s {ip_to_remove} -j DROP"
        stdin, stdout, stderr = ssh.exec_command(remove_command)
        print(
            f"IP address {ip_to_remove} has been removed from the PREROUTING chain in the raw table on Server {server_ip}.")

    # SSH-Verbindung schließen
    ssh.close()
    print("Connection closed")
    print("------------")


def unblock(ip):
    for i in config.get("servers"):
        remove_ip_from_docker_user_chain(i, "2811", "key.pem", "root", ip)


def get_table(server_ip, server_port, ssh_key_path, username) -> (str, paramiko.SSHClient):
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

    # Prüfen, ob die IP-Adresse in der PREROUTING-Kette der Raw-Tabelle ist
    check_command = "sudo iptables -t raw -L PREROUTING -n"
    stdin, stdout, stderr = ssh.exec_command(check_command)
    return stdout.read().decode(), ssh
