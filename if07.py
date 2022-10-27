def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    s = int(a)
    if s>0 and s%2==1 :
        return "positive odd number"
    if s>0 and s%2==0 :
        return "positive even number"
    if s<0 and s%2==1 :
        return "negativ odd number"
    if s<0 and s%2==0 :
        return "negative even number"
    if s==0:
        return "the number is zero"

print(main(0))