print('goog morning mercy')
colors=['blue','red','yellow','purple']
for color in colors:
    print(color)

marks=[80,90,77,89,93]
sum=0
for mark in marks:
    sum+=mark
print(sum)
#PYHTON RANGES.
for n in range(1,10,3):
    print(n)
#BREAK AND CONTINUE
for n in marks:
    print(n)
    if n==77:
        break

n=1
while n<10:
    print(n)
    if n==2:
        break
    n+=1

while True:
    x=int(input('Enter 0 to stop:'))
    if x==0:
        break

#continue
for n in range(1,10):
    if n==1:
        continue
    print(n)
