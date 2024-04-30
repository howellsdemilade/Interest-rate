#Interest Rate Monthly Payment Calculator
def main():
    print(" This is a Monthly Payment Loan Calculator ")
    print("")
    
    principal = float(input("Input the Loan Amount: "))
    annual_interest_rate = float(input("Input the Annual Interest Rate: "))
    years = int(input("Input the Amount of Years: "))
    
    monthly_interest_rate = annual_interest_rate / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1-(1 + monthly_interest_rate) ** (-amount_of_months ))
    
    
    print(" The Monthly payment for this loan is: $%.2f " % monthly_payment)
    
main()
    