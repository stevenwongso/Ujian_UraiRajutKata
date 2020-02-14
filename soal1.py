class uraiRajutKata:
    def urai(self,x) :
        hasil = ''
        for i in range (len(x)+1):
            for j in range(i) :
                hasil += x[j]
        return hasil
    def rajut(self,y) :
        templist= [1]
        awal = 1
        for i in range(2, len(y)):
            awal = awal + i
            templist.append(awal)
        return y[len(y)-(templist.index(len(y))+1):]
       

x = uraiRajutKata()
print(x.urai('Code'))
print(x.urai('Python'))
print(x.urai('Purwhadika'))

print(x.rajut('CCoCodCode'))
print(x.rajut('PPyPytPythPythoPython'))
print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))