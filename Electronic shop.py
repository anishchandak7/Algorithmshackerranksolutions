b,n,m = input().split(" ")
b = int(b)  # Amount of money monica had.
n = int(n)  # No. of keyboards
m = int(m)  # No. of USBs.

# Keyboards cost:
keyboard = list(map(int,input().split(" ",n)))
usb = list(map(int,input().split(" ",m)))
maxamt=-1
for pos1 in range(len(keyboard)):
    i = 0
    while(i < len(usb)):
        sum1 = keyboard[pos1]+usb[i]
        if(sum1>b):
            pass
        else:
            maxamt = sum1
        i+=1
if maxamt==-1:
    print(-1)
else:
    print(maxamt)




