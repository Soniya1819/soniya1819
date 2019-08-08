cn=input('enter customer name:')
units=eval(input('enter no of units consumed:'))
dc=20
if units>500:
    charge=3000+dc
elif units>100 and units<=200:
    charge=500+dc
elif units>200 and units<=300:
    charge=650+dc
elif units>300 and units<=500:
    charge=800+dc
else:
    charge=0+dc
print('customer name=',cn)
print('units consumed=',units)
print('charges=',charge)
