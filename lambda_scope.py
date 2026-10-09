#lambda.py
kuadrat = lambda x: x ** 2
print(kuadrat(4))               #16

siswa = [("ani", 80), ("budi", 95)]
print(max(siswa, key=lambda s: s[1]))

#scope.py
x = "global"
def tes():
    x = "local"     #hanya di dalam tes()
    print(x)        #lokal
tes()
print(x)            #global