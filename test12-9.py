#coding:utf-8

list = ["A","B","C","D","B"]
print list

print '"B" in list', "B" in list
print '"E" in list', "E" in list
print '"B" not in list', "B" not in list
print '"E" not in list', "E" not in list

if "B" in list:
  print 'list.index("B")', list.index("B")

if "B" in list:
  print 'list.count("B")', list.count("B")
