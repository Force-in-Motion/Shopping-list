import sys

class Templates:

    @staticmethod
    def checks_presence_element(data, matrix):
        for elem in matrix:
            if data in elem: return True
        return False

    @staticmethod
    def on_closing() -> None:
        """
        Выход из приложения при закрытии главного окна
        """
        sys.exit()