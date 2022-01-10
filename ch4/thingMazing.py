chars = ['t', 'a', 'c', 'o']

output = ''
length = len(chars)
i = 0
while i < length:
	output = output + chars[i]
	i = i + 1

length = length * -1

i = - 2

while i >= length:
	output = output + chars[i]
	i = i - 1

print(output)
