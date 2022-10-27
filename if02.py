def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else decreased by 2.
    """
    
    if a>0 and int(a):
        return a+1
    if a<0 and int(a):
        return a-2
print(main(-4))