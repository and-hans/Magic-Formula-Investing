import yfinance as yf


# Should not be a financial or utility company
# Also exclude foreign companies (e.g. CDR or ADR)
symbol = 'MSFT'

ticker = yf.Ticker(symbol)

balanceSheet = ticker.balancesheet
cashFlow = ticker.cashflow
financialStat = ticker.financials

marketCap = ticker.info['marketCap']
minimum_marketCap = 100000000

if marketCap < minimum_marketCap:
    print("Market capitalization needs to be greater than 100 million")
if ticker.info['sector'] == 'Utilities' or ticker.info['sector'] == 'Financial Services':  # noqa: E501
    print("Cannot use a finances or utilities stock")

# Easy way of getting EBITDA and earnings yield

yf_EBIT = financialStat.iloc[8, 0]
yf_earningsYield = round(yf_EBIT/ticker.info['enterpriseValue'], 5)

yf_currentAssets = balanceSheet.iloc[18, 0]
yf_currentLiabilities = balanceSheet.iloc[13, 0]
yf_workingCapital = yf_currentAssets - yf_currentLiabilities

yf_returnOnCapital = round((yf_EBIT/(yf_currentAssets + yf_workingCapital))*100, 3)  # noqa: E501

'----------------'


# Harder way of getting EBIT. Need to look at financial statements
# Data found for 6/30/2021

netIncome = 61271000000  # income statement
normalizedIncome = 60150420000
taxExpense = 9831000000  # income statement
interestExpense = 2346000000  # income statement
depreciationAmortization = 11686000000  # cash flow statement

EBIT = netIncome + taxExpense + interestExpense

# Harder way of getting earnings yield

totalDebt = 67775000000  # balance sheet
cashAndEquivs = 130334000000  # balance sheet

enterprise_value = (marketCap + totalDebt) - cashAndEquivs

earningsYield = round(EBIT/enterprise_value, 5)

# Harder way of getting return on capital

currentAssets = 184406000000
currentLiabilities = 88657000000
workingCapital = currentAssets - currentLiabilities

fixedAssets = 184406000000

ROC = round(EBIT/(fixedAssets + workingCapital), 4) * 100
