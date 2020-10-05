class MyAdminUser:
    def __init__(self):
        self.name = None
        self.age = None
        self.level = 0

user_1 = MyAdminUser()
print(type(user_1))
print(dir(user_1))