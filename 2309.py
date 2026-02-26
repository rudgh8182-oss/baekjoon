tall = [int(input()) for _ in range(9)]
lst = []
a = False
for i in range(8):
    if a:
        break
    for j in range(i+1, 9):
        lst = tall[:]
        lst.pop(i)
        lst.pop(j-1)
        if sum(lst) == 100:
            a = True
            break

lst.sort()
for k in lst:
    print(k)
