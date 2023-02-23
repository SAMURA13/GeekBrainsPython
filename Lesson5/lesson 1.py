spisok = [1,2,3,3,5,8,15,23,38]
spisok2= list()
for i in spisok:
    if i % 2==0:
        spisok2.append((i,i*i))
        i+=1
        print(spisok2)
print(spisok2)


