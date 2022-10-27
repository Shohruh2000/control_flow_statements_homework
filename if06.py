def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    x1 = int(a)
    x2 = int(b) 
    x3 = int(c)

    if x1>0 and x2>0 and x3>0:
        return "there are a lot of positive numbers"
    if x1>0 and x2>0 and x3<0:
        return "there are a lot of positive numbers"
    if x1>0 and x3>0 and x2<0:
        return "there are a lot of positive numbers"
    if x3>0 and x2>0 and x1<0:
        return "there are a lot of positive numbers"
    if x1>0 and x2<0 and x3<0:
        return "there are a lot of negative numbers"
    if x1<0 and x2>0 and x3<0:
        return "there are a lot of negative numbers"
    if x1<0 and x2<0 and x3>0:
        return "there are a lot of negative numbers"
    if x1<0 and x2<0 and x3<0:
        return "there are a lot of negative numbers"
    