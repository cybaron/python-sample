#coding:utf-8

dict = {"yamada":75,"endou":82}
print dict

print 'del dict["endou"]'
del dict["endou"]

dict = {"yamada":75,"endou":82}
print dict

print 'dict.pop("yamada")'
val = dict.pop("yamada")
print u"削除された要素の値は" + str(val) + u"です"

print 'dict.pop("yamada","none")'
val = dict.pop("yamada","none")
print u"削除された要素の値は" + str(val) + u"です"

dict = {"itou":76,"yamada":75,"endou":82}
print dict

while dict:
  tuple = dict.popitem()
  print tuple
