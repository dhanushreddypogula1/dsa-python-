coins=[25,10,5,1]
amount=63

results=[]
for coin in coins:
    while amount>=coin:
        amount-=coin
        results.append(coin)
print(results)