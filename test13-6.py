#coding:utf-8

print tuple("ABC")
print tuple([20,18])

t = ("PHP","PERL")
print tuple(t)

t = ("B","C","A")
tmplist = list(t)
tmplist.sort()
t = tuple(tmplist)
print t
