import PySimpleGUI as sg
from random import randint

def uus_tehe():
    #Kas liitmine või lahutamine
    i = randint(0, 1)
    x = "+"
    if i == 0:
        i = -1
        x = "-"
    #Määra suvalised arvud
    a = randint(0, max_arv)
    b = randint(0, a)
    #Vormista tehe
    tekst = str(a) + x + str(b) + "= ?"
    lahendus = a + i * b
    return [tekst, lahendus]

global max_arv
max_arv = 10


# Loome rehkenduse akna
def create_operation_window(operation):
    if operation == 'LIITMINE':
        layout = [
            [sg.Text("Liitmine: Sisesta kaks arvu")],
            [sg.InputText(key='NUM1'), sg.InputText(key='NUM2')],
            [sg.Button('Arvuta'), sg.Button('Tagasi')]
        ]
    elif operation == 'LAHUTAMINE':
        layout = [
            [sg.Text("Lahutamine: Sisesta kaks arvu")],
            [sg.InputText(key='NUM1'), sg.InputText(key='NUM2')],
            [sg.Button('Arvuta'), sg.Button('Tagasi')]
        ]
    elif operation == 'KORRUTAMINE':
        layout = [
            [sg.Text("Korrutamine: Sisesta kaks arvu")],
            [sg.InputText(key='NUM1'), sg.InputText(key='NUM2')],
            [sg.Button('Arvuta'), sg.Button('Tagasi')]
        ]
    elif operation == 'JAGAMINE':
        layout = [
            [sg.Text("Jagamine: Sisesta kaks arvu")],
            [sg.InputText(key='NUM1'), sg.InputText(key='NUM2')],
            [sg.Button('Arvuta'), sg.Button('Tagasi')]
        ]

    return sg.Window(f"{operation} - Rehkendusinator3000", layout)

# Peamine aken tehete valimiseks
def create_main_window():
    layout = [
        [sg.Text("Mis tehteid soovid teha?")],
        [sg.Text("Vali tehte liik:")],
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
            operation_window = create_operation_window('LIITMINE')
        elif values['LAHUTAMINE']:
            operation_window = create_operation_window('LAHUTAMINE')
        elif values['KORRUTAMINE']:
            operation_window = create_operation_window('KORRUTAMINE')
        elif values['JAGAMINE']:
            operation_window = create_operation_window('JAGAMINE')

        window.close()
    
        while True: # Tehtega tegevus
            op_event, op_values = operation_window.read()
            if op_event == sg.WIN_CLOSED or op_event == 'Tagasi':
                operation_window.close()
                window = create_main_window()
                break
            if op_event == 'Arvuta':
                num1 = float(op_values['NUM1'])
                num2 = float(op_values['NUM2'])
                if values['LIITMINE']:
                    result = num1 + num2
                    sg.popup(f"Tulemus: {result}")
                elif values['LAHUTAMINE']:
                    result = num1 - num2
                    sg.popup(f"Tulemus: {result}")
                elif values['KORRUTAMINE']:
                    result = num1 * num2
                    sg.popup(f"Tulemus: {result}")
                elif values['JAGAMINE']:
                    if num2 != 0:
                        result = num1 / num2
                        sg.popup(f"Tulemus: {result}")
                    else:
                        sg.popup("Jagamine nulliga ei ole lubatud!")

window.close()