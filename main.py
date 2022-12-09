from gui import *


def main():
    window = Tk()
    window.title('Contest Entry Form')
    window.resizable(False, False)
    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
