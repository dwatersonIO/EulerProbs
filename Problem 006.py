
squares =[]

# Create a list in a range of 10-20 
My_list = [*range(1, 101)] 
 
for a in My_list:
    b=a*a
    squares.append(b)

sum_my_list = sum(My_list)
sq_sum_my_list = sum_my_list * sum_my_list
print (My_list)
print (squares)

print ("Square of sum of my list is:", sq_sum_my_list)
print ("Sum of squres is:", sum(squares))
print ("Solution to problem is: Sum of squres is:", sq_sum_my_list-sum(squares))


