range(9
number=int(input("몇 단을 출력할래요?"))
i=number
for i in range(1,10):
    print("%d단 = " %i,end="")

    for j in range(1,10):
        print([i*j],end='')
       
    if j == 9 :
        print("\n")
