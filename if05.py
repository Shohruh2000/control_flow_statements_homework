def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    x1 = int(a)
    x2 = int(b) 
    x3 = int(c)
    if x1>0 and x2>0 and x3>0:
        return 0
    if x1>0 and x2>0 and x3<0:
        return 1
    if x1>0 and x3>0 and x2<0:
        return 1
    if x3>0 and x2>0 and x1<0:
        return 1
    if x1>0 and x2<0 and x3<0:
        return 2
    if x1<0 and x2>0 and x3<0:
        return 2
    if x1<0 and x2<0 and x3>0:
        return 2
    if x1<0 and x2<0 and x3<0:
        return 3

print(main(2,-4,-8))