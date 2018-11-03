#example on instance variable

class employee:
    def assign(self):
        self.comp_name="ADITHYA"
        self.comp_cno=9533463473
    def display(self):
        print("employee class")
        print(self.comp_name)
        print(self.comp_cno)

e1 = employee()
e1.assign()
e1.display()
print("====================")
e2 = employee()
e2.assign()
e2.display()