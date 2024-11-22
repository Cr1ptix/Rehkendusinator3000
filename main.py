import PySimpleGUI as sg
from random import randint

global max_arv
max_arv = 10

# Hoidame juba genereeritud vastuseid
generated_answers = set()

def uus_tehe(operation):
    a = randint(0, max_arv)
    
    if operation == 'LIITMINE':
        b = randint(0, a)
        tekst = f"{a} + {b} = ?"
        lahendus = a + b
    elif operation == 'LAHUTAMINE':
        b = randint(0, a)
        tekst = f"{a} - {b} = ?"
        lahendus = a - b
    elif operation == 'KORRUTAMINE':
        b = randint(0, a)
        tekst = f"{a} * {b} = ?"
        lahendus = a * b
    elif operation == 'JAGAMINE':
        if a == 0:
            b = 1  # Kui a on 0, siis jagame 1-ga, et vältida jagamist nulliga
        else:
            # Valime jagaja b, mis jagab a täpselt
            divisors = [i for i in range(1, a + 1) if a % i == 0]
            b = divisors[randint(0, len(divisors) - 1)]  # Valime suvalise jagaja
        tekst = f"{a} / {b} = ?"
        lahendus = a // b  # Kasutame täisarv jagamist

    return [tekst, lahendus]

def create_operation_window(operation, score):
    global generated_answers
    while True:
        tehe, lahendus = uus_tehe(operation)
        if lahendus not in generated_answers:
            generated_answers.add(lahendus)
            break
    
    layout = [
        [sg.Text(tehe, key='TEXT')],  # Lisame TEXT võtme
        [sg.InputText(key='USER_ANSWER')],
        [sg.Text('', key='RESULT', size=(40, 1))],  # Tulemuse tekst
        [sg.Text(f"Punktid: {score}", key='SCORE')],  # Punktide tekst
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
score = 0  # Algne punktide arv

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

        operation_window, correct_answer = create_operation_window(operation, score)
        
        while True:
            op_event, op_values = operation_window.read()
            if op_event == sg.WIN_CLOSED or op_event == 'Tagasi':
                operation_window.close()
                break  # Väljuge tehete lahendamise tsüklist
            if op_event == 'Kontrolli':
                try:
                    user_answer = float(op_values['USER_ANSWER'])
                    if user_answer == correct_answer:
                        score += 1  # Suurendame punkte õigete vastuste eest
                        operation_window['RESULT'].update("Õige vastus!")  # Uuendame tulemuse teate
                    else:
                        score -= 1  # Vähendame punkte vale vastuse eest
                        operation_window['RESULT'].update(f"Vale vastus! Õige vastus on: {correct_answer}")  # Uuendame tulemuse teate
                    
                    # Uuendame punktide näitamise teksti
                    operation_window['SCORE'].update(f"Punktid: {score}")

                    # Generatsioon uue tehte jaoks
                    new_tehe, new_correct_answer = uus_tehe(operation)  # Loome uue tehte
                    operation_window['TEXT'].update(new_tehe)  
                    correct_answer = new_correct_answer  # Uuendame õige vastuse
                    operation_window['USER_ANSWER'].update('')  # Tühjendame sisendi väärtuse

                except ValueError:
                    operation_window['RESULT'].update("Palun sisestage kehtiv number.")  # Uuendame tulemuse teate

        window = create_main_window()  # Avame tehete valimise akna

window.close()