"""
m is the modulo(MOD).
n is the number that the user choose
r is remainder.

The euclid_algorithm takes 2 inputs(m and n) and gives 2 outputs(r and q).
With this algorithm we find the remainder of the division of n and m.

"""

def euclid_algorithm (m,n):

    m = input("Please enter an integer for m: ")
    n = input("Please enter an integer for n: ")
    x = n
    q = 0

    # q equals how mant time this loop runs
    while(int(x) - int(m)) >= 0:
        x = int(x) - 11
        q = q + 1
        print(x)

    r = int(n) % int(m)

    # we can also calculate q like this
    #q =int(((int(n) - int(r)) / int(m)))

    print("m = " + m)
    print("n = " + n)
    print("q = " + str(q))
    print("r = " + str(r))

#Test
euclid_algorithm (11,101)

