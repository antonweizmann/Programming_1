def factors(n):
    facts_n = []
    for i in range(1, n+1):
        if n % i == 0:
            facts_n.append(i)
    return facts_n

def is_prime(n):
    facts_n = factors(n)
    if len(facts_n) == 2:
        return True
    else:
        return False