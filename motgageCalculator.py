def main():
    #TODO Add Mortgage insurance

    homePrice = 0 # User entered home price value
    downPayment = 0 # User entered down payment
    downPaymentPercentString = "0" # User entered down payment percent, human readable
    downPaymentPercentInt = 0 # User entered down payment percent as int
    downPaymentPecentFloat = 0.00 # Down Payment percent as a decimal
    totalMortgage = 0 # Calculated total mortage required (price - down payment + insurance)
    mortgageRatePercent = 0.00 # User entered mortgage rate
    totalLength = 0 # User entered amoritization period
    paymentFreq = "monthly" # User entered payment frequency
    periodRate = 0.00 # Interest rate per payment period
    totalPayments = 0 # Total number of payment calculated
    periodPayment = 0.00 # Calculated payment per period
    totalDue = 0.00 # Calculated total payment over the length of the loan
    totalInterest = 0.00 # Calculated total interest paid

    # Get home price
    print("Enter the total home price")
    homePrice = int(input())

    # Get downpayment
    print("Enter your down payment percentage (just the number)")
    downPaymentPercentString = input()
    downPaymentPercentInt = int(downPaymentPercentString)
    downPaymentPecentFloat = downPaymentPercentInt/100
    downPayment = homePrice*downPaymentPecentFloat

    # Calculate total Mortgage
    totalMortgage = homePrice - downPayment

    # Get rate
    print("Enter the mortgage rate percetage (just the number)")
    mortgageRatePercent = float(input())
    mortgageRateDecimal = mortgageRatePercent/100

    # Get ammoritization period
    print("Enter the length of the loan in years")
    totalLength = int(input())

    # Get payment frequency and interest rate per period
    print("Enter the frequency of payment: 'monthly', 'biweekly' or 'weekly'")
    paymentFreq = input().lower()
    if paymentFreq == "monthly":
        periodRate = mortgageRateDecimal/12
    elif paymentFreq == "biweekly":
        periodRate = mortgageRateDecimal/26
    elif paymentFreq == "weekly":
        periodRate = mortgageRateDecimal/52
    else:
        print("Error: frequency entry not recognized")
        return

    # Calculate number of payments
    if paymentFreq == "monthly":
        totalPayments = totalLength*12
    elif paymentFreq == "biweekly":
        totalPayments = totalLength*26
    elif paymentFreq == "weekly":
        totalPayments = totalLength*52
    else:
        print("Error: frequency entry not recognized")
        return

    # Set math variables for better looking calculations
    P = int(totalMortgage)
    a = float(periodRate)
    n = int(totalPayments)

    # Print the variables before doing the math
    print("\n")
    print(f"totalMortgage (P) is {P}")
    print(f"Interest rate per peried (a) is {a}")
    print(f"Total payment number is {n}")
    print("\n")

    # Do the math to get the payment per period
    topPt1 = P*a
    topPt2Base = 1+a
    topPt2 = topPt2Base**n
    top = topPt1*topPt2
    bottomBase = 1+a
    bottom = bottomBase**n
    bottom = bottom - 1
    periodPayment = top/bottom

    # Calculate the total of the loan and the total interest
    totalDue = periodPayment*totalPayments
    totalInterest = totalDue-totalMortgage

    # Print the results
    print("\nBased on the information provided, the mortgage information is as follows")
    print(f"Your {paymentFreq} payment would be {periodPayment}")
    print(f"The total due over the length of the loan would be {totalDue}")
    print(f"The total interest paid over the length of the loan would be {totalInterest}\n")


if __name__ == "__main__":
    main()