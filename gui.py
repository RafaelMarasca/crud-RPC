#!/usr/bin/env python
""" 
Este script implementa uma simples interface
gráfica para a aplicação CRUD para cadastro 
de carros
"""

__author__ = "Lucas Carvalho and Rafael Marasca Martins"

import PySimpleGUI as sg
import codes

sg.theme("DarkBrown1")

win_layout = [
    [
        sg.Text("Placa", size=(15), font=("Arial Baltic", 12)),
        sg.InputText(size = 37, enable_events=True, key="-PLATE-", font=("Arial Baltic", 12))
    ],
    [
        sg.Text("Modelo", size=(15), font=("Arial Baltic", 12)),
        sg.InputText(size = 37, enable_events=True, key="-MODEL-", font=("Arial Baltic", 12))
    ],
    [
        sg.Text("Marca", size=(15), font=("Arial Baltic", 12)),
        sg.InputText(size = 37, enable_events=True, key="-BRAND-", font=("Arial Baltic", 12))
    ],
    [
        sg.Text("Ano", size=(15), font=("Arial Baltic", 12)),
        sg.InputText(size = 37, enable_events=True, key="-YEAR-", font=("Arial Baltic", 12))
    ],
    [
        sg.Text("KM Rodados", size=(15), font=("Arial Baltic", 12)),
        sg.InputText(size = 37, enable_events=True, key="-KMS-", font=("Arial Baltic", 12))
    ],
    [
        sg.Text("Combustível", size=(15), font=("Arial Baltic", 12)),
        sg.InputText(size = 37, enable_events=True, key="-FUEL-", font=("Arial Baltic", 12))
    ],
    [
        sg.Button("Criar", size = (7), enable_events=True, key ="-ADDB-", font=("Arial Baltic", 12)),
        sg.Button("Ler", size = (7), enable_events=True, key ="-REFB-", font=("Arial Baltic", 12)),
        sg.Button("Atualizar", size = (7), enable_events=True, key ="-UPDB-", font=("Arial Baltic", 12)),
        sg.Button("Deletar", size = (7), enable_events=True, key ="-DELB-", font=("Arial Baltic", 12)),
        sg.Button("Limpar", size = (7), enable_events=True, key ="-CLRB-", font=("Arial Baltic", 12))
    ]
]


class gui:
    def __init__(self):
        self.window = sg.Window("CAR CRUD", win_layout, element_justification='c', enable_close_attempted_event=True, finalize=True)

    def get_event(self):
        event, self.values = self.window.read()

        if(event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == "Exit"):
            return codes.END
        elif(event == "-ADDB-"):
            return codes.CREATE
        elif(event == "-REFB-"):
            return codes.READ
        elif(event == "-UPDB-"):
            return codes.UPDATE
        elif(event == "-DELB-"):
            return codes.DELETE
        elif(event == "-CLRB-"):
            self.set_fields("","","","","","")
    
    def set_fields(self, plate, model, brand, year, km, fuel):
        self.window["-PLATE-"].update(plate)
        self.window["-MODEL-"].update(model)
        self.window["-BRAND-"].update(brand)
        self.window["-YEAR-"].update(year)
        self.window["-KMS-"].update(km)
        self.window["-FUEL-"].update(fuel)
    
    def get_fields(self):
        return {'plate': self.values["-PLATE-"],
                'model': self.values["-MODEL-"],
                'brand': self.values["-BRAND-"],
                'year': self.values["-YEAR-"],
                'km': self.values["-KMS-"],
                'fuel': self.values["-FUEL-"]}

    def pop_up_error(self, str):
        sg.popup_ok(str, image=sg.EMOJI_BASE64_FRUSTRATED)

    def pop_up_fatal_error(self, str):
        sg.popup_ok(str,  text_color ='#FF0000', image=sg.EMOJI_BASE64_DEAD)

    def pop_up_ok(self, str):
        sg.popup_ok(str,image=sg.EMOJI_BASE64_THINK)
    
    def pop_up_success(self, str):
        sg.popup_ok(str, image=sg.EMOJI_BASE64_HAPPY_BIG_SMILE)

    
        

    def clear(self):
        self.window["-PLATE-"].update('')
        self.window["-MODEL-"].update('')
        self.window["-BRAND-"].update('')
        self.window["-YEAR-"].update('')
        self.window["-KMS-"].update('')
        self.window["-FUEL-"].update('')

