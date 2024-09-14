ranger = 4
l_a = list(range(0, ranger + 1))
print(l_a)

l_b = list(map(lambda x: (list(range(x,x+2))), l_a))
print(l_b)


average = list(map(lambda x:sum(list_x[(range(x,x+1)): range(x+1,x+2), l_a])))

average = list(map(lambda x:sum(list_x[x:x+1]), ranger))