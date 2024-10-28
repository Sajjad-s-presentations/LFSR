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

        new_reg = self.shift(self.register)
        print(new_reg)
        first_index = new_reg[0]
        for tl in tap_list:
            first_index = first_index ^ self.register[tl]

        new_reg[0] = first_index

        return new_reg



        print(tap_elements)
