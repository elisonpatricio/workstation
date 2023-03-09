from bcb import currency
import matplotlib
df = currency.get(['USD', 'EUR'],
                  start='2000-01-01',
                  end='2021-01-01',
                  side='ask')


print(df.head())

df.plot(figsize=(12, 6));

print(currency.get_currency_list().head())

# https://www.bcb.gov.br/en/currencyconversion
# https://wilsonfreitas.github.io/python-bcb/currency.html#module-bcb.currency