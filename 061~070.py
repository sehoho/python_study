# 061
price = ['20180728', 100, 130, 140, 150, 160, 170]
price1 = price[1:]

print(price1)

# 062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums1 = nums[::2]

print(nums1)

# 063
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums1 = nums[1::2]

print(nums1)

# 064
nums = [1, 2, 3, 4, 5]
nums1 = nums[::-1]

print(nums1)

# 065
interest = ['삼성전자', 'LG전자', 'Naver']

print(interest[0],interest[2])

# 066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print(" ".join(interest))

# 067
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print("/".join(interest))

# 068
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print("\n".join(interest))

# 069
string = "삼성전자/LG전자/Naver"
interest = string.split("/")

print(interest)

# 070
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()

print(data)