import sys
import string

lst = []
def filterwords(s, n):
    s = s.split()
    for word in s:
        if len(word) - word.count('.') - word.count(',') - word.count('!') - word.count('?') - word.count(':') - word.count(';') > n:
            lst.append(word)
    print(lst)

if __name__ == "__main__":
    if len(sys.argv) == 3  and sys.argv[2].isdigit():
        filterwords(sys.argv[1], int(sys.argv[2]))
    else:
        print("ERROR")

