import sys


def error_massage_detail(error,error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message[{error}]"
    return error_message

class CustomException(Exception):
    def __init__(self,error_messsage,error_detail:sys):
        super().__init__(error_messsage)
        self.error_massage = error_massage_detail(error_messsage,error_detail)

    def __str__(self):
        return self.error_massage
        