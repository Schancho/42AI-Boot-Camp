import sys

word = ''
n = len(sys.argv)
if n == 1:
    print("Usage: Please enter at least one argument!")
    exit()
for i in range(1, n):
    word += sys.argv[i] + ' '
word = word.rstrip(word[-1])
word = word.swapcase()
word = word[::-1]
print(word)