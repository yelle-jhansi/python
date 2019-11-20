def is_multiple(m,n):
    #function to return true or false if multiple of m is n 
    if m==0: return False
    return (n%m==0)
if __name__ = "__main__":
    print(is_multiple(10,5))
