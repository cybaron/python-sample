#coding:utf-8

list = ["A","B","C"]
print list

print 'list[len(list):] = "D"'
list[len(list):] = "D"
print list

print 'list[len(list):] = ["E","F"]'
list[len(list):] = ["E","F"]
print list

print 'list[1:1] = "a"'
list[1:1] = "a"
print list

print 'list[1:4] = []'
list[1:4] = []
print list
