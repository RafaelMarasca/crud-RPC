#!/usr/bin/env python
""" 
Este arquivo implementa a classe CRUD que
define os objetos remotos. Além disso, é aqui
criado o servidor no método main().
"""

__author__ = "Lucas Carvalho and Rafael Marasca Martins"

import Pyro5.api
from Pyro5.api import SerializerBase
import car

#Classe Crud acessível remotamente
@Pyro5.api.expose
class Crud:

    def __init__(self):
        #Dicionário vazio como armazenamento interno
        self._car_dict = {}

    #Adiciona um novo registro ao dicionário interno
    def add(self, obj:car.Car) -> int: 
        self._car_dict[obj._lic_plate] = obj

    #Remove um registro do dicionário interno
    def delete(self, lic_plate:str) -> int:
        if lic_plate in self._car_dict:
            del self._car_dict[lic_plate]

    #Atualiza um registro do dicionário interno
    def update(self, obj:car.Car):
        if self._car_dict[obj._lic_plate]:
            self._car_dict[obj._lic_plate] = obj

    #Busca e retorna um registro do dicionário itnerno
    def get_car(self, lic_plate:str) -> car.Car:
        return self._car_dict[lic_plate]

#Implementação do servidor
def main():

    #Cria o daemon do servidor
    daemon = Pyro5.api.Daemon()

    #Localiza o serviço de nomes
    ns = Pyro5.api.locate_ns() 

    #Registra o objeto remoto (com o nome requerido no enunciado) no nameservice
    uri = daemon.register(Crud)
    ns.register("lucas_rafael", uri)

    #Registra os métodos de serialização
    SerializerBase.register_dict_to_class("car.Car", car.dict_to_Car)
    SerializerBase.register_class_to_dict(car.Car, car.Car_to_dict)

    #Printa o uri
    print(uri)

    ##Aguarda um input do usuário
    input('Enter para entrar no loop de requisições') 

    #Loop de Requisições
    daemon.requestLoop()


if __name__ == "__main__":
    main()