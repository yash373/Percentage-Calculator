def getPercentage(n,total):
    return n/total*100

def main():
    total = float(input("Enter total: "))
    n = float(input("Enter n: "))
    print(f"Your percentage is: {getPercentage(n,total)}%")

if __name__ == '__main__':
    main()