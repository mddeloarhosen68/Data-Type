#without lambda

def is_even(n):
    return n % 2 == 0
nums = [2,5,8,9,3,6,7,11,14]
evens = list (filter(is_even,nums))
print(evens)


#with lambda

nums = [2,5,8,9,3,6,7,11,14]
evens = list (filter(lambda n: n % 2 == 0,nums))
print(evens)