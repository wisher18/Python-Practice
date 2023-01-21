class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def details(self):
        return f"The name of employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set, Please set it using setters"
        return f"{self.fname}.{self.lname}@wisher.com"
    @email.setter
    def email(self, string):
        print("Setting now")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

bhushan = Employee("bhushan","pagare")
print(bhushan.details())
print(bhushan.email)
del bhushan.email
print(bhushan.email)
bhushan.fname = "mayur"
bhushan.email = "mayur.pagare@gmail.com"
print(bhushan.email)
