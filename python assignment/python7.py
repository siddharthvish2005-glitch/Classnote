amount = int(input("Enter the value of amount : "))

notes100 = notes50= notes20 = notes10 = notes5 = notes2 = notes100 = 0

match 100:
    case 100:
        notes100 = amount // 100 
        amount = amount%100
        if notes100 > 0:
         print("TOTAL NO OF 100 NOTES : ",notes100)


match 50:
    case 50:
        notes50 = amount // 50 
        amount = amount%50
        if notes50 > 0:
          print("TOTAL NO OF 50 NOTES : ",notes50)


match 20:
    case 20:
        notes20 = amount // 20 
        amount = amount%20
        if notes20 > 0:
           print("TOTAL NO OF 20 NOTES : ",notes20)


match 10:
    case 10:
        notes10 = amount // 10 
        amount = amount%10
        if notes10 > 0: 
           print("TOTAL NO OF 10 NOTES : ",notes10)

match 5:
    case 5:
        notes5 = amount//5 
        amount = amount%5
        if notes5 > 0: 
           print("TOTAL NO OF 5 NOTES : ",notes5)


match 2:
    case 2:
        notes2 = amount//2 
        amount = amount%2
        if notes2 > 0:
           print("TOTAL NO OF 2 NOTES : ",notes2)


match 1:
    case 1:
        notes1 = amount//1  
        amount = amount%1
        if notes1 > 0:
           print("TOTAL NO OF 1 NOTES : ",notes1)