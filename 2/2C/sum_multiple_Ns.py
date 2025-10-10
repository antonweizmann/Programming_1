while 1:
    n = int ( input ( " Give me an integer N : " ) )
    if n < 0 :
        exit(0)
    sum = 0
    i = 0
    while i <= n:
        sum += i
        i += 1
    print ( " Sum from 0 to N is " + str ( sum ) )