'''
when set includes alphabet letter, then order won't be same every time running program, however, when set has all number
the order seems to be same every time.
Also difference between python2 and python3. Python2 will print same order all the time, python3 won't for letter cases.
'''
a = set(range(5))
print("print out set", a)
b = {1: set(range(5))}
print("print out dictionary value", b[1])
c = set(range(3, 7))
for id in range(1):
    print(id, " print out a - c ", a - c)
    print(id, " print out b[1] - c ", b[1] - c)

for id in range(5):

    d = set(['a', 'b', 'c', 'd', 'e'])
    print("d:", d)

    a = set(range(5))
    print("print out set", a)

    e = set([1,2,3,4,5])
    print("e ", e)