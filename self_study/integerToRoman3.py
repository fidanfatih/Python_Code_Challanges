num = int(input("Enter a n(1-3999): "))
ones =['','I','II','III','IV','V','VI','VII','VIII','IX']
tens =['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
hundreds =['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
thousands = ['','M','MM','MMM']
result = thousands [ num // 1000 ] +\
         hundreds [ num % 1000 // 100 ] +\
         tens [ num % 100 // 10 ] +\
         ones [ num % 10 ]
# uzun satırlarda aritmetik operatörden önce veya sonra entera basarak (otomatik "/" işareti koyar)kodun devamını altsatırdan devam ettirebilirsiniz..
print(result)
