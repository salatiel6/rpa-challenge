import os
from RPA.Excel.Files import Files


class FileHandler:
    @staticmethod
    def save_to_excel(data, filename):
        """
        Saves a list of dictionaries to an Excel file.

        Args:
            data (list[dict]): A list of dictionaries, where each dictionary
                represents a row of data in the Excel file.
            filename (str): The name of the Excel file to create.

        Raises:
            ValueError: If the data list is empty.
            Exception: If an error occurs while saving the Excel file.
        """
        if not data:
            raise ValueError("Data list cannot be empty.")

        try:
            # Get the directory path of this file
            module_dir = os.path.dirname(__file__)

            # Create a directory for output files if it doesn't exist
            filedir = os.path.join(module_dir, '', 'outputs')
            if not os.path.exists(filedir):
                os.makedirs(filedir)

            # Get the full path of the output file
            file_path = os.path.join(filedir, filename)

            # Create a new workbook
            lib = Files()
            lib.create_workbook(path=file_path, fmt="xlsx")

            # Create a new worksheet
            lib.create_worksheet(name="articles", content=data, header=True)

            lib.save_workbook()

        except Exception as e:
            print(f"An error occurred while saving to Excel: {e}")
