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
create_date = "{:%m-%d-%Y}".format(date.today())
created_by = "ZAA"
footer = [('Created by', [created_by]), ('Created on', [create_date]), ('Version', [1.1])]
df_footer =pd.DataFrame.from_items(footer)
print(df_footer)


