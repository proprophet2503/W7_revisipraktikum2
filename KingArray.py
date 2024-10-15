t = int(input())
arrJumlah = []

for i in range(t):
   
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    q = int(input())
    
    jumlah_skrg = sum(A[:k])

    jumlah_max = jumlah_skrg
    jumlah_min = jumlah_skrg
    # Sliding window 

    for i in range(1, k+1):
        jumlah_skrg = sum(A[:i])
        jumlah_max = max(jumlah_max, jumlah_skrg)
        jumlah_min = min(jumlah_min, jumlah_skrg)
        for j in range (1, n - i + 1):
            jumlah_skrg = jumlah_skrg - A[j - 1] + A[j + i - 1]
            jumlah_max = max(jumlah_max, jumlah_skrg)
            jumlah_min = min (jumlah_min, jumlah_skrg)
    
    if (q == 1):
        arrJumlah.append(jumlah_max)
    elif ( q == 2):
        arrJumlah.append(jumlah_min)

for a in arrJumlah:
    print(a)