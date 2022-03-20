from restaurant import Restaurant

if __name__ == "__main__":
    restaurant = Restaurant("Ta´ sabrozo", "Mexican food")

    print("\nrestaurant description")
    restaurant.describe_restaurant()

    print("\nopenning restaurant...")
    restaurant.open_restaurant()