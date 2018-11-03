# EXAMPLE PROGRAM ON HOLD DIFFERENT VALUES FOR DIFFERENT OBJECTS

class employee:
    def assign(self,id,na):
        self.idno=id
        self.name=na
    def display(self):
        print(self.idno)
        print(self.name)
e1 = employee()
e1.assign(10100,"DURGA")
e1.display()
print("==========")
print("==========")
e2 = employee()
e2.assign(8000,"PRASAD")
e2.display()