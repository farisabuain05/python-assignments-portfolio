def greg(x):
    if 0 <= x <= 1:
        cnt = True
        n = 1
        while cnt == True:
            a = 0
            for i in range(n):
                a = (((-1)**i)*(x**(2*i+1))/(2*i+1))
                error_bound = (x**(2*n+1)/(2*n+1))
                if error_bound <= 0.0001 and a == x:
                    print((a, n, error_bound))
                    cnt = False
                    break
                elif error_bound > 0.0001:
                    n += 1
                    
    else:
        print("Error!")

greg(-1)

greg(0)

greg(0.25)

greg(0.5)

greg(0.75)

greg(1)
