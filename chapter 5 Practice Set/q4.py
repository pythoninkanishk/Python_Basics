# 4. What will be the length of following set s: 
# s = set() 
# s.add(20) 
# s.add(20.0) 
# s.add('20')  length of s after these operations? 
s = set()
s.add(20)   
s.add(20.0)
s.add('20')
print("Length of set s:", len(s))
# The length of set s will be 3, as all three values are considered unique in a set.
print("Set s contains:", s)