import json


class Config:

    def __init__(self, path: str):
        self.path = path
        self.data = {}
        self.load()

    def load(self):
        with open(self.path, "r") as f:
            self.data = json.load(f)

    def save(self):
        with open(self.path, "w") as f:
            json.dump(self.data, f, indent=4)

    def get(self, key: str):
        # Make sure that you can access subkey by using a dot
        if "." in key:
            keys = key.split(".")
            data = self.data
            for key in keys:
                data = data[key]
            return data
        return self.data[key]

    def set(self, key: str, value):
        self.data[key] = value
        self.save()

    def delete(self, key: str):
        del self.data[key]
        self.save()

    def reload(self):
        self.load()

    def __del__(self):
        self.save()

    def __repr__(self):
        return f"<Config path={self.path}>"

    def __str__(self):
        return f"<Config path={self.path}>"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.set(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, item):
        return item in self.data


config = Config("config.json")
