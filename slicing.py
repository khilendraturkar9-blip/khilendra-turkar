numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]#slice
print(numbers[0:5])
print(numbers[5:])
print(numbers[:5])
print(numbers[::2])

# normal way 
numbers = []
for i in range(1,6):
    numbers.append(i)
print(numbers)

# CComprehension way - one line :
numbers = [i for i in range(1,6)]
print(numbers) # [1,2,3,4,5,]
# even nambers
even = [i for i in range(1,11)if i%2==0]
print(even)#[2,4,6,8,10]
# squares
squares = [i*i for i in range(1,6)]
print(squares)#[1,4,9,16,25]