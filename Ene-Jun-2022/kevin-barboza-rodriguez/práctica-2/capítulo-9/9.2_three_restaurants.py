class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"restaurant name: {self.restaurant_name} \ncuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(self.restaurant_name + "is open")

restaurant = Restaurant("Ta´ sabrozo", "Mexican food")
restaurant1 = Restaurant("Taco master", "Mexican food")
restaurant2 = Restaurant("Luigui's", "Italian food")


print("\nrestaurant description")
restaurant.describe_restaurant()

print("\nrestaurant description")
restaurant1.describe_restaurant()

print("\nrestaurant description")
restaurant2.describe_restaurant()