"""
You can implement helper function here if you want
"""
# from perm import prp_oracle
def attack(oracle, pi_func, p):
    """
    The challenger has sampled a bit b <- {0, 1} uniformly randomly:
        If b = 0, the challenger has chosen the PRP
        If b = 1, the challenger has chosen a uniformly random permutation

    Your goal is to predict the bit b that the challenger has sampled given access to p, the public permutation pi(x) used in PRP construction and oracle function

    The oracle function is simulating interacting with a challenger which has previously sampled a random bit b and two uniformly random keys k1 and k2 over the key space
        oracle(x) - returns the output on x where x is from 0 to p-1

    NOTE: 
        1. Ensure that x is from 0 to p-1
        2. A maximum of 5 queries can be made to oracle function
        3. You can make as many query as you want to the pi_func function
        4. For at most 3 queries to oracle, full score will be awarded
        5. For making 4 queries to oracle, 90% of the score will be awarded
        6. For making 5 queries to oracle, 85% of the score will be awarded

    TODO: Implement your code below
    """
    zero=oracle(0)
    one=oracle(1)
    minusone=oracle(p-1)
    denom=(one+minusone-2*zero)%p
    inv=pi_func(denom)
    l=(minusone-one)%p
    k1=(l*inv)%p
    check=(pi_func(k1+1)-pi_func(k1))%p
    if(check==(one-zero)%p):
        return 0
    else:
        return 1


    """
    Return guess of b (either 0 or 1)
    """

# obj=prp_oracle()
# res=attack(obj.oracle,obj.pi_func,obj.p)
# print(res)
# print(obj.b)