# 3. A spam comment is defined as a text containing following keywords: 
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
# to detect these spams

Comment = input("Comment: ")
if "make a lot of money" in Comment or "buy now" in Comment or "subscribe this" in Comment or "click this" in Comment:
    print("Comment is a spam")
else: 
    print("Comment is fine")      