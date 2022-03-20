#from users import User
class Admin(object()):
    def __init__(self,first_name,last_name,age):
        object().__init__(first_name,last_name,age)
        self.priv  = ""
        self.admin = True


    def is_admin(self):
        print(f"is admin? {self.admin}")