# Function to get user input for loan details
def get_loan_details():
    PV = int(input("How much do you wish to borrow? ($): "))
    i = int(input("What is the effective interest rate? (%): "))
    PMT = int(input("How much is the annual repayment? ($): "))
    return PV, i, PMT


# Function to validate repayment amount
def validate_repayment(PMT, INT):
    while PMT <= INT:
        PMT = int(input("The repayment is too low to amortise loan, please revise ($): "))
    return PMT


# Function to calculate amortisation schedule
def calculate_amortisation(PV, i, PMT):
    n = 1
    header = "YEAR\tINTEREST\tPAYMENT\tBALANCE"
    print(header)

    while PV > PMT:
        INT = int(PV * (i / 100))
        if PV < PMT:
            PMT = PV + INT
        PV = PV + INT - PMT
        print(f"{n}\t{INT}\t{PMT}\t{PV}")
        n += 1


# Function to ask user for repeat calculation
def repeat_calculation():
    return input("Do you wish to perform another calculation? (Y/N): ").upper()


# Main function to control the flow of the program
def main():
    repeat = True
    while repeat:
        PV, i, PMT = get_loan_details()
        PMT = validate_repayment(PMT, PV * (i / 100))
        calculate_amortisation(PV, i, PMT)
        repeat = repeat_calculation() == 'Y'
    print("Good day")


# Call the main function to start the program
if __name__ == "__main__":
    main()
