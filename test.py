# strI = "nihao"
# print(strI.find("i"),"\n" + str(strI.count("h")))

# text = 'Put several strings within parentheses '
         
# text += "666"
# print(text)

# words = ['cat', 'window', 'defenestrate']
# d = max(map(len, words))
# for x in words:
#     print(x.rjust(d),":",len(x))


users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# for keys,values in users.copy().items():
#     if values == 'inactive':
#         del users[keys]
    
d = max(map(len, users.items()))
for x in users:
    print(x.rjust(d),':',users[x])

i =1