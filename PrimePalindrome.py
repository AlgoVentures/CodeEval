
def is_palindrome(x):
    y = int(str(x)[::-1])
    return x == y
        
def is_prime(x):
    return x > 1 and all(x % i for i in xrange(2, x))
    
for i in range(1000,-1,-1):
    if is_palindrome(i) and is_prime(i):
        print i
        break
