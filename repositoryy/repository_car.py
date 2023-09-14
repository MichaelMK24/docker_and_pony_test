from pony.orm import db_session, select
import sys
sys.path.append("/app")
from models.base_model import UserM, CarM


class CarRepo:

    def __init__(self):
        self.model = CarM

    @db_session
    def get_by_id(self, car_id: int):
        car = self.model.get(lambda c: c.car_id == car_id)
        car.user.load()
        return car

    @db_session
    def get_all_cars(self):
        all_cars = self.model.select(lambda c: c).prefetch(UserM)[:]
        return all_cars

    @db_session
    def get_by_brand(self, brand: str):
        cars = select(cb for cb in CarM if cb.brand == brand).prefetch(UserM)[:]
        for car in cars:
            car.user.load()
        return cars

    @db_session
    def get_by_model(self, model: str):
        cars = select(cb for cb in CarM if cb.model == model).page(1).to_list()
        for car in cars:
            car.user.load()
        return cars

    @db_session
    def get_car_below_mileage(self, mileage: int):
        cars = self.model.select(lambda c: c.mileage < mileage)[:]
        for car in cars:
            car.user.load()
        return cars

    @db_session
    def update_car_info(self, car_id: int, brand: str, model: str, mileage: int):
        car_upd = self.get_by_id(car_id)
        car_upd.brand = brand
        car_upd.model = model
        car_upd.mileage = mileage

    @db_session
    def create_new_car(self, user_id: int, brand: str, model: str, mileage: int):
        CarM(user=user_id, brand=brand, model=model, mileage=mileage)

    @db_session
    def delete_car_by_id(self, car_id: int):
        car_del = self.model.get(lambda c: c.car_id == car_id)
        car_del.delete()


if __name__ == '__main__':
    repo_car = CarRepo()
    # print(repo_car.get_by_id(13))
    print(f"Get car by brand: \n{repo_car.get_by_brand('Audi')}")
    print(f"Get car by model: \n{repo_car.get_by_model('Jetta')}")
    low_mileage_cars = repo_car.get_car_below_mileage(50000)
    print("Low mileage cars: ", *low_mileage_cars, sep='\n')
    # repo_car.update_car_info(12, 'Audi', 'RS8', 73112)

    # repo_car.create_new_car(12, 'Audi', 'RS8', 73112)
    # repo_car.delete_car_by_id(15)

    print(f"All available cars: ", *repo_car.get_all_cars(), sep='\n')


