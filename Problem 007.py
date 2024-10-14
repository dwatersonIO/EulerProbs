from sympy import *
import time

begin = time.time()
print (begin)

print (prime(10001))

end = time.time()
print (end)
print ("Time taken: ", begin-end)