'''
Use the grid hear to visualize the checks needed in the two
lists used n_list and m_list
https://blog.dreamshire.com/generating-pythagorean-triples/
'''

import time

def is_triplet(a,b,c):
    if (a*a)+(b*b)==(c*c):
        return True
    else:
        return False

def sum_correct(a,b,c):
    if a + b + c == 1000:
        return True
    else:
        return False

def find_triplet_solution():
    n_list=list(range(1, 1000, 1))
    for n in n_list:
        start_m=n+1
        m_list=list(range(start_m, 1001, 2))
        for m in m_list:
            a=(m*m)-(n*n)
            b=2 * m * n
            c=(m*m) + (n*n)
    #       print (f" n={n} m={m} and abc are: {a}-{b}-{c}")
            if is_triplet(a,b,c):
                if sum_correct(a,b,c):
                    print (f"This is the solution: {a} - {b} - {c}")
                    print (f"Product is: {a*b*c}")
                    break
        start_m = start_m + 2

begin = time.time()
find_triplet_solution()
end = time.time()
print (f"This took: {end-begin}")

begin = time.time()
for a in range(1,1000):
    for b in range(1,a):
        if (a**2 + b**2)**0.5 == 1000-a-b:
            print(f'{a*b*(1000-a-b)}')
end = time.time()
print (f"This took: {end-begin}")

