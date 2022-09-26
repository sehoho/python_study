# 071
my_variable = ()

print(type(my_variable))

# 072
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

print(movie_rank,type(movie_rank))

# 073
num = (1, )

print(num, type(num))

# 074
# t = (1, 2, 3)
# t[0] = 'a'

# 075
t = 1, 2, 3, 4

print(t, type(t))

# 076
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')

print(t)

# 077
interest = ('삼성전자', 'LG전자', 'SK Hynix')

print(list(interest))

# 078
interest = ['삼성전자', 'LG전자', 'SK Hynix']

print(tuple(interest))

# 079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 080
data = tuple(range(2, 99, 2))
print(data)