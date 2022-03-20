class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can be user"]

    def show_privileges(self):
        print(f"privileges {self.privileges}")