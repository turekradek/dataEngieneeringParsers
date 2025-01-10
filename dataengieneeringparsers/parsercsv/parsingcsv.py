

class CsvParser:
    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        with open(self.file_path, 'r') as file:
            lines = file.readlines()
            return [line.strip().split(',') for line in lines]
