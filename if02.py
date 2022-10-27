def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else decreased by 2.
    """
    a = int(a)
    if a>0 :
        return a+1
    if a<0 :
        return a-2
print(main(5.6))