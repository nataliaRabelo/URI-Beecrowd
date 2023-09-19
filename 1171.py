def number_frequence():
    numbers = {}
    amount = int(input())
    for i in range(amount):
    	num = int(input())
    	if num in numbers:
    		numbers[num] += 1
    	else:
    		numbers[num] = 1
    for res in sorted(numbers.keys()):
    	print(f"{res} aparece {numbers.get(res)} vez(es)")

number_frequence()