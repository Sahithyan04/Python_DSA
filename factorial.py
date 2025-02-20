# Factorial in python
def fact(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * fact(n-1)
print(fact(3))

'''
    **The Concept**
    base cases :
        n = 0 -> 0
        n = 1 -> 1
    factorials:
        n = 5 -> 5 x factorial(4)
            4 -> 4 x factorial(3)
            3 -> 3 x factorial(2)
            2 -> 2 x factorial(1)
            1 -> 'base case' 1
            
'''