import numpy as np

def initializing():
    a = np.array([1,2,3])
    b = np.array([(1,2), (3,4)], dtype=float)
    c = np.array([[(1,2), (3,4)], [(5,6), (7,8)]], dtype=float)

    d = np.zeros((3,4))
    print("d:\n", d)
    e = np.ones((2, 3, 4), dtype=np.int16)
    print("e:\n", e)
    f = np.arange(15, 25, 5)
    print("f:\n", f)
    g = np.full((2,2), 7, dtype=np.int16)
    print("g:\n", g)
    h = np.eye(2)
    print("h:\n", h)
    i = np.random.random((2,2))
    print("i:\n", i)
    g = np.empty((2,2))
    print("g:\n", g)

def IO():
    a = np.array([1,2,3])
    b = np.array([(1,2), (3,4)], dtype=float)
    np.save('my_array', a)
    np.savez('array.npz', a=a, b=b)
    res = np.load('array.npz')
    for x in res.items():
        print(x)
    data = np.loadtxt("text")
    print("data:\n", data)
    # np.genfromtxt("my_file.csv", delimiter=",")
    np.savetxt("my_array.txt", a, delimiter=",")

def InspectArray():
    c = np.array([[(1,2), (3,4)], [(5,6), (7,8)]], dtype=float)
    print("c shape:", c.shape)
    print("c dim:", c.ndim)
    print("c length:", len(c))
    print("c size:", c.size)
    print("c dtype:", c.dtype)
    print("c dtype name:", c.dtype.name)
    print("c convert to float", c.astype(np.float32))

def ArrayMath():
    a = np.array([1,2,3])
    b = [3,4,5]
    c = 1
    d = a - b
    e = a - np.array([2,3,4])
    f = a - c
    a = [[1,2,3], [2,3,4]]
    b = [[4,5], [0,0],[1,1]]
    c = np.dot(a, b)
    d = np.matmul(a,b)
    print(c)
    print(d)
    e = [1,-1,1]
    c = np.dot(a, e)
    d = np.matmul(a,e)
    print(c)
    print(d)
    res = a == b
    print("res:", res)
    res = [1,2,3] == [1,2,3]
    # a can be np.array, b can be python list
    res = np.array_equal(a, [1,23])
    a = [[111,22,3], [12,3,4]]
    r = np.array(a)
    r.sort(axis=0)
    print(r)

    
initializing()
IO()
InspectArray()
ArrayMath()