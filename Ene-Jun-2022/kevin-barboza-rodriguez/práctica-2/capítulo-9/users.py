#exersice 9.3
class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"the user {self.first_name} {self.last_name} has {self.age} years old")

    def greet_user(self):
        print(f"Hi {self.first_name}")

if __name__ == "__main__":
    user1 = User("Kevin", "Barboza", 21)
    user2 = User("Osvaldo","Barboza", 23)
    user3 = User("Arturo", "Rodriguez", 24)

    user1.describe_user()
    user1.greet_user()

    user2.describe_user()
    user2.greet_user()

    user3.describe_user()
    user3.greet_user()