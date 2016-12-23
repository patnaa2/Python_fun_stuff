'''
    Given an array of size n with numbers from 1 <= x <= n, find all
    numbers that are missing from array
'''

def find_missing_numbers(numbers):
    '''
        Inputs:
            :numbers - list of numbers

        Ouptuts:
            :missing - list of missing numbers
    '''
    for num in numbers:
        idx = abs(num) - 1
        if numbers[idx] > 0:
            numbers[idx] = -numbers[idx]

    missing = []
    for idx in xrange(len(numbers)):
        try:
            if numbers[idx] > 0:
                missing.append(idx+1)
        except:
            import pdb ; pdb.set_trace()
    return missing
