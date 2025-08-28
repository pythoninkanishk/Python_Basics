# 5. Repeat program 4 for a list of such words to be censored.
Words_to_Sensor= ["fuck", "Drugs" , "Fucking"] 


def Sensor():
     with open("TXT.txt") as f:
        content = f.read()
     for word in Words_to_Sensor:
            content = content.replace(word, "#"*len(word))
     with open("TXT.txt", "w") as f:
         Text = f.write(content)
Sensor()