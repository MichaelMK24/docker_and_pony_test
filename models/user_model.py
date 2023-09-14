from pony.orm import PrimaryKey, Required, Set
from Kobryn_AQA_course.lesson_25_pony.models.base_model import db


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
        return f"ID: {self.id} Age: {self.age} Name: {self.name} Country: {self.country} City: {self.city} " \
               f"Email: {self.email} Password: {self.password} Cars: {self.cars}"

    def __repr__(self):
        return f"ID: {self.id} Age: {self.age} Name: {self.name} Country: {self.country} City: {self.city} " \
               f"Email: {self.email} Password: {self.password} Cars: {self.cars}"


db.generate_mapping(create_tables=True)
