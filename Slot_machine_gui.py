from tkinter import *
import random


class GUI:
    """
    A class representing a slot machine in GUI
    """
    def __init__(self, window):
        """
        The user interface is created here
        :param window: Creates a GUI window
        """
        self.window = window

        self.frame_slot = Frame(self.window)
        self.label_wheel1 = Label(self.frame_slot, text='1')
        self.label_wheel2 = Label(self.frame_slot, text='1')
        self.label_wheel3 = Label(self.frame_slot, text='1')

        self.label_wheel1.pack(side='left')
        self.label_wheel2.pack(side='left')
        self.label_wheel3.pack(side='left')
        self.frame_slot.pack()

        self.frame_bet = Frame(self.window)
        self.label_bet = Label(self.frame_bet, text='Please Place Your Bet')
        self.label_money = Label(self.frame_bet, text='$')
        self.entry_amount = Entry(self.frame_bet)
        self.label_bet.pack()
        self.label_money.pack(side='left')
        self.entry_amount.pack(side='left')
        self.frame_bet.pack()

        self.frame_play = Frame(self.window)
        self.button_play = Button(self.frame_play, text='Play', command=self.play_slots)
        self.button_play.pack()
        self.frame_play.pack()

        self.frame_output = Frame(self.window)
        self.label_output = Label(self.frame_output, text='Amount You Won')
        self.label_user_output = Label(self.frame_output)
        self.label_output.pack()
        self.label_user_output.pack()
        self.frame_output.pack()

    def play_slots(self):
        """
        function to generate 3 random numbers and then calculate an amount based on the bet amount
        :return:
        """

        amount1 = self.entry_amount.get()

        value1 = random.randint(1, 5)
        value2 = random.randint(1, 5)
        value3 = random.randint(1, 5)

        self.label_wheel1.config(text=f'{value1}')
        self.label_wheel2.config(text=f'{value2}')
        self.label_wheel3.config(text=f'{value3}')

        try:
            amount2 = float(amount1)
            if value1 == 5 and value2 == 5 and value3 == 5:
                final = amount2 * 10
                self.label_output.config(text=f'You won ${final}')
                self.entry_amount.delete(0, END)
                self.label_user_output.config(text=f'You placed a ${amount1} bet')
            elif value1 == 4 and value2 == 4 and value3 == 4:
                final = amount2 * 5
                self.label_output.config(text=f'You won ${final}')
                self.entry_amount.delete(0, END)
                self.label_user_output.config(text=f'You placed a ${amount1} bet')
            elif value1 == 3 and value2 == 3 and value3 == 3:
                final = amount2 * 4
                self.label_output.config(text=f'You won ${final}')
                self.entry_amount.delete(0, END)
                self.label_user_output.config(text=f'You placed a ${amount1} bet')
            elif value1 == 2 and value2 == 2 and value3 == 2:
                final = amount2 * 3
                self.label_output.config(text=f'You won ${final}')
                self.entry_amount.delete(0, END)
                self.label_user_output.config(text=f'You placed a ${amount1} bet')
            elif value1 == 1 and value2 == 1 and value3 == 1:
                final = amount2 * 2
                self.label_output.config(text=f'You won ${final}')
                self.entry_amount.delete(0, END)
                self.label_user_output.config(text=f'You placed a ${amount1} bet')
            else:
                self.label_output.config(text=f'You Lost ${amount2}')
                self.entry_amount.delete(0, END)
                self.label_user_output.config(text=f'You placed a ${amount1} bet')

        except ValueError:
            self.label_output.config(text='Error spin is forfeit ')
            self.entry_amount.delete(0, END)
            self.label_user_output.config(text=' ')