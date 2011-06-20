#coding:utf-8

dict = {"yamada":75,"endou":82}
print dict

print 'dict["itou"] = 89'
dict["itou"] = 89
print dict
print u"要素数=" + str(len(dict))

dict.update({"honda":52,"endou":92})
print dict
