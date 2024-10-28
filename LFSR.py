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

    def successor(self, input_list):
        tap_list = self.taps
        tap_list.reverse()

        new_reg = self.shift(input_list)
        first_index = new_reg[0]
        for tl in tap_list:
            first_index = first_index ^ input_list[tl]

        new_reg[0] = first_index

        return new_reg

    def decrypt(self, input_list):
        rare = input_list[0]
        new_list = input_list[1:]

        tap_list = self.taps
        tap_list.reverse()

        for tl in tap_list:
            rare ^= new_list[tl-1]

        new_list.append(rare)

        return new_list

    def lfsr(self):
        cur_list = self.register
        new_list = cur_list

        while True:
            print(new_list)
            new_list = self.successor(new_list)

            if new_list == cur_list:
                break

