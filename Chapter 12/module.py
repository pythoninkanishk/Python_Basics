def sum():
    n = int(input("Enter Your Number: "))
    m = int(input("Enter Your Second Number: "))
    print(m+n)
sum()    
print(__name__)

if __name__ == "__main__":
    print("This File was opened directly from the module")
elif __name__ == "module":
    print("This File was opened using import")

