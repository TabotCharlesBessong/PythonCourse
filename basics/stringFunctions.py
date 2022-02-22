
name = "Charles"
lasName = 'Bessong Tabot'

fName = lasName[:7]
lName = lasName[8:]
funky = lasName[::2]
reverName = lasName[::-1]
print(lName + "\n" + funky + "\n" + reverName + "\n" + fName )
print(len(name))
print(name.find('s'))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.replace('e','i'))
print(name*3)

website = 'https://google.com'
website2 = 'https://github.com/TabotCharlesBessong'

slice = slice(7,-4)
# slice[start:stop:step]

print(website[slice])
# print(website2[slice])
web = website2[:6:3]
web1 = website2[0::3]
print(web1)

