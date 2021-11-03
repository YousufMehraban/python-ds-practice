def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    repeat1 = {}
    repeat2 = {}
    for val in str(num1):
        repeat1[val] = repeat1.get(val, 0) + 1
    for val in str(num2):
        repeat2[val] = repeat2.get(val, 0) + 1
    return repeat1 == repeat2
