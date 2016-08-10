theSum = 0            # use global variable rather than local variable
def sumTo(aBound):
    global theSum     # global copy of theSum
    print theSum
    for aNumber in range(1, aBound + 1):
        theSum = theSum + aNumber

    return theSum

print(sumTo(4))

print(sumTo(1000))
