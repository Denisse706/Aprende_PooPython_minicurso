#method resolution order

class A():
    def hablar(self):
        print ("Hola desde A")

class B(A):
    def hablar(self):
        pass

class C(A):
    def hablar(self):
        print ("Bienvenido a C")

class D(C):
    def hablar(self):
        print ("Bienvenido a D")

X = B()

B.hablar(X)

print (D.mro())

