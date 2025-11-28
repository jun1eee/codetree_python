n = int(input())
cnt = 0
for i in range(2, round(n**0.5)+1):
    if (n%i)==0:
        cnt += 1;
if (cnt==0 or n==2):
    print("P")
else:
    print("C")