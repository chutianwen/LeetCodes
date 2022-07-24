
# list iterator can change
a = [1,2,3,4]
for x in a:
	print(a.pop())

print("*"*100)
# we can append to the iterator like this. -x, "," is important
for x in a:
	print(x)
	if x > 0:
		a += -x,


# set iterator cannot change
b = {1,2,3,4}
for x in b:
	b.pop()
