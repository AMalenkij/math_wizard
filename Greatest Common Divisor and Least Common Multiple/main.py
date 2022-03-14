#greatest common division(GCD)
count = []
def gcd(a = 24):
    if a != 1:
        if a % 2 == 0:
            count.append(2)
            gcd(a=a/2)
        else:
            count.append(3)
            gcd(a=a/3)

print(gcd())
print(count)

if __name__ == '__main__':

