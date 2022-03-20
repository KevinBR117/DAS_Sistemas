def make_car(manufacter, model, **car_info):
    car = {}
    car['manufacter'] = manufacter
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

car_profile = make_car('toyota', 'corolla',
                color='blue', doors=4)
print(car_profile)