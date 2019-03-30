class person:
    def __init__(self,id):
        self.id=id
        print("object created",id)
    def __del__(self):
        print("object destroyed")
    def setname(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def getname(self):
        print(self.fname+""+self.lname)
p1=person(5)
p1.setname("raju","raman")
p1.getname()
p1.__del__()        
