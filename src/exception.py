# Importing required modules
import sys                
import logging           
from src.logger import logging   

# Function to create a detailed error message
def error_message_detail(error, error_detail: sys):
    """
    Extracts the filename, line number, and error message
    from the system exception info (sys.exc_info).
    """

    # sys.exc_info() returns (exception_type, exception_value, traceback_object)
    _, _, exc_tb = error_detail.exc_info()

    # Extract filename from traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a readable error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, 
        exc_tb.tb_lineno,   # line number where error happened
        str(error)          # actual error message
    )
    return error_message


# Custom Exception Class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Extends the base Exception class.
        Accepts an error message and error details (sys).
        Calls error_message_detail() to format a detailed error message.
        """
        super().__init__(error_message)   # Call parent Exception class
        self.error_message = error_message_detail(
            error_message, 
            error_detail=error_detail
        )

    def __str__(self):
        """
        When str(CustomException) is called (e.g., print(e)),
        this returns the detailed error message instead of the default one.
        """
        return self.error_message
