def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
      return 1.0
    elif base == 0:
      return 0.0
    else:
        result = 1.0
        for i in range (abs(exp)):
            result *= base
        return result
        
        
print(iterPower(-4.76, 4))