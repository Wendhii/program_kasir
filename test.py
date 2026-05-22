test = [
    {
        "harga": 3000
    },
    {
        "harga": 3000
    }    
]
total = 0
for i in test:
    total += i['harga']
print(total)