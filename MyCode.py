#without anonymous
def square(a):
    return a * a

result = square(5)
print(result)



# with anonymous
f = lambda a,b: a + b

result = f(5,6)
print(result)