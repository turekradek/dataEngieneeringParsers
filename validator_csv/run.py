from validation_csv import ValidationCSV
import os
import logging

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    file_name = 'test_file_csv.csv'
    test_files_path = '../test_files/'
    validation = ValidationCSV(file_name) 
    complete_path = validation.complete_path_return()
    
    try:
        if os.path.exists(complete_path):
            logging.info(f"Current working directory: {os.getcwd()}")
            logging.info(f"File {complete_path} exists")
            validation = ValidationCSV(complete_path)
            validation.validate()
            separator = validation.validate_separator()
            logging.info(f"Separator: {separator}")
        else:
            logging.warning(f"File {complete_path} does not exist")
    except ValueError as e:
        logging.error(e)

if __name__ == "__main__":
    main()
