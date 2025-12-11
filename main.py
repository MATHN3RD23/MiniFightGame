from logic import *

def main():
    """
    runs gui
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()