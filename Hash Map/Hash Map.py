stock_price = []
with open ("Book1.csv" ,"r") as f :
    for line in f :
        day,price = line.split(',')
        price = float(price)
        stock_price.append([day , price])

print(stock_price)

for element in stock_price:
    if element[0] == "7-Mar" :
        print(element[1])

stock_price = {}
with open ("Book1.csv" ,"r") as f :
    for line in f :
        day,price = line.split(',')
        price = float(price)
        stock_price [day] = price

print(stock_price)
print(stock_price["8-Mar"])