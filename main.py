from LFSR import LFSR

lfsr = LFSR(10, [0, 3, 4, 9])
print(lfsr.getRegister())
print(lfsr.getTaps())
print(lfsr.successor(lfsr.getRegister()))
