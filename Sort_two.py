def sort(ip, A, B, n):
    #### Put in your sorting algorithm here
    #### This function will take as input:
    ########## ip: input list that consists of n element from {A,B}
    ########## You should assume that A<B
    cA= ip.count(A)
    cB= n-cA
    a=[A]*cA
    b=[B]*cB

    a[len(a):] = b

    return [A]*cA[len([A]*cA):] = [B]*cB # Returns the empty list for now
