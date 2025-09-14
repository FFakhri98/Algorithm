t = int(input())
for i in range(t):
    n = int(input())
    ans = 0
    a = 1
    while a * a < n:
        if n % a == 0 and (a + (n / a)) % 2 == 0:
            ans += 1
        a += 1
    print(ans)
