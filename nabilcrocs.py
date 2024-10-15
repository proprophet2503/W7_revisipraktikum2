N = int(input())
B = list(map(int, input().split()))

hasil = 1
for i in range(N):
    for j in range(i+1, N):
        perkalian_xor = B[i]^B[j]
        hasil*= perkalian_xor
        
print(hasil)
