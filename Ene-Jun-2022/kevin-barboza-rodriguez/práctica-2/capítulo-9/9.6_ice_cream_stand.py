from restaurant import Restaurant

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate","strawberry","vanilla"]
    
    def show_flavors(self):
        print(f"flavors: {self.flavors}")

if __name__ == "__main__":
    restaurant = IceCreamStand("holanda", "ice cream stand")
    print(f"restaurant name: {restaurant.restaurant_name}")
    print(f"cuisine type: {restaurant.cuisine_type}")

    print("\nrestaurant description")
    restaurant.describe_restaurant()

    print("\nopenning restaurant...")
    restaurant.open_restaurant()

    restaurant.show_flavors()