def make_car(manufacter, model, **car_info):
    car = {}
    car['manufacter'] = manufacter
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car