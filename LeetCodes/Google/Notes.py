"""
Python closure, 'a' in below as to be a reference type of variable, otherwise, error as "reference before assignment"
shows up.
"""
def fun():
    '''
    a is good here
    :return:
    '''
    a = [4]
    def funny():
        a[0] = 2
        print(a)
    funny()
    print(a)
fun()

def fun():
    '''
    a is good here
    :return:
    '''
    a = [4]
    def funny():
        a[0] += 2
        print(a)
    funny()
    print(a)
fun()

def fun():
    '''
    a cannot be referenced
    :return:
    '''
    a = 4
    def funny():
        print(a)
        a += 2
        # print(a)
    funny()
    print(a)
fun()

