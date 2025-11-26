class A:
    def process(self):
        print("A is Initial Processing")

class B(A):
    def process(self):
        print("B : Starting B's Process")
        super().process()
        print("B : Finishing B's Process")

class C(A):
    def process(self):
        print("C : Starting C's Process")
        super().process()
        print("C : Finishing C'S Process")

class D(B , C):
    def process(self):
        print("D : Staring D's Combine Process")
        # Calls the next class in MRO (which is B, based on order)
        super().process()
        print("D : Finishing D's Combine Process")

print(D.mro())

obj = D()
print(obj.process())