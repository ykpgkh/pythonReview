from collections import deque
letters = []

# 'push' some letters into the list by using .append
letters.append('a')
letters.append('b')
letters.append('c')
letters.append('d')

print('1')
print(letters)

lastItem = letters.pop()
print('2')
print('the following letter got popped: ', lastItem)
print(letters)

# you can write in an index inside of pop() to get a queue like behavior
lastItem = letters.pop(0)
print('3')
print('the following letter got popped: ', lastItem)
print(letters)

# initialize the dequeue for queues
numbers = deque()

# append some numbers to the queue using append
numbers.append(99)
numbers.append(98)
numbers.append(97)
numbers.append(96)
numbers.append(95)

# pop it like a stack
lastItem2 = numbers.pop()
print('example1')
print(lastItem2)
print(numbers)


# dequeue like a queue
firstItem = numbers.popleft()
print('example2')
print(firstItem)
print(numbers)
