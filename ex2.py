products = [ 
    {"name": "Keyboard", "price": 45}, 
    {"name": "Monitor", "price": 180}, 
    {"name": "Mouse", "price": 25}, 
    {"name": "Headphones", "price": 75}, 
    {"name": "USB Drive", "price": 15}, 
    {"name": "Webcam", "price": 60} 
]

under50 = list(filter(lambda x: x["price"] < 50, products))
print(under50)
trimmed = list(map(lambda x: (x["name"], x["price"]), under50))
print(trimmed)