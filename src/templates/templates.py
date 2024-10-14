
class Templates:

    @staticmethod
    def checks_presence_element(data, matrix):
        for elem in matrix:
            if data in elem: return True
        return False
