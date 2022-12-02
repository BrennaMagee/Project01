from gui import *


def main():
    window = Tk()
    window.title('Lab 10')
    window.geometry('250x180')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
