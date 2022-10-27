def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2.
    Args:
        a: integer
    Returns:
        a: a increased by 1 if positive, else decreased by 2.
    """
    s = int(a)

    if s>0 :
        return s+1
    else:
        return s-2
print(main(6))