#!/usr/bin/python3
'''create storage to store reservations'''

import json

class FileStorage:
    # string - path to the JSON file
    __file_path = "file.json"
    # dictionary - empty but will store all objects by <class name>.id
    __objects = {}

    def read_res(self):
        """Read reservations from the JSON file."""
        if not os.path.exists(self.__file_path):
            return []
        with open(self.__file_path, 'r') as file:
            return json.load(file)

    def new(self, reservations):
        """Write reservations to the JSON file."""
        with open(self.__file_path, 'w') as file:
            json.dump(reservations, file, indent=4)

