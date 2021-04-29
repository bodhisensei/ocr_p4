from controllers.control_chess import Control_menu


def start():
    """Lancement du programme
    """
    start_control = Control_menu()
    start_control.control_choice()


if __name__ == '__main__':
    start()
