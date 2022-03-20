class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"restaurant name: {self.restaurant_name} \ncuisine type: {self.cuisine_type}")

    def open_restaurant(self):
        print(self.restaurant_name + "is open")

    def set_number_served(self, number):
        self.number_served += number

restaurant = Restaurant("Ta´ sabrozo", "Mexican food")

print(f"restaurant name: {restaurant.restaurant_name}")
print(f"cuisine type: {restaurant.cuisine_type}")

print("\nrestaurant description")
restaurant.describe_restaurant()

print("\nopenning restaurant...")
restaurant.open_restaurant()

print(f"\nnumber of customers: {restaurant.number_served}")
restaurant.set_number_served(10)
print(f"\nnumber of customers: {restaurant.number_served}")