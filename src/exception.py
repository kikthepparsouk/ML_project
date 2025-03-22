import sys



def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    # file_name = exc_tb.tb_frame.f_code.co_filename
    # line_number = exc_tb.tb_lineno
    # function_name = exc_tb.tb_frame.f_code.co_name

    error_message = f"Error: {error} \n"
    error_message += f"Line number: {exc_tb.tb_lineno} \n"
    error_message += f"File name: {exc_tb.tb_frame.f_code.co_filename} \n"
    error_message += f"Function name: {exc_tb.tb_frame.f_code.co_name} \n"

    return error_message


def CustomError(Exception):
    def __init__(self,error_detail,error_message):
        self.error_message = error_message
        self.error_detail = error_detail
        self.error_message = error_message_detail(self.error_message,self.error_detail)
    
    def __str__(self):
        return self.error_message