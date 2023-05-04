import calendar

from datetime import date
from .config import MONTH_AMOUNT


class Feats:
    @staticmethod
    def define_months():
        try:
            # Check if month_amount is a valid input (between 0 and 3)
            if not 0 <= MONTH_AMOUNT <= 3:
                raise ValueError("month_amount must be between 0 and 3")

            # Get today's date
            today = date.today()

            # Create a list of the names of the last self.month_amount months,
            # starting from the current month
            months = []
            for i in range(MONTH_AMOUNT):
                month_number = today.month - i
                month_name = calendar.month_name[month_number]
                months.append(month_name)

            # Convert all month names to uppercase
            months = [month.upper() for month in months]

            # Return the list of months
            return months

        except ValueError as ve:
            print(f"ValueError: {ve}")

        except Exception as e:
            print(f"An error occurred while defining the months: {e}")


feats = Feats()
