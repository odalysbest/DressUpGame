
list_hats = ['earmuff.png', 'necklace.png']
x = 250
y = 150
hats = []
for item in list_hats:
    hats.append(Button(item, x, y, item.split('.')[-1]))
    x += 150

list_shirts = ['crop-top.png', 'orange-shirt.png', 'pink-sweater.png']
x = 250
y = 250
shirts = []
for item in list_shirts:
    shirts.append(Button(item, x, y, item.split('.')[-1]))
    x += 150

list_shoes = ['boots.png', 'grey-shoes.png']
x = 250
y = 350
shoes = []
for item in list_shoes:
    shoes.append(Button(item, x, y, item.split('.')[-1]))
    x += 150

list_pants = ['jeans.png', 'red-skirt.png']
x = 250
y = 450
pants = []
for item in list_pants:
    pants.append(Button(item, x, y, item.split('.')[-1]))
    x += 150

list_dresses = ['overalls.png', 'purple-dress.png']
x = 250
y = 550
dresses = []
for item in list_dresses:
    dresses.append(Button(item, x, y, item.split('.')[-1]))
    x += 150
