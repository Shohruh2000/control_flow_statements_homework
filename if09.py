def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    s = int(a)
    
    if s >= ((s%10)*10 + s//10):
        return "True"
    if s <= ((s%10)*10 + s//10):
        return "False"

print(main(68))
