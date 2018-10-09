
# list iterator can change
a = [1,2,3,4]
for x in a:
	print(a.pop())


# set iterator cannot change
b = {1,2,3,4}
for x in b:
	b.pop()
