a = int(input())
print("number of attempt left 8")
count = 0
while(a!=18 and count<8):
 a = int(input())
 count = count+1
 print("numbers of attempt left",8-count)
 continue
if(a==18):
    print("success")
    print("number of attempts took")
    print(count+1)
else:
    print("game over")


