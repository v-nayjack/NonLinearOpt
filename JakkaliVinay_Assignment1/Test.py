def myfunc():
    print("Please enter an anonymous function for x")
    n = input()
    return lambda x: x


if __name__ == '__main__':
    y = myfunc()
    print(y)
