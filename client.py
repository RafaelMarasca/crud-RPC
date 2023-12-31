""" 
Este arquivo implementa o cliente para chamadas de objeto remoto
"""

__author__ = "Lucas Carvalho and Rafael Marasca Martins"


import Pyro5.api
from Pyro5.api import SerializerBase
import car
import codes
import gui as g

def main():
    #Instancia a interface gráfica
    interface = g.gui()

    #Cria o proxy que interceptará as chamadas locais
    crud = Pyro5.api.Proxy("PYRONAME:lucas_rafael")
    
    #Bloqueia até que a ok seja pressionado
    interface.pop_up_ok('Proxy ok!')

    #Registra os métodos de serialização
    SerializerBase.register_class_to_dict(car.Car, car.Car_to_dict)
    SerializerBase.register_dict_to_class('car.Car', car.dict_to_Car)

    #Tenta associar o proxy ao objeto remoto 
    try:
        crud._pyroBind()
        interface.pop_up_ok('Bind ok!')
    except:
        interface.pop_up_fatal_error('Um erro Ocorreu! \n Encerrando Aplicação!')
        return


    #Laço para requisições
    while True:
        op = interface.get_event()

        if(op == codes.END):
            break 

        #Operação de Criação
        elif(op == codes.CREATE):   
            entry = interface.get_fields()
            try:
                crud.add(car.Car(entry['plate'], entry['brand'], entry['model'], entry['year'], entry['km'], entry['fuel']))
                interface.pop_up_success("Registro Criado com Suceso!")
                interface.clear()
            except Exception:
                interface.pop_up_error("Erro ao Criar Registro!")

        #Operação de Leitura
        elif(op == codes.READ):
            #Pega os dados da interface
            entry = interface.get_fields()
            try:
                c = crud.get_car(entry['plate'])
                #Atualiza a interface
                interface.set_fields(c._lic_plate, c._model, c._brand, c._year, c._km, c._fuel)
                interface.pop_up_success("Registro Lido com Sucesso!")
            except KeyError:
                interface.pop_up_error("Registro não Encontrado!")
            except Exception:
                interface.pop_up_error("Erro na Leitura!")
            
        
        #Operação de Atualização
        elif(op == codes.UPDATE):
            #Pega os dados da interface
            entry = interface.get_fields()

            try:
                crud.update(car.Car(entry['plate'], entry['brand'], entry['model'], entry['year'], entry['km'], entry['fuel']))
                interface.pop_up_success("Registro Atualizado com Sucesso!")
                interface.clear()
            except KeyError:
                interface.pop_up_error("Registro não Encontrado!")
            except Exception:
                interface.pop_up_error("Erro de Atualização!")

        #Operação de Exclusão
        elif(op == codes.DELETE):
            entry = interface.get_fields()

            try:
                crud.delete(entry['plate'])
                interface.pop_up_success("Registro Deletado com Sucesso!")
                interface.clear()
            except KeyError:
                interface.pop_up_error('Registro não Encontrado!')
            except Exception:
                interface.pop_up_error('Erro de Exclusão!')

if __name__ == "__main__":
    main()