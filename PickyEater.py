Freq = [0]*11
N = int(input())
Buah = list(map(int,input().split()))
maxi = 0

for i in Buah:
    Freq[i]+=1
    
maxi = max(Freq)
print(maxi)
for i in range(len(Freq)):
    if(Freq[i] > max):
        max = Freq[i]

Freq_Tot = Freq.count(max)
if Freq_Tot == 1:
    print(Freq.index(max))
    print(N-max)
else:
    print("-1")
