a_list = [1, 2, 3, 4, 5]
b_list = ['a', 'b', 'c', 'd', 'e']
[[print(i, j) for i in a_list] for j in b_list]

[print(j) for i in a_list for j in b_list]
