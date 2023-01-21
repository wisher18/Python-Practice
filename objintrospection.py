class Employee:
    def __init__(self,fname , lname):
        self.fname = fname
        self.lname = lname
    def details(self):
        return f"employee is {self.fname} {self.lname}"
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@wisher.com"
    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
import inspect
emp = Employee("bhushan", "pagare")
print(emp.details())
print(emp.email)
print(inspect.getmembers(emp))
print(inspect.__file__)
print(inspect.isclass(Employee))

