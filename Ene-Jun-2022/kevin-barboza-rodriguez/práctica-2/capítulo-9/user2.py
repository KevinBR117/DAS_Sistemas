class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"the user {self.first_name} {self.last_name} has {self.age} years old")

    def greet_user(self):
        print(f"Hi {self.first_name}")

class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.priv = Privileges()
        self.admin = True

    def is_admin(self):
        print(f"is admin? {self.admin}")

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can be user"]

    def show_privileges(self):
        print(f"privileges {self.privileges}")