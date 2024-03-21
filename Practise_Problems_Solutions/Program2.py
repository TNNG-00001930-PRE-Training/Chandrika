def dict(n):
    square_dict = {}
    for i in range(1, n+1):
        square_dict[i] = i*i
    return square_dict

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    square_dict = dict(n)
    print(square_dict)
