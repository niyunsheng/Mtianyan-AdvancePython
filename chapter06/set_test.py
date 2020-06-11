#set 集合 fronzenset (不可变集合) 无序， 不重复
# s = set('abcdee')
# s = set(['a','b','c','d','e'])
s = {'a','b', 'c'}
fs1 = frozenset("abcde") #frozenset 可以作为dict的key
print(fs1)
fs2 = frozenset("bcdea")
print(fs2)
print(fs1&fs2)

#向set添加数据
another_set = set("cef")
re_set = s.difference(another_set)
re_set = s - another_set
re_set = s & another_set
re_set = s | another_set

#set性能很高
# | & -  #集合运算
print(re_set)

print (s.issubset(re_set))
# if "c" in re_set:
#     print ("i am in set")
