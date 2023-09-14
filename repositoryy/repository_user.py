from pony.orm import db_session, select
import sys
sys.path.append("/app")
from models.base_model import UserM, CarM


class UserRepo:

    def __init__(self):
        self.model = UserM

    @db_session
    def get_by_id(self, id: int):
        user = self.model.get(lambda u: u.id == id)
        user.cars.load()

        return user

    @db_session
    def get_all_users(self):
        all_users = self.model.select(lambda u: u).prefetch(CarM)[:]
        # Load the 'cars' collection for each user within the active session
        for user in all_users:
            user.cars.load()
        return all_users

    @db_session
    def get_all_users_by_name(self, name):
        users_by_name = select(u for u in UserM if u.name == name).prefetch(CarM).page(1).to_list()
        for user in users_by_name:
            user.cars.load()
        return users_by_name

    @db_session
    def update_user_info(self, id, age, name, country, city, email, password):
        user = self.get_by_id(id)
        user.age = age
        user.name = name
        user.country = country
        user.city = city
        user.email = email
        user.password = password

    @db_session
    def create_new_user(self, age, name, country, city, email, password):
        UserM(age=age, name=name, country=country, city=city, email=email, password=password)

    @db_session
    def delete_user_by_id(self, id: int):
        user = select(u for u in self.model if u.id == id)
        user.delete()


if __name__ == '__main__':
    repo = UserRepo()
    print(f"This is user with ID=4: \n{repo.get_by_id(id=4)}\n")
    # repo.update_user_info(10, 20, 'Mugiwaraya', 'Spain', 'Barcelona', 'mugiwaraya@example.com', 'basepass4')
    users = repo.get_all_users()
    print("Get all users: ", *users, sep='\n')

    print(f"Get user by name: \n{repo.get_all_users_by_name('Juan Perez')}")
    # print(f"This is user with ID=11: \n{repo.get_by_id(id=11, with_cars=True)}\n")
    # repo.create_new_user(24, 'Roman T', 'Ukraine', 'Kyiv', 'romant@example.com', 'basepass7')

    # repo.delete_user_by_id(11)
