class TTT():
    """
    Text To Text
    """

    def __init__(self):
        pass

    def get_input(self):
        text = input('>> ').lower()
        while text == '':
            text = input('>> ').lower()
        return text

