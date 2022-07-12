a=[1,2,3,4,5,6,7]
print(type(a))
print(a[3])
print(a[-4])
print(a[1:4])
print(a[:4])
print(a[3:])
print(a[-2:2])
print(a[2:-3])
print(a[1:6:2])
#changing elements in a list
b=[12,23,45,67,42,87,97]
b[1]=50
print(b)
b[2:5]=[80,90,100]
print(b)
#adding elements in a list
b.append(20)
print(b)

b.extend([78,90,88])
print(b)

c=a+b
print(c)

b.insert(2,3)
print(b)

#deleting elements in alist
del b[3]
print(b)
del b[2:6]
print(b)

b.remove(90)
print(b)

print(b.remove(97))

d=[20,40]

d1=d*3
print(d1)
#python list operators
print(50 in b)

# mylist=[]
# for i in range(5):
#     print("enter value of n[",i,"}")
#     mylist.append(input())
# print(mylist)

namess=list(range(1,11))
print(namess)
list1=[1,2,3,4]
list2=list1.copy()
list2[3]=60
print(list1)
print(list2)

print(len(list1))
print(max(b))
print(min(c))
print(sum(c))
print(sorted(c))
print(c.reverse())
print(c.index(87))
print(b.count(1))

#PYTHON LIST COMPREHENSION.
cubes=[]
for i in range(1,10):
    cubes.append(i**3)
print(cubes)

square=[]
for i in range(1,10):
    square.append(i**2)
print(square)

cube=[i**4 for i in range(1,11)]
print(cubes)

mylist=[i for i in range(1,6)]
print(mylist)

even=[num%2==0 for num in range(1,11)]
print(even)

even1=[num for num in range(1,20) if num%2==0]
print(even1)

result=[num**2 if num%2==0 else num**3 for num in range(1,11)]
print(result)

lis1=[1,2,3,4]
lis2=[1,20,30,4]
resul=[]

for x in lis1:
    for y in lis2:
        if x==y:
            resul.append(y)
print(resul)

li1=[1,2,3,4,5]
li2=[23,2,37,48,4,34,5]
resu=[]
for x in li1:
    for y in li2:
        if x==y:
            resu.append(y)
print(resu)

results=[y for x in li1 for y in li2 if x==y]
print(results)