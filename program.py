def convert_to_binary(n):
	i = 1
	while 2 ** i <= n:
		i += 1
	i -= 1
	new_string = ''
	while i >= 0:
		divide_by = 2 ** i
		if n / divide_by == 1:
			n = n % divide_by
			new_string += '1'
		else:
			new_string +='0'
		i -= 1
	return new_string

palindrome_numbers = 0
j = 1
while j < 1000000:
	if str(j) == str(j)[::-1] and convert_to_binary(j) == convert_to_binary(j)[::-1]:
		print(j)
		palindrome_numbers += j

	j += 1
print(palindrome_numbers)
