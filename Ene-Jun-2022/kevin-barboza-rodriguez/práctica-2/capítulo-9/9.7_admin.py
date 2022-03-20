from users import User

class Admin(User):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges = ["can add post", "can delete post", "can be user"]

    def show_privileges(self):
        print(f"privileges {self.privileges}")

if __name__ == "__main__":
    user1 = Admin("Kevin", "Barboza", 21)
    user1.describe_user()
    user1.greet_user()
    user1.show_privileges()