import pandas as pd
from collections import OrderedDict
from datetime import date

# Lists row oriented
sales = [('CocaCola LLC', 151, 201, 51),
         ('Apple Co', 133, 211, 31),
         ('RocketLawyer Inc', 131, 121, 111)]
labels = ['account','Jan','Feb','Mar']
df = pd.DataFrame.from_records(sales,columns = labels )
print(df)
print('--------------Column--------------------------------')
# Lists column oriented
salesCol = [('account', ['CocaCola LLC', 'Apple Co', 'RocketLawyer Inc']),
         ('Jan', [150, 200, 50]),
         ('Feb', [200, 210, 90]),
         ('Mar', [140, 215, 95]),
         ]
dfC = pd.DataFrame.from_items(salesCol)
print(dfC)
