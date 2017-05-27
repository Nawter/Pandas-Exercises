import pandas as pd
from collections import OrderedDict
from datetime import date

# Dictionaries row oriented.
salesRow =[{'account':'CocaCola LLC', 'Jan':153, 'Feb':177, 'Mar':143},
        {'account':'Apple Co', 'Jan':201, 'Feb':277, 'Mar':343},
        {'account':'RocketLawyer Inc', 'Jan':253, 'Feb':377, 'Mar':543}]

df = pd.DataFrame(salesRow)
print(df)
print('--------------------column--------------------------------------')
# Dictionaries column oriented.
salesColumn ={'account': ['CocaCola LLC', 'Apple Co', 'RocketLawyer Inc'],
                'Jan': [150, 200, 50],
                'Feb': [200, 210, 90],
                'Mar': [140, 215, 95]}
dfC = pd.DataFrame.from_dict(salesColumn)
print(dfC)
print('--------------------ordered-------------------------------------')
# Manual ordered columns
dfC = dfC[['account','Jan','Feb','Mar']]
print(dfC)
print('----------------------------------------------------------------')
# Autmatic ordered columns
salesOrd = OrderedDict([ ('account', ['CocaCola LLC', 'Apple Co', 'RocketLawyer Inc']),
          ('Jan', [150, 200, 50]),
          ('Feb',  [200, 210, 90]),
          ('Mar', [140, 215, 95]) ] )
dfOrd = pd.DataFrame.from_dict(salesOrd)
print(dfOrd)
