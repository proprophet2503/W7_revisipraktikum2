N = int(input())
id_buah = list(map(int, input().split()))

counter = [0]*11

for buah in id_buah:
    counter[buah]+=1

terbanyak = 0

for jumlah_buah in counter:
    if(jumlah_buah > terbanyak):
        terbanyak = jumlah_buah

buah_terbanyak = []
selisih = 0
for i in range(len(counter)):
    if(counter[i] == terbanyak):
        buah_terbanyak.append(i)
        selisih = len(id_buah)-counter[i]


if(len(buah_terbanyak)==1):
    print(buah_terbanyak[0])
    print(selisih)
else:
    print(-1)
    
     


