from customs_duty import CustomsDuty

def main():
    calculator = CustomsDuty()
    num_importers = int(input("Enter the number of importers to assess: "))
    exchange_rate = float(input("Enter the Exchange Rate applicable today: "))
    calculator.assess_importers(num_importers, exchange_rate)
    duties = calculator.compute_duties(exchange_rate)

    print("\nDuty Amounts for Each Importer:")
    for i, duty_zwl in enumerate(duties, start=1):
        print(f"Importer {i}: ZWL {duty_zwl:.2f}")

    choice = input("\nDo you want to assess another set of importers? (yes/no): ")
    if choice.lower() == 'yes':
        main()
    else:
        print("Exiting program.")


if __name__ == "__main__":
    main()
