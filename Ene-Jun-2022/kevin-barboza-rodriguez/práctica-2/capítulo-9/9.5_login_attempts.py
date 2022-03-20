class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"the user {self.first_name} {self.last_name} has {self.age} years old")

    def greet_user(self):
        print(f"Hi {self.first_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Kevin", "Barboza", 21)
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"number of login attemps: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"number of login attemps: {user1.login_attempts}")


