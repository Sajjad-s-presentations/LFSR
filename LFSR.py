import random

class LFSR():
    def __init__(self, degree, taps):
        print("Initializing LFSR {} degree".format(degree))
        cur = random.randrange(0, degree, 3)
        self.register = ([0]*cur) + ([1]*(degree-cur))
        random.shuffle(self.register)
        self.taps = taps


    def setRegister(self, register):
        self.register = register

    def getRegister(self):
        return self.register

    def getTaps(self):
        return self.taps

    def shift(self, input_list):
        cuurr_list = [[input_list[i - j] for i in range(len(input_list))] for j in range(len(input_list))]
        return cuurr_list[1]

    def successor(self):
        tap_list = self.taps
        tap_list.reverse()
        tap_elements = []
        for tl in tap_list:
            tap_elements.append(self.register[tl])

        print(tap_elements)
