import yfinance as yf

# Should not be a financial or utility company
# Also exclude foreign companies (e.g. CDR or ADR)
symbol = 'MSFT'

MSFT = yf.Ticker(symbol)

marketCap = MSFT.info['marketCap']
minimum_marketCap = 100000000

if marketCap < minimum_marketCap:
    print("Market capitalization needs to be greater than 100 million")

# Easy way of getting EBITDA and EV/EBITDA

yf_EBITDA = MSFT.info['ebitda']
yf_EVtoEBITDA = MSFT.info['enterpriseToEbitda']

# Harder way of getting EBITDA. Need to look at financial statements
# Data found for 6/30/2021

netIncome = 61271000000  # income statement
normalizedIncome = 60150420000
taxExpense = 9831000000  # income statement
interestExpense = 2346000000  # income statement
depreciationAmortization = 11686000000  # cash flow statement

EBITDA = netIncome + taxExpense + interestExpense + depreciationAmortization

# Harder way of getting EV/EBITDA

enterprise_value = 0
