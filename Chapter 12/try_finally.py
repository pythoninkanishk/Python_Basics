

def main():
    try:
      N = int(input("Enter Your Number: "))
    except Exception as e:
     
     print(e)
    else:
      print(f"the entered number is {N}")
    finally:
     print("Thank You")
main()
# the code set in finally print everytime the code ends (with or without exception)

