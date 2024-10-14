'''
Problem 8
'''

my_string = ("73167176531330624919225119674426574742355349194934"
"9698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511"
"1254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113"
"6222989342338030813533627661428280644448664523874930358907296290491560440772390713810515859307960866"
"7017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243"
"5258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482"
"8397224137565705605749026140797296865241453510047482166370484403199890008895243450658541227588666881"
"1642717147992444292823086346567481391912316282458617866458359124566529476545682848912883142607690042"
"2421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188"
"8458015616609791913387549920052406368991256071760605886116467109405077541002256983155200055935729725"
"71636269561882670428252483600823257530420752963450")

# my_string = "123456789"

num_list = []

# Need to convert string to list of integers
for a in my_string:
    num_list.append(int(a))
print (num_list)
        
def calc_segment_product(my_list):
    result = 1
    for a in my_list:
        result=result*a
    return result
        
highest_so_far = 0
starting = 0
span = 13 
length = len(num_list)
last_start = length - span
while starting  <= last_start: 
    finish = starting + span
    segment = num_list[starting:finish]
    segment_product = calc_segment_product(segment)
    if segment_product > highest_so_far:
        highest_so_far=segment_product
    starting = starting +1


print (highest_so_far)
print ("Ended")
