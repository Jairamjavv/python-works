# Method 1
def gcd1(gcd_num: tuple[int, int]):
    m, n = gcd_num
    
    # swap to keep the largest, smallest format
    if m < n:
        m, n = n, m
    
    # factors of m
    fm = []
    for i in range(1, m+1):
        if m%i == 0:
            fm.append(i)
    
    # factors of n
    fn = []
    for i in range(1, n+1):
        if n%i == 0:
            fn.append(i)

    # common factors between m and n
    cf = [1]
    for f in fm:
        if f in fn:
            cf.append(f)

    # return the largest common factor
    return cf[-1] 

# Method 2
def gcd2(gcd_num: tuple[int, int]):
    m, n = gcd_num

    # swap to keep the largest, smallest format
    if m < n:
        m, n = n, m
    
    # scan once in range 1 to max(m,n)
    cf = [1]
    for i in range(1, max(m,n)+1):
        if m%i == 0 and n%i == 0:
            cf.append(i)
        
    # return the largest
    return cf[-1]

# Method 3
def gcd3(gcd_num: tuple[int, int]):
    m, n = gcd_num

    # swap to keep the largest, smallest format
    if m < n:
        m, n = n, m

    # scan once in range 1 to min(m,n)
    # as gcd(m,n)<= min(m,n)
    cf = [1]
    for i in range(1, min(m,n)+1):
        if m%i == 0 and n%i == 0:
            cf.append(i)

    # return the largest
    return cf[-1]

# Method 4
def gcd4(gcd_num: tuple[int, int]):
    m, n = gcd_num

    # 1 will always the common factor for any 2 given numbers
    common_factor = 1

    # swap to keep the largest, smallest format
    if m < n:
        m, n = n, m

    # just store the latest common factor
    for i in range(1, min(m, n)+1):
        if m%i == 0 and n%i == 0:
            common_factor = i

    return common_factor

# Method 5
def gcd5(gcd_num: tuple[int, int]):
    m, n = gcd_num

    # swap to keep the largest, smallest format
    if m < n:
        m, n = n, m

    # 1 will always the common factor for any 2 given numbers
    common_factor = 1

    # scan backwards from min(m,n) to 1, return first common factor
    # to reduce the time to find the factor. On worst case O(min(m,n))
    for i in range(min(m, n), 1, -1):
        if m%i == 0 and n%i == 0:
            return i

    return common_factor

# Method 6 - Euclid GCD Variant 1
def gcd6(gcd_num: tuple[int, int]):
    m, n = gcd_num

    # swap to keep the largest, smallest format
    if m < n:
        m, n = n, m

    # chances are the smallest among m,n can be gcd
    # also serves as stopping condtion for recursion
    if m % n == 0:
        return n
    
    # use recursion
    else:
        # calculate the diff max-min
        diff = m - n

        # call recursion - gcd6
        return gcd6((max(n, diff), min(n, diff)))
    
# Method 7 - Euclid GCD Variant 2
def gcd7(gcd_num: tuple[int, int]):
    m, n = gcd_num

    # swap to keep the largest, smallest format
    if m < n:
        m, n = n, m

    # using while loop instead of recursion
    while m%n != 0:
        m, n = (max(n, m-n), min(n, m-n))

    return n

# Method 8 - Euclid GCD Variant 3
def gcd8(gcd_num: tuple[int, int]):
    m, n = gcd_num

    # swap to keep the largest, smallest format
    if m < n:
        m, n = n, m

    if m%n == 0:
        return n
    else:
        remainder = m%n
        return gcd8((max(n, remainder), min(n, remainder)))
    