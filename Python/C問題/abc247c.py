def c(n):
    if n==1:
        return "1"
    else:
        return c(n-1) +" " + str(n) +" "+ c(n-1)
print(c(int(input())))

