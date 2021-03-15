from model.Stock import Stock
import time

# testing for a ultra cap stock
ticker = "AAPL"
# begin timer for execution
t1 = time.time()
stock1 = Stock.get_fundamental(Stock(ticker))
# end timer for execution
t2 = time.time()
print("Time to retrieve AAPL stock data in seconds = " + str(t2 - t1))
# testing if all the values retrieved are equivalent to the ratios in financial statements of apple
# all these numbers are gotten from sec.gov where one can view the papers of public financial statements
if stock1.get_priceFairValueTTM() != 30.95:
    print("Error: AAPL stock get_priceFairValueTTM() method is incorrect and does not equal 30.95 as shown in sec.gov, "
          "current value is " + str(stock1.get_priceFairValueTTM()))

if stock1.get_debtEquityRatioTTM() != 4.35:
    print("Error: AAPL stock get_debtEquityRatioTTM() method is incorrect and does not equal 4.35 as shown in sec.gov, "
          "current value is " + str(stock1.get_debtEquityRatioTTM()))

if stock1.get_priceToBookRatioTTM() != 30.95:
    print("Error: AAPL stock get_priceToBookRatioTTM() method is incorrect and does not equal 30.95 as shown in sec.gov, "
          "current value is " + str(stock1.get_priceToBookRatioTTM()))

if stock1.get_returnOnEquityTTM() != 0.91:
    print("Error: AAPL stock get_returnOnEquityTTM() method is incorrect and does not equal 0.91 as shown in sec.gov, "
          "current value is " + str(stock1.get_returnOnEquityTTM()))

if stock1.get_priceEarningsToGrowthRatioTTM() != 3.02:
    print("Error: AAPL stock get_priceEarningsToGrowthRatioTTM() method is incorrect and does not equal 3.02 as shown in sec.gov, "
          "current value is " + str(stock1.get_priceEarningsToGrowthRatioTTM()))

if stock1.get_returnOnAssetsTTM() != 0.18:
    print("Error: AAPL stock get_returnOnAssetsTTM() method is incorrect and does not equal 0.18 as shown in sec.gov, "
          "current value is " + str(stock1.get_returnOnAssetsTTM()))

if stock1.get_returnOnCapitalEmployedTTM() != 0.34:
    print("Error: AAPL stock get_returnOnCapitalEmployedTTM() method is incorrect and does not equal 0.34 as shown in sec.gov, "
          "current value is " + str(stock1.get_returnOnCapitalEmployedTTM()))

if stock1.get_currentRatioTTM() != 1.16:
    print("Error: AAPL stock get_currentRatioTTM() method is incorrect and does not equal 1.16 as shown in sec.gov, "
          "current value is " + str(stock1.get_currentRatioTTM()))

# testing if all the values retrieved are equivalent to the ratios in financial statements of carparts.com
# all these numbers are gotten from sec.gov where one can view the papers of public financial statements

# testing for a small cap stock
ticker = "PRTS"
# begin timer for execution
t1 = time.time()
stock1 = Stock.get_fundamental(Stock(ticker))
# end timer for execution
t2 = time.time()
print("Time to retrieve PRTS stock data in seconds = " + str(t2 - t1))
if stock1.get_priceFairValueTTM() != 8.69:
    print("Error: PRTS stock get_priceFairValueTTM() method is incorrect and does not equal 8.69 as shown in sec.gov, "
          "current value is " + str(stock1.get_priceFairValueTTM()))

if stock1.get_debtEquityRatioTTM() != 1.28:
    print("Error: PRTS stock get_debtEquityRatioTTM() method is incorrect and does not equal 1.28 as shown in sec.gov, "
          "current value is " + str(stock1.get_debtEquityRatioTTM()))

if stock1.get_priceToBookRatioTTM() != 8.69:
    print("Error: PRTS stock get_priceToBookRatioTTM() method is incorrect and does not equal 8.69 as shown in sec.gov, "
          "current value is " + str(stock1.get_priceToBookRatioTTM()))

if stock1.get_returnOnEquityTTM() != -0.7:
    print("Error: PRTS stock get_returnOnEquityTTM() method is incorrect and does not equal -0.7 as shown in sec.gov, "
          "current value is " + str(stock1.get_returnOnEquityTTM()))

if stock1.get_priceEarningsToGrowthRatioTTM() != 0.06:
    print("Error: PRTS stock get_priceEarningsToGrowthRatioTTM() method is incorrect and does not equal 0.06 as shown in sec.gov, "
          "current value is " + str(stock1.get_priceEarningsToGrowthRatioTTM()))

if stock1.get_returnOnAssetsTTM() != -0.12:
    print("Error: PRTS stock get_returnOnAssetsTTM() method is incorrect and does not equal -0.12 as shown in sec.gov, "
          "current value is " + str(stock1.get_returnOnAssetsTTM()))

if stock1.get_returnOnCapitalEmployedTTM() != -0.0:
    print("Error: PRTS stock get_returnOnCapitalEmployedTTM() method is incorrect and does not equal -0.0 as shown in sec.gov, "
          "current value is " + str(stock1.get_returnOnCapitalEmployedTTM()))

if stock1.get_currentRatioTTM() != 1.9:
    print("Error: PRTS stock get_currentRatioTTM() method is incorrect and does not equal 1.9 as shown in sec.gov, "
          "current value is " + str(stock1.get_currentRatioTTM()))

# testing if all the values retrieved are equivalent to the ratios in financial statements of Cabot Microelectronics
# all these numbers are gotten from sec.gov where one can view the papers of public financial statements

# testing for a medium cap stock
ticker = "CCMP"
# begin timer for execution
t1 = time.time()
stock1 = Stock.get_fundamental(Stock(ticker))
# end timer for execution
t2 = time.time()
print("Time to retrieve CCMP stock data in seconds = " + str(t2 - t1))
if stock1.get_priceFairValueTTM() != 4.44:
    print("Error: CCMP stock get_priceFairValueTTM() method is incorrect and does not equal 4.44 as shown in sec.gov, "
          "current value is " + str(stock1.get_priceFairValueTTM()))

if stock1.get_debtEquityRatioTTM() != 1.16:
    print("Error: CCMP stock get_debtEquityRatioTTM() method is incorrect and does not equal 1.16 as shown in sec.gov, "
          "current value is " + str(stock1.get_debtEquityRatioTTM()))

if stock1.get_priceToBookRatioTTM() != 4.44:
    print(
        "Error: CCMP stock get_priceToBookRatioTTM() method is incorrect and does not equal 4.44 as shown in sec.gov, "
        "current value is " + str(stock1.get_priceToBookRatioTTM()))

if stock1.get_returnOnEquityTTM() != 0.13:
    print("Error: CCMP stock get_returnOnEquityTTM() method is incorrect and does not equal 0.13 as shown in sec.gov, "
          "current value is " + str(stock1.get_returnOnEquityTTM()))

if stock1.get_priceEarningsToGrowthRatioTTM() != 0.14:
    print(
        "Error: CCMP stock get_priceEarningsToGrowthRatioTTM() method is incorrect and does not equal 0.14 as shown in sec.gov, "
        "current value is " + str(stock1.get_priceEarningsToGrowthRatioTTM()))

if stock1.get_returnOnAssetsTTM() != 0.06:
    print("Error: CCMP stock get_returnOnAssetsTTM() method is incorrect and does not equal 0.06 as shown in sec.gov, "
          "current value is " + str(stock1.get_returnOnAssetsTTM()))

if stock1.get_returnOnCapitalEmployedTTM() != 0.07:
    print(
        "Error: CCMP stock get_returnOnCapitalEmployedTTM() method is incorrect and does not equal 0.07 as shown in sec.gov, "
        "current value is " + str(stock1.get_returnOnCapitalEmployedTTM()))

if stock1.get_currentRatioTTM() != 3.8:
    print("Error: CCMP stock get_currentRatioTTM() method is incorrect and does not equal 3.8 as shown in sec.gov, "
          "current value is " + str(stock1.get_currentRatioTTM()))