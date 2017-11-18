class A():
    def __init__(self):
        pass
    def save(self):
        print("This is from A")
class B(A):
    def __init__(self):
        pass
class C(A):
    def __init__(self):
        pass
    def save(self):
        print("This is from C")
class D(B,C):
    def __init__(self):
        pass
