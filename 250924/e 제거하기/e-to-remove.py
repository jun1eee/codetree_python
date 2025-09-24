s = input()
arr = list(s)
arr.pop(s.find('e'))
print(''.join(arr))