# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old.

def generatble(n):
     X =" "
     for i in range(1,11):
      X +=  f"{n} X {i} = {n*i}\n" 
     with open(f"Tables/Table_{n}.txt","w") as f:
         Text = f.write(X)
         




for i in range(2,21):
    generatble(i)