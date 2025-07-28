# Enter the row size for the pattern: 5
#         * 
#       * * * 
#     * * * * * 
#   * * * * * * * 
# * * * * * * * * * 

n = int(input("Enter Your Number: "))
for i in range(1,n+1):
    for j in range(1,n-i):
        print()