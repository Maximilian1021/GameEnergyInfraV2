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


config = Config("config.json")
