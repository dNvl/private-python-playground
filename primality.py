import sys
import math

# Test primality for 2 to sqrt(n) and check for rest
def testPrimality(n):
    if(n == 1):
        return;
    m = 2
    while m < math.sqrt(n):
        if(n == 1):
            break;
        if(n % m == 0):
            return;
        else:
            m += 1
    #print('Number {} is a prime! Hurray!'.format(n))
    return n;

def preparePrimality(arg1, arg2):
    start = arg1
    end = arg2
    resList = []
    print('Testing prime range from {} to {}'.format(start, end))
    while start <= end:
        if(start % 2 == 0):
            start += 1
            continue;
        res = testPrimality(start)
        if(res):
            resList.append(res)
        start += 1
    return resList;


# The command line code
if(len(sys.argv) == 0):
    print('Please provide at least 1 argument or 2 for a range of calclations')
elif(len(sys.argv) == 2):
    res = testPrimality(int(sys.argv[1]))
    if(res == None):
        resList = 'none'
    else:
        resList = res
elif(len(sys.argv) > 2):
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    if(a == b):
        res = testPrimality(a)
        if(res == None):
            resList = 'none'
        else: 
            resList = res
    if(a < b):
        resList = preparePrimality(a, b)
    if(b < a):
        resList = preparePrimality(b, a)

print('Primes are: {}'.format(resList))

