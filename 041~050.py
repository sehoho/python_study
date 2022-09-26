# 041
ticker = "btc_krw"
ticker_B = ticker.upper()

print(ticker_B)

# 042
ticker = "BTC_KRW"
ticker_A = ticker.lower()

print(ticker_A)

# 043
문자열 = 'hello'
문자열_A = 문자열.capitalize()

print(문자열_A)

# 044
file_name = "보고서.xlsx"
xlsx = file_name.endswith("xlsx")

print(xlsx)

# 045
file_name = "보고서.xlsx"
xls = file_name.endswith(("xlsx","xls"))

print(xls)

# 046
file_name = "2020_보고서.xlsx"
start = file_name.startswith("2020")

print(start)

# 047
a = "hello world"
b = a.split()
print(b)

# 048
ticker = "btc_krw"
ticker1 = ticker.split("_")

print(ticker1)

# 049
date = "2020-05-01"
date1 = date.split("-")

print(date1)

# 050
data = "039490      "
data1 = data.rstrip("")

print(data1)