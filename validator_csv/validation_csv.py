import os
import csv
import logging

print( os.getcwd())
class ValidationCSV:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.project_path = os.getcwd()
        self.test_files_path = 'test_files'
        self.complete_path = os.path.join(self.project_path,self.test_files_path, self.csv_file)
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    def complete_path_return(self):
        return self.complete_path
    
    def validate(self):
        logging.info("Starting validation")
        if not os.path.exists(self.complete_path):
            raise ValueError("File not found")

        if not self.csv_file.endswith(".csv"):
            raise ValueError("Invalid file format")

        return True
    
    def validate_separator(self): 
        logging.error("Invalid file format")
        with open(self.complete_path, 'r') as file:
            sample = file.read(1024) 
            sniffer = csv.Sniffer() 
            dialect = sniffer.sniff(sample) 
            return dialect.delimiter