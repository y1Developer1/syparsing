class ruleError(Exception):
    msg = "error"
    def __init__(self,message):
        if(type(message) is str):
            self.msg = message + ""

    def __str__(self):
        return self.msg