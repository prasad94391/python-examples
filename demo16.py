   #example on static variable

class employee:
    comp_name="DURGA"
    comp_cno=9533463473
    def display(self):
        print("employee class")
        print(employee.comp_name)
        print(employee.comp_cno)

e1 = employee()
e1.display()
