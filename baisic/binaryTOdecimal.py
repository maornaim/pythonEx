str = (1,0,1,0,1,1,0,1)
decimal = 0
x = 1
r = 0
for i in str[::-1]:
    r = x*i
    decimal += r
    x = x*2

print(decimal)
