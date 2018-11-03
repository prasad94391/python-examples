class employee:
    def assign(self,id,na):
        self.idno=id
        self.name=na
    def display(self):
        print(self.idno)
        print(self.name)
e1 = employee()
e1.assign(100,"durga")
e1.display()

e2 = employee()
e2.assign(200,"prasad")
e2.display()

