import Pyro5.api
from Pyro5.api import SerializerBase
import car


@Pyro5.api.expose
class Crud:
    def __init__(self):
        self._car_dict = {}

    def add(self, obj:car.Car) -> int: 
        self._car_dict[obj._lic_plate] = obj

    def delete(self, lic_plate:str) -> int:
        if lic_plate in self._car_dict:
            del self._car_dict[lic_plate]

    def update(self, obj:car.Car):
        if self._car_dict[obj._lic_plate]:
            self._car_dict[obj._lic_plate] = obj
            

    def get_car(self, lic_plate:str) -> car.Car:
        return self._car_dict[lic_plate]

def main():
    daemon = Pyro5.api.Daemon()
    ns = Pyro5.api.locate_ns() 
    uri = daemon.register(Crud)
    ns.register("lucas_rafael", uri)

    SerializerBase.register_dict_to_class("car.Car", car.dict_to_Car)
    SerializerBase.register_class_to_dict(car.Car, car.Car_to_dict)

    print(uri)

    input() 

    daemon.requestLoop()


if __name__ == "__main__":
    main()