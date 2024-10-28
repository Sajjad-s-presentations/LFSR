from LFSR import LFSR

lfsr = LFSR(10, [0, 3, 9])
print(lfsr.getRegister())
print(lfsr.getTaps())
lfsr.successor()
print(lfsr.shift([1,2,3,4]))