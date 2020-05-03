import pandas as pd
import numpy as np
from datetime import date

interestRate = 0.025
years = 15
paymentYears = 12
iniPrincipal = 200000
iniAddPrincipal = 50
startDate = (date(2018,1,1))

# Payment per month
pmt = np.pmt(interestRate / paymentYears, years * paymentYears, iniPrincipal)
print("Payment per month:",pmt)

# Period to calculate for one month
period = 1
# Calculate the interest
ipmt = np.ipmt(interestRate / paymentYears, period, years * paymentYears, iniPrincipal)
# Calculate the principal
ppmt = np.ppmt(interestRate / paymentYears, period, years * paymentYears, iniPrincipal)
print("Payment per month:",pmt,", Principal:",ppmt,", Interest:",ipmt)

# Period to calculate for 10 years, 120 months
periodYears = 120
# Calculate the interest
ipmt = np.ipmt(interestRate / paymentYears, periodYears, years * paymentYears, iniPrincipal)
# Calculate the principal
ppmt = np.ppmt(interestRate / paymentYears, periodYears, years * paymentYears, iniPrincipal)
print("Payment per month for 15 years:",pmt,", Principal:",ppmt,", Interest:",ipmt)

# Table of balance over time
rng = pd.date_range(startDate, periods=years * paymentYears, freq='MS')
rng.name = "PaymentDate"
df = pd.DataFrame(index=rng,columns=['Payment', 'Principal', 'Interest', 'AddPrincipal', 'Balance'], dtype='float')
df.reset_index(inplace=True)
df.index += 1
df.index.name = "Period"
df["Payment"] = pmt
df["Principal"] = np.ppmt(interestRate / paymentYears, df.index, years * paymentYears, iniPrincipal)
df["Interest"] = np.ipmt(interestRate / paymentYears, df.index, years * paymentYears, iniPrincipal)
# Convert to negative value in order to keep the sign the same
df["AddPrincipal"] = -iniAddPrincipal
df = df.round(2)
# Calculate balance using no optimize way.
df["Balance"] = 0
df.loc[1, "Balance"] = iniPrincipal + df.loc[1, "Principal"] + df.loc[1, "AddPrincipal"]
for i in range(2,  len(df) + 1):
    # Get the previous balance as well as current Payments
    prevBalance = df.loc[i-1, 'Balance']
    principal = df.loc[i, 'Principal']
    addPrincipal = df.loc[i, "AddPrincipal"]
    # If there is no balance, then do zero out the principal and interest
    if prevBalance == 0:
        df.loc[i, ['Payment', 'Principal', 'Interest', 'AddPrincipal', 'Balance']] = 0
        continue
    # If there is a payment does not pay it off, reduce the balance
    if abs(principal + addPrincipal) <= prevBalance:
        df.loc[i, 'Balance'] = principal + prevBalance + addPrincipal
    # If it does pay it off(When you pay all the mortgage), zero out the balance and adjust the final payment
    else:
        # Just adjust the principal down
        if prevBalance <= abs(principal):
            principal = - prevBalance
            addPrincipal = 0
        else:
            addPrincipal = (prevBalance - abs(principal))
        df.loc[i, 'Balance'] = 0
        df.loc[i, 'Principal'] = principal
        df.loc[i, 'AddPrincipal'] = addPrincipal
        df.loc[i, 'Payment'] = principal + df.loc[i, 'Interest']
df = df.round(2)








print(df)
