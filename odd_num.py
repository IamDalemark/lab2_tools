odd = [1,3,5,7]

odd = odd.clear()
print(odd)

def odd(num):
    return [odd for odd in num if odd % 2 == 0]
print(odd([2,3,4,5,6]))

