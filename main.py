import tkinter as tk
from tkinter import messagebox
from random import randint, choice

global max_arv
max_arv = 10 # Maksimaalne arv, mis tehetes kasutusel on

# Hoiame juba genereeritud vastuseid
generated_answers = set()

# Funktsioon uue tehte loomiseks
def uus_tehe(operations):
    operation = choice(operations)
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

    return tekst, lahendus

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.total_questions = 0
        self.correct_answer = None
        self.operations = ['LIITMINE', 'LAHUTAMINE', 'KORRUTAMINE', 'JAGAMINE']
        self.selected_operations = []
        self.initUI()

    # UI loomine
    def initUI(self):
        self.title('Rehkendusinator3000')
        self.geometry('350x300') # Akna suurus

        self.tehe_label = tk.Label(self, text='Tehe:', font=('Arial', 9))
        self.tehe_label.pack(pady=10) 

        self.answer_input = tk.Entry(self, font=('Arial', 9))
        self.answer_input.pack(pady=10)

        self.check_button = tk.Button(self, text='Kontrolli', command=self.check_answer, font=('Arial', 9))
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(self, text='', font=('Arial', 9))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self, text='Punktid: 0 / 0', font=('Arial', 9))
        self.score_label.pack(pady=10)

        self.operation_vars = {op: tk.BooleanVar(value=True) for op in self.operations}
        operation_frame = tk.Frame(self)
        operation_frame.pack(pady=10)

        # Loome valikvastused ja paigutame need kahte tulpa
        for i, op in enumerate(self.operations):
            cb = tk.Checkbutton(operation_frame, text=op, variable=self.operation_vars[op], font=('Arial', 9))
            cb.grid(row=i//2, column=i%2, padx=10, pady=5)

        self.new_tehe()

    # Uue tehte loomine
    def new_tehe(self):
        # Valime kasutaja poolt valitud tehete kategooriad
        self.selected_operations = [op for op, var in self.operation_vars.items() if var.get()]
        if not self.selected_operations:
            messagebox.showwarning("Hoiatus", "Palun valige vähemalt üks tehe.")
            return
        self.tehe, self.correct_answer = uus_tehe(self.selected_operations)  # Loome uue tehte
        self.tehe_label.config(text=f'Tehe: {self.tehe}')
        self.answer_input.delete(0, tk.END)
        self.result_label.config(text='')

    # Kasutaja vastuse kontrollimine
    def check_answer(self):
        try:
            user_answer = float(self.answer_input.get())
            self.total_questions += 1
            if user_answer == self.correct_answer:
                self.score += 1 # Suurendame õige vastuse korral punktisummat
                self.result_label.config(text="Õige vastus!", fg='green')
            else:
                self.result_label.config(text=f"Vale vastus! Õige vastus on: {self.correct_answer}", fg='red') # Vale vastuse korral näitame õiget vastust

            self.score_label.config(text=f'Punktid: {self.score} / {self.total_questions}')
            # Näitame tulemust ja ootame enne uue tehte loomist
            self.after(800, self.new_tehe)

        except ValueError:
            self.result_label.config(text="Palun sisestage kehtiv number.", fg='red')

# Peamise akna loomine ja käivitamine
def create_main_window():
    window = MainWindow()
    window.mainloop()

if __name__ == '__main__':
    create_main_window()
