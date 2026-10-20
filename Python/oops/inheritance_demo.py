# single and multilevel inheritance
class A:
    def f1(self):
        print("f1 works")

    def f2(self):
        print("f2 works")


class B(A):
    def f3(self):
        print("f3 works")

    def f4(self):
        print("f4 works")


class C(B):
    def f5(self):
        print("f5 works")


obj1 = C()
obj1.f1()
obj1.f3()
obj1.f5()


# multiple inheritance
class A1:
    def f1(self):
        print("A1: f1 works")

    def show(self):
        print("A1 show")


class B1:
    def f2(self):
        print("B1: f2 works")

    def show(self):
        print("B1 show")


class C1(A1, B1):
    def f3(self):
        print("C1: f3 works")

    def show(self):
        print("C1 show")


obj2 = C1()
obj2.show()
B1.show(obj2)
A1.show(obj2)
