class A:
    def meth(self):
        print("This is method from class A")
class B(A):
    def meth(self):
        print("This is method from class B")
class C(A):
    def meth(self):
        print("This is method from class C")
class D(B,C):
    def meth(self):
        print("This is method from class D")
a = A()
b = B()
c = C()
d = D()
d.meth()