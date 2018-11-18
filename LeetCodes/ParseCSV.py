input = 'a, "b, x,""", d'

res = []
for x in input.split('\n'):
	x = x + ','
	elem = ""
	row = []
	inQuotes = False
	for ch in x:
		if ch not in ',"':
			elem += ch
		elif ch == '"':
			inQuotes = not inQuotes
		elif ch == ',':
			if inQuotes:
				elem += ch
			else:
				row.append(elem)
				elem = ""
	res.append(row)
	# print(elem + "\n")

print(res)