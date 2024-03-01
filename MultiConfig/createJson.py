import json, os


class JsonFormat:
    def __init__(self, obj):
        self.object = obj

    def addObjectToJson(self, **objects):
        for key, value in objects.items():
            self.object[key] = value

    def getFileInfor(self):
        return json.dumps(self.__dict__)

class ItemFormat(JsonFormat):
    def __init__(self, obj, name):
        super(ItemFormat, self).__init__(obj)
        self.name = name



class JsonConfigFile:
    def __int__(self, file_name):
        self.file_name = file_name
        # self.config = {}

    def write(self, data):
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def read(self):
        with open(self.file_name, "r") as file:
            data = json.load(file)
        return data
