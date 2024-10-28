import random

class LFSR():
    def __init__(self, degree):
        print("Initializing LFSR {} degree".format(degree))
        cur = random.randrange(0, degree, 3)
        self.register = ([0]*cur) + ([1]*(degree-cur))
        random.shuffle(self.register)

    def getRegister(self):
        return self.register
