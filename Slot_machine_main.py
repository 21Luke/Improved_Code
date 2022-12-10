from gui2 import *

def main()-> None:
    """
    function to initialize the program

    """

    window = Tk()
    window.title('Slot Machine')
    window.geometry('400x300')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
