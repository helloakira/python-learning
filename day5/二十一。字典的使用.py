p0 = {
    'name': '拉面',
    'price': 30,
}

p1 = {
    'name': '牛肉饭',
    'price': 40,
}

p2 = {
    'name': '柠檬茶',
}

p2['price'] = 15

print(p0, p1, p2)

shop = [p0, p1, p2]

print(shop[2]['price'])