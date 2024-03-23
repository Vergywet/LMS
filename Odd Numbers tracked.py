#Normal Comprehensive Odd Numbers
codes = [14,15,16,17,18,19,20]

oddNum = []
for odd in codes:
    if odd%2 !=0:
        oddNum.append(odd)
        print("Odd Numbers : ",oddNum)

#List Comprehensive Odd numbers 
listOdd = [o for o in codes if o%2 != 0 ]
print("List_odd : ",listOdd)
