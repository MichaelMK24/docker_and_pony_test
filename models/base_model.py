from pony.orm import Database
from pony.orm import PrimaryKey, Required, Optional, Set

db = Database()
db.bind(provider='postgres', user='postgres', password='Admin24', host='host.docker.internal', database='20_05AQA_Group')


class UserM(db.Entity):
    _table_ = 'users'
    id = PrimaryKey(int, auto=True)
    age = Required(int)
    name = Required(str, 100)
    country = Required(str, 100)
    city = Required(str, 100)
    email = Required(str, 100)
    password = Required(str, 100)
    cars = Set('CarM')

    def __str__(self):
        cars_info = ", ".join([f"Brand-{car.brand} Model-{car.model} Mileage-{car.mileage}" for car in self.cars])
        return f"ID: {self.id} Age: {self.age} Name: {self.name} Country: {self.country} City: {self.city} " \
               f"Email: {self.email} Password: {self.password} Cars: {cars_info}"

    def __repr__(self):
        cars_info = ", ".join([f"Brand-{car.brand} Model-{car.model} Mileage-{car.mileage}" for car in self.cars])
        return f"ID: {self.id} Age: {self.age} Name: {self.name} Country: {self.country} City: {self.city} " \
               f"Email: {self.email} Password: {self.password} Cars: {cars_info}"


class CarM(db.Entity):
    _table_ = 'cars'
    car_id = PrimaryKey(int, auto=True)
    # user_id = Column(ForeignKey("users.id"))
    brand = Required(str, 100)
    model = Required(str, 100)
    mileage = Required(int)
    user = Required(UserM, column='user_id')

    def __str__(self):
        return f"Car_id: {self.car_id} Brand: {self.brand} Model: {self.model} " \
               f"Mileage: {self.mileage} owner: {self.user.name}"

    def __repr__(self):
        return f"Car_id: {self.car_id} Brand: {self.brand} Model: {self.model} " \
               f"Mileage: {self.mileage} owner: {self.user.name}"


db.generate_mapping(create_tables=True)

