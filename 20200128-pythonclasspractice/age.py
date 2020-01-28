class Age:

    def __init__(self,age):
        self.age = age
    
    def getage(self):
        return self.age
    
    def setage(self,age):
        self.age = age
    
    age = property(getage,setage)
