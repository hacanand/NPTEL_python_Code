
#%%
# ice_cream=('vanilla','chocolate','strawberry','butter scotch')
# for flavour in ice_cream:
#     print(flavour)

# print(ice_cream[0])
 
import random
bet =int(input("your bet:"))
lucky_draw=random.randint(1,10)
account=0
if bet == lucky_draw:
    account+=900-100
else:
    account-=100
print(account)
