from users import User
from admin import Admin
from privileges import Privileges

if __name__ == "__main__":
    user1 = Admin(User("kevin", "barboza", 21))
    user1.priv = Privileges()
    user1.describe_user()
    user1.greet_user()
    user1.is_admin()
    user1.priv.show_privileges()