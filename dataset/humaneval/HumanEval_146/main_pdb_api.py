from typing import *	##line:(1)
def specialFilter(nums):	##line:(2)
    	##line:(3)
    count = 0	##line:(4)
    for num in nums:	##line:(5)
        if num > 10:	##line:(6)
            odd_digits = (1, 3, 5, 7, 9)	##line:(7)
            number_as_string = str(num)	##line:(8)
            if int(number_as_string[0]) in odd_digits and int(number_as_string[-1]) in odd_digits:	##line:(9)
                count += 1	##line:(10)
        	##line:(11)
    return count 	##line:(12)

specialFilter([5, -2, 1, -5]) 