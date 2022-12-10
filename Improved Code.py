from gui import *


def main() -> None:
    """
        function to initialize the program

        """

    window = Tk()
    window.title('Area and Perimeter Calculator')
    window.geometry('450x400')
    window.resizable(False, False)
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()