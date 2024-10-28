from LFSR import LFSR

lfsr = LFSR(5, [0, 3])
print(lfsr.getRegister())
#lfsr.lfsr()

print(lfsr.successor([1,0,1,0,0]))
print(lfsr.decrypt([1, 1, 0, 1, 0]))
