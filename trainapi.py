
class Train:
    def __init__(self, n=None):
        self.apikey = "9dgk93tggn"
        if n is not None:
            self.setapi(n)
    
    def setapi(self,n):
        self.apikey = n
    
    def getapi(self):
        return self.apikey