'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


# def is_even(n): 
#     if n % 2 == 0:
#         return True
#     return False

# def get_next_num(n):
#     if is_even(n):
#         next_num = number / 2        
#     else:
#         next_num = (number * 3) + 1
#     return next_num

# record = {}

# for number in range(10,999999):
#     chain = []
#     starting_num=number
#     while True:
#         chain.append(number)
#         if number == 1:
#             break
#         next_num = get_next_num(number)
#         number=next_num
#     record[starting_num]=len(chain)

# max_key = max(record, key=record.get)
# print (max_key)

collatz = dict()

collatz[1] = 1

def sequence(col, num):
    if num in col:
        return col[num]
    elif num % 2 == 0:
        return 1 + sequence(col,num//2)
    else:
        return 1 + sequence(col,num*3+1)

largest = [1,1]

for i in range(1,999999):
    seq = sequence(collatz,i)
    if seq > largest[1]:
        largest[1] = seq
        largest[0] = i
    collatz[i] = seq
    # print(largest)
print(largest)


