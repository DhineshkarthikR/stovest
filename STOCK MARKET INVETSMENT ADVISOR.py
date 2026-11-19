import yfinance as yf
import matplotlib.pyplot as plt
import mysql.connector as mysql

def get_company_name(cursor, ticker_symbol):
    cursor.execute("SELECT COMPANY_NAME FROM ticker WHERE TICKER_SYMBOL = %s", (ticker_symbol,))
    result=cursor.fetchone()
    if result:
        return result[0]
    return None

def analyze_stock(cursor, ticker):     # Function to analyze stock data
    try:
        company_name=get_company_name(cursor, ticker)
        if not company_name:
            print(f"No company found for ticker symbol {ticker}. Please check the database.")
            company_name="Unknown Company"

        # Ask for the number of days to analyze
        num_days=int(input("How many days of stock data would you like to analyze? "))
        stock=yf.Ticker(ticker)      # Fetching stock data for the specified number of days
        data=stock.history(period=f"{num_days}d")
        if data.empty:
            print(f"No data found for {ticker}. Please check the ticker symbol.")
            return
        dates = data.index
        prices = data['Close']
        plt.plot(dates, prices, marker='o', label=company_name)  # Setting label if company name is valid
        plt.title(f"{company_name} ({ticker}) Stock Price Trend")
        plt.xlabel("Date")
        plt.ylabel("Stock Price")
        plt.xticks(rotation=45)
        plt.legend() 
        plt.grid(True)
        plt.show()

        if prices.iloc[-1] > prices.iloc[0]:
            print(f"{company_name} ({ticker}): Stock price is increasing.")
            print()
            print("Recommendation: Safe to Invest!")

        else:
            print(f"{company_name} ({ticker}): Stock price is decreasing.")
            print()
            print("Recommendation: Risky to Invest!")

    except Exception as e:
        print(f"Error: {e}")

# Main function
def main():
    try:
        # Connect to MySQL database
        mycon=mysql.connect(host="localhost", user="root", password="1234", database="stock_market")
        cursor=mycon.cursor()
        choose_2="YES"
        while choose_2.upper()=="YES":
            print("1. CREATE TABLE OF TICKER SYMBOL.")
            print("2. DISPLAY TICKER SYMBOL.")
            print("3. ANALYZE THE STOCK.")
            choose_1=int(input("Enter your choice: "))

            if choose_1==1:
                cursor.execute("CREATE TABLE IF NOT EXISTS ticker (S_NO INT, COMPANY_NAME VARCHAR(100), TICKER_SYMBOL VARCHAR(20))")
                n=int(input("How many records do you want to update? "))
                for i in range(n):
                    sno=int(input("Enter the serial number: "))
                    company_name=input("Enter the company name: ")
                    ticker_symbol=input("Enter the ticker symbol (e.g., TCS.NS): ")
                    cursor.execute("INSERT INTO ticker (S_NO, COMPANY_NAME, TICKER_SYMBOL) VALUES (%s, %s, %s)",(sno, company_name, ticker_symbol))
                mycon.commit()

            elif choose_1==2:
                cursor.execute("SELECT * FROM ticker")
                for row in cursor.fetchall():
                    print(f"| {row[0]:<3} | {row[1]:<13} | {row[2]:<4} |")

            elif choose_1==3:
                ticker=input("Enter the company ticker symbol (e.g., TCS.NS, RELIANCE.NS): ")
                analyze_stock(cursor, ticker)
                
            print()
            choose_2=input("Do you want to continue (YES/NO):")
            print()

        mycon.close()

    except Exception as e:
        print(f"An error occurred: {e}")

# MAIN PROGRAM
if __name__=="__main__":
    main()
