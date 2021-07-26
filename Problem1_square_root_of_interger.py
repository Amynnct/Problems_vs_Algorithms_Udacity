import math
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print("Invalid input. This function only supports numbers that greater than or equal to 0.")
        return None
    
    if number == 0:
        return 0
    
    divisor = number/2
    result = number/divisor
    while (abs(result-divisor) > 0.00001):
        divisor = (divisor + result)/2
        result = number/divisor
    return math.floor(divisor)

print ("Pass" if  (3 == sqrt(9)) else "Fail") #Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail") #Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail") #Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail") #Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail") #Pass
print ("Pass" if  (7 == sqrt(49)) else "Fail") #Pass

#Edge cases
print("Pass" if (None == sqrt(-22)) else "Fail") 
# Invalid input. This function only supports numbers that greater than or equal to 0.
# Pass
print("Pass" if (3162 == sqrt(9999999)) else "Fail") #Pass
