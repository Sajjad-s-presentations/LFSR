from LFSR import LFSR

lfsr = LFSR(4, [2, 3])
lfsr.setRegister([1,0,0,1])
print(lfsr.getRegister())
lfsr.lfsr()

