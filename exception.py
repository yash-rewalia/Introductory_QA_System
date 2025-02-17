import sys

class customexception(Exception):
    def __init__(self, error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        print(exc_tb)

        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script: {} at line number: {} with error message: {}".format(self.filename,self.lineno,str(self.error_message))
    
if __name__ == '__main__':
    try:
        a = 1/0
    except Exception as e:
        raise customexception(e,sys)