from collections import defaultdict


print("hello mercy")
# def multiplication_table():
#     pairs=zip(n1,n2)
#     for idx,pair in enumerate(pairs):
#         n,m=pair
#         print('{}^{}={}'.format(n,2,m))
# multiplication_table()
def my_Dictionaries():
    z={'a':20,'b':30,'c':50}
    for x in z:
        print(z.items())
my_Dictionaries()
# d = {'a':20, 'b':21, 'c':22, 'd':23}
#  'd' in d:
#     print(d['d'])
# else:
#     print('d')
def multiply_dic():
    d=defaultdict(int)
    for x in range(4):
        d[x]=x**2
        print(d.items())
multiply_dic()
def working_Counters():
    a=[1,2,3,4,56,7,8,9,90]
    for x in a:
        print(Counter(x))