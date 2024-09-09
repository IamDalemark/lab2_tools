def odd(num):
    return [odd for odd in num if odd % 2 == 0]

print(odd([1,2,3,4,5,6,7,8,10]))