import PySimpleGUI as sg
from random import randint

global max_arv
max_arv = 10

def uus_tehe(operation):
    a = randint(0, max_arv)
    b = randint(0, a)
    
    if operation == 'LIITMINE':
        tekst = f"{a} + {b} = ?"
        lahendus = a + b
    elif operation == 'LAHUTAMINE':
        tekst = f"{a} - {b} = ?"
        lahendus = a - b
    elif operation == 'KORRUTAMINE':
        tekst = f"{a} * {b} = ?"
        lahendus = a * b
    elif operation == 'JAGAMINE':
        b = randint(1, max_arv)
        tekst = f"{a} / {b} = ?"
        lahendus = a / b
    
    return [tekst, lahendus]

def create_operation_window(operation):
    tehe, lahendus = uus_tehe(operation)
    layout = [
        [sg.Text(tehe)],
        [sg.InputText(key='USER_ANSWER')],
        [sg.Button('Kontrolli'), sg.Button('Tagasi')]
    ]
    return sg.Window("Rehkendusinator3000 - Tehe", layout), lahendus

def create_main_window():
    layout = [
        [sg.Text("Mis tehteid soovid teha?")],
        [sg.Radio('Liitmine', 'CATEGORY', key='LIITMINE'), sg.Radio('Lahutamine', 'CATEGORY', key='LAHUTAMINE')],
        [sg.Radio('Korrutamine', 'CATEGORY', key='KORRUTAMINE'), sg.Radio('Jagamine', 'CATEGORY', key='JAGAMINE')],
        [sg.Button('Ok'), sg.Button('Cancel')]
    ]
    return sg.Window("Rehkendusinator3000", layout)

window = create_main_window()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Ok':
        if values['LIITMINE']:
            operation = 'LIITMINE'
        elif values['LAHUTAMINE']:
            operation = 'LAHUTAMINE'
        elif values['KORRUTAMINE']:
            operation = 'KORRUTAMINE'
        elif values['JAGAMINE']:
            operation = 'JAGAMINE'

        window.close()

        operation_window, correct_answer = create_operation_window(operation)
        
        while True:
            op_event, op_values = operation_window.read()
            if op_event == sg.WIN_CLOSED or op_event == 'Tagasi':
                operation_window.close()
                break  # Väljuge tehete lahendamise tsüklist
            if op_event == 'Kontrolli':
                try:
                    user_answer = float(op_values['USER_ANSWER'])
                    if user_answer == correct_answer:
                        sg.popup("Õige vastus!")
                    else:
                        sg.popup(f"Vale vastus! Õige vastus on: {correct_answer}")
                except ValueError:
                    sg.popup("Palun sisestage kehtiv number.")

                # Generatsioon uue tehte jaoks
                operation_window.close()  # Sulgeme vana akna
                operation_window, correct_answer = create_operation_window(operation)  # Loome uue akna

        window = create_main_window()  # Avame tehete valimise akna

window.close()