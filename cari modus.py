N = int(input())
data_harga = list(map(int, input().split()))

counter = [0]*11

for harga in data_harga:
    counter[harga]+=1

modus_harga = 0

for jumlah_harga in counter:
    if(jumlah_harga > modus_harga):
        modus_harga = jumlah_harga

harga_terbanyak = []
for i in range(len(counter)):
    if(counter[i] == modus_harga):
        harga_terbanyak.append(i)
        
modus_tergede = 0
for i in range(len(harga_terbanyak)):
    if(harga_terbanyak[i]>modus_tergede):
        modus_tergede = harga_terbanyak[i]

print("Modus: ", modus_tergede)

if modus_tergede <= 1:
    print("Yah, modusnya gak prima.")
else:
    cek_prima = True
    for i in range(2, (modus_tergede ** 0.5) + 1):
        if modus_tergede % i == 0:
            cek_prima = False
            break
    if cek_prima:
        print("Prima")
    else:
        print("Bukan Prima")
