#Finds Sum of digits of a number
def sumcal(n):
    r=-1
    sum=0
    while n>0:
        r = n%10
        sum+=r
        n//=10
    return sum

if __name__=="__main__":
    n= int(input("Enter the number: "))
    ans = sumcal(n)
    print(ans)