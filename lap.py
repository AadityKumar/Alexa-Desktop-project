# class Student:
#     def detail(self):
#         print("hello bharat")

# obj = Student()
# obj.detail()


class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return self.radius**2*3.14
    def primeter(self):
        return self.radius*2*3.14

obj = Circle(8)
print(f"Area of Circle = {obj.area()}")
print(f"Primeter of circle= {obj.primeter()}")
