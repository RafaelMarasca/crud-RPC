class Car:
    def __init__(self, lic_plate:str, brand:str, model:str, year:int, km:int, fuel:str):
        self._lic_plate = lic_plate
        self._brand = brand
        self._model = model
        self._year = year
        self._km = km
        self._fuel = fuel

    def imprimir (self):
        print(self.lic_plate)
    

def Car_to_dict(obj:Car) -> dict:
    temp = {
        "__class__": "car.Car",
        "lic_plate": obj._lic_plate,
        "brand": obj._brand,
        "model": obj._model,
        "year" : obj._year,
        "km" : obj._km,
        "fuel" : obj._fuel
    }

    return temp

def dict_to_Car(classname, obj:dict)->Car:
    if classname != "car.Car":
        return None

    return Car(obj['lic_plate'], obj['brand'], obj['model'], obj['year'], obj['km'], obj['fuel'])
