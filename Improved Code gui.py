from tkinter import *
import math


class GUI:
    """
    A class that is used to create GUI and math calculations
    """
    def __init__(self, window):
        """
        The user interface is created here
        :param window: Creates a GUI window
        """
        self.window = window

        self.frame_shape = Frame(self.window)
        self.label_title = Label(self.frame_shape, text='Select A Shape')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_circle = Radiobutton(self.frame_shape, text='Circle', variable=self.radio_1, value=1,
                                        command=self.circle)
        self.radio_rectangle = Radiobutton(self.frame_shape, text='Rectangle', variable=self.radio_1, value=2,
                                           command=self.rectangle)
        self.radio_square = Radiobutton(self.frame_shape, text='Square', variable=self.radio_1, value=3,
                                        command=self.square)
        self.radio_triangle_area = Radiobutton(self.frame_shape, text='Triangle area', variable=self.radio_1, value=4,
                                          command=self.triangle_area)
        self.radio_triangle_perimeter = Radiobutton(self.frame_shape, text='Triangle perimeter', variable=self.radio_1, value=5,
                                               command=self.triangle_perimeter)
        self.label_title.pack()
        self.radio_circle.pack(side='left')
        self.radio_rectangle.pack(side='left')
        self.radio_square.pack(side='left')
        self.radio_triangle_area.pack(side='left')
        self.radio_triangle_perimeter.pack(side='left')
        self.frame_shape.pack()

        self.frame_area_perimeter = Frame(self.window)
        self.label_area_perimeter = Label(self.frame_area_perimeter, text='Select Area or Perimeter')
        self.button_area = Button(self.frame_area_perimeter, text='Area', command=self.calculate_area)
        self.button_perimeter = Button(self.frame_area_perimeter, text='Perimeter', command=self.calculate_perimeter)
        self.button_calculate_area = Button(self.frame_area_perimeter, text='Calculate', command=self.calculate_area)
        self.button_calculate_perimeter = Button(self.frame_area_perimeter, text='Calculate',
                                             command=self.calculate_perimeter)


        self.frame_area_perimeter.pack()

        self.frame_values = Frame(self.window)
        self.label_value1 = Label(self.frame_values, text='Value1')
        self.label_values = Label(self.frame_values, text='Please type the specified Length(s)')
        self.label_value2 = Label(self.frame_values, text='Value2')
        self.entry_value1 = Entry(self.frame_values, width=40)
        self.label_value3 = Label(self.frame_values, text='Value3')
        self.entry_value2 = Entry(self.frame_values, width=40)
        self.entry_value3 = Entry(self.frame_values, width=40)



        self.frame_values.pack()



        self.frame_output = Frame(self.window)
        self.label_output = Label(self.frame_output, text='The Perimeter or Area is')

        self.frame_output.pack()

    def calculate_area(self):
        """
        this function Calculates all the area equations

        """
        shape = self.radio_1.get()
        if shape == 1:
            value1 = self.entry_value1.get()
            try:
                float_1 = float(value1)
                circle_a = math.pi * (float_1 ** 2)
                self.label_output.config(text=f'The area of the circle is {circle_a}')

            except ValueError:
                self.label_output.config(text='Please type in a number')

        elif shape == 2:

            value1 = self.entry_value1.get()
            value2 = self.entry_value2.get()
            try:
                float_1 = float(value1)
                float_2 = float(value2)
                rectangle_a = float_1 * float_2
                self.label_output.config(text=f'The area of the rectangle is {rectangle_a}')
            except ValueError:
                self.label_output.config(text='Please type in a number')

        elif shape == 3:
            value1 = self.entry_value1.get()
            try:
                float_1 = float(value1)
                square_a = float_1 ** 2
                self.label_output.config(text=f'The area of the square is {square_a}')
            except ValueError:
                self.label_output.config(text='Please type in a number')

        elif shape == 4:
            value1 = self.entry_value1.get()
            value2 = self.entry_value2.get()
            try:
                float_1 = float(value1)
                float_2 = float(value2)
                triangle_a = (float_1 * float_2) / 2
                self.label_output.config(text=f'The area of the triangle is {triangle_a}')
            except ValueError:
                self.label_output.config(text='Please type in a number')

    def calculate_perimeter(self):
        """

        this function Calculates all the perimeter equations
        """
        shape = self.radio_1.get()
        if shape == 1:
            try:
                value1 = self.entry_value1.get()
                circle_p = math.pi * 2 * float(value1)
                self.label_output.config(text=f'The area of the circle is {circle_p}')
            except ValueError:
                self.label_output.config(text='Please type in a number')

        elif shape == 2:
            value1 = self.entry_value1.get()
            value2 = self.entry_value2.get()
            try:
                rectangle_p = 2 * (float(value1) + float(value2))
                self.label_output.config(text=f'The area of the rectangle is {rectangle_p}')
            except ValueError:
                self.label_output.config(text='Please type in a number')

        elif shape == 3:
            value1 = self.entry_value1.get()
            try:
                square_p = 4 * float(value1)
                self.label_output.config(text=f'The area of the square is {square_p}')
            except ValueError:
                self.label_output.config(text='Please type in a number')

        elif shape == 5:
            value1 = self.entry_value1.get()
            value2 = self.entry_value2.get()
            value3 = self.entry_value3.get()
            try:
                triangle_p = float(value1) + float(value2) + float(value3)
                self.label_output.config(text=f'The perimeter of the triangle is {triangle_p}')
            except ValueError:
                self.label_output.config(text='Please type in a number')

    def circle(self):
        """
        This functions makes it so that input only involving the circle appears

        """
        self.label_value1.config(text="Radius")
        self.label_output.config(text='The area or perimeter is')
        self.label_value2.pack_forget()
        self.entry_value2.pack_forget()
        self.label_value3.pack_forget()
        self.entry_value3.pack_forget()
        self.label_area_perimeter.pack()
        self.label_values.pack()
        self.label_value1.pack()
        self.entry_value1.pack()
        self.button_area.pack()
        self.button_perimeter.pack()
        self.label_area_perimeter.pack()
        self.label_output.pack()
        self.button_calculate_area.pack_forget()
        self.button_calculate_perimeter.pack_forget()

    def rectangle(self):
        """

        This functions makes it so that input only involving the rectangle appears
        """
        self.label_value1.config(text="length")
        self.label_value2.config(text="width")
        self.label_output.config(text='The area or perimeter is')
        self.label_value3.pack_forget()
        self.entry_value3.pack_forget()
        self.label_area_perimeter.pack()
        self.label_values.pack()
        self.label_value1.pack()
        self.entry_value1.pack()
        self.label_value2.pack()
        self.entry_value2.pack()
        self.button_area.pack()
        self.button_perimeter.pack()
        self.label_area_perimeter.pack()
        self.label_output.pack()
        self.button_calculate_area.pack_forget()
        self.button_calculate_perimeter.pack_forget()

    def square(self):
        """

        This functions makes it so that input only involving the square appears
        """
        self.label_value1.config(text="side")
        self.label_output.config(text='The area or perimeter is')
        self.label_value2.pack_forget()
        self.entry_value2.pack_forget()
        self.label_value3.pack_forget()
        self.entry_value3.pack_forget()
        self.label_area_perimeter.pack()
        self.label_values.pack()
        self.label_value1.pack()
        self.entry_value1.pack()
        self.button_area.pack()
        self.button_perimeter.pack()
        self.label_area_perimeter.pack()
        self.label_output.pack()
        self.button_calculate_area.pack_forget()
        self.button_calculate_perimeter.pack_forget()

    def triangle_area(self):
        """

        This functions makes it so that input only involving the triangle area appears
        """
        self.label_value1.config(text="base")
        self.label_value2.config(text="height")
        self.label_output.config(text='The area is')
        self.label_area_perimeter.pack()
        self.label_values.pack()
        self.label_value1.pack()
        self.entry_value1.pack()
        self.label_value2.pack()
        self.entry_value2.pack()
        self.label_output.pack()
        self.label_value3.pack_forget()
        self.entry_value3.pack_forget()
        self.button_area.pack_forget()
        self.button_perimeter.pack_forget()
        self.label_area_perimeter.pack_forget()
        self.button_calculate_area.pack()
        self.button_calculate_perimeter.pack_forget()


    def triangle_perimeter(self):
        """

        This functions makes it so that input only involving the triangle perimeter appears
        """
        self.label_value1.config(text="Side 1")
        self.label_value2.config(text="Side 2")
        self.label_value3.config(text="Side 3")
        self.label_output.config(text='The perimeter is')
        self.label_area_perimeter.pack()
        self.label_values.pack()
        self.label_value1.pack()
        self.entry_value1.pack()
        self.label_value2.pack()
        self.entry_value2.pack()
        self.label_value3.pack()
        self.entry_value3.pack()
        self.label_output.pack()
        self.button_area.pack_forget()
        self.button_perimeter.pack_forget()
        self.label_area_perimeter.pack_forget()
        self.button_calculate_perimeter.pack()
        self.button_calculate_area.pack_forget()