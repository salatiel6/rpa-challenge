import os
import openpyxl


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
            # Create a new workbook
            workbook = openpyxl.Workbook()

            # Select the active worksheet
            worksheet = workbook.active

            # Define the headers for the columns
            headers = list(data[0].keys())

            # Write the headers to the first row of the worksheet
            worksheet.append(headers)

            # Loop through each dictionary in the list
            for row_data in data:
                # Extract the values from the dictionary
                row = [row_data[key] for key in headers]

                # Write the values to a new row in the worksheet
                worksheet.append(row)

            # Get the directory path of this file
            module_dir = os.path.dirname(__file__)

            # Create a directory for output files if it doesn't exist
            filedir = os.path.join(module_dir, '.', 'outputs')
            if not os.path.exists(filedir):
                os.makedirs(filedir)

            # Save the workbook to a file
            file_path = os.path.join(filedir, filename)
            with open(file_path, "wb") as file:
                workbook.save(file)

        except Exception as e:
            print(f"An error occurred while saving to Excel: {e}")
