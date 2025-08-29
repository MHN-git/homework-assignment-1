class text_printer:
    def __init__(self, mode):
        self.mode = mode 
        self.text = input('enter your sentence: ')
    
    def set_mode(self, mode):
        self.mode = mode
        
    def print_text(self):
        self.mode.write(self.text)


class normalPrint():
    def write(self, text):
        print(text)


class reversePrint():
    def write(self, text):
        words = text.split()
        for word in reversed(words):
           print(word, end = " ")
        print()


if __name__ == "__main__":
    
    printer = text_printer(reversePrint())
    printer.print_text()
    printer.set_mode(normalPrint()) 
    printer.print_text()

 
