# Python

def is_triplet(a,b,c):
    if (a*a)+(b*b)==(c*c):
        return True

def sum_correct(a,b,c):
    if a + b + c == 1000:
        return True

def find_triplet_solution():
    n_list=list(range(1, 1000, 1))
    for n in n_list:
        start_m=n+1
        m_list=list(range(start_m, 1001, 2))
        for m in m_list:
            a=(m*m)-(n*n)
            b=2 * m * n
            c=(m*m) + (n*n)
            if is_triplet(a,b,c):
                if sum_correct(a,b,c):
                    print (f"The solution is: {a*b*c}")
                    break
        start_m = start_m + 2

find_triplet_solution()