def squareit(n):
    return n * n

def cubeit(n):
    return n*n*n

def main():
    anum = int(input("Please enter a number"))
    print(squareit(anum))
    print(cubeit(anum))

if __name__ == "__main__":     # uses an if statement to ask about the value of the __name__ variable. If the value is "__main__", then the main function will be called. 
    main()
