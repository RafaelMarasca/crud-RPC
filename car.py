#!/usr/bin/env python
""" 
Este arquivo fornece definições da
classe Car, bem como funções de conversão
de objetos do tipo Car para dicionário.
"""

__author__ = "Lucas Carvalho and Rafael Marasca Martins"

#Classe Car para armazenamento das informações acerca de um carro
class Car:
    def __init__(self, lic_plate:str, brand:str, model:str, year:int, km:int, fuel:str):
        self._lic_plate = lic_plate
        self._brand = brand
        self._model = model
        self._year = year
        self._km = km
        self._fuel = fuel
    

#Converte um objeto do tipo Car para dicionário
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

#Converte um dicionário para um objeto do tipo Car 
def dict_to_Car(classname, obj:dict)->Car:
    if classname != "car.Car":
        return None

    return Car(obj['lic_plate'], obj['brand'], obj['model'], obj['year'], obj['km'], obj['fuel'])
