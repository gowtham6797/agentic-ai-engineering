class A:
    def show(self):
        print('in A show')

class B(A):
    def show(self):
        print('in B show')
    # pass

obj1=B()
obj1.show()
A.show(obj1)