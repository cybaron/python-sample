#coding:utf-8

list = ["A","B","C","D","E"]
print u"変更前",list

list[1] = "b"
print u"変更後",list

list[3:5] = ["d","e"]
print u"変更後",list

preflist = ["Tokyo","Osaka","Fukuoka"]
print u"変更前",preflist

preflist[1:2] = ["Osaka","Nagoya","Sapporo"]
print u"変更後",preflist
