stockPurchase = 0.0
stockSale = 0.0
sharesPurchased = 0
sharesSold = 0
pricePerShare = 0.0
pricePerShareSell = 0.0
amountPaid = 0.0
amountSold = 0.0

stockPurchase = float(input("Enter commission rate percentage on stock purchase: "))
stockSale = float(input("Enter commision rate percentage on stock sale: "))
sharesPurchased = int(input("Enter number of shares purchased: "))
sharesSold = int(input("Enter number of shares sold: "))
pricePerShare = float(input("Enter Purchase price per share: "))
pricePerShareSell = float(input("Enter sell price per share: "))
                      
amountPaid = sharesPurchased * pricePerShare
amountSold = pricePerShareSell * sharesSold                      
print("Amount paid for the stock: $", amountPaid)
print("Commission paid on the purchase: $", format((stockPurchase * amountPaid), '.2f'))
print("Amount the stock sold for: $", format((amountSold),'.2f'))
print("Commission paid for the sale: $", format((amountSold * stockSale),'.2f'))
print("Profit ( or loss if negative): $", format(((amountSold-amountPaid)-(stockPurchase * amountPaid)-(amountSold * stockSale)), '.2f'))
                      
