from user2 import *

if __name__ == "__main__":
    user1 = Admin("Kevin", "Barboza", 21)
    user1.describe_user()
    user1.greet_user()
    user1.is_admin()
    user1.priv.show_privileges()
