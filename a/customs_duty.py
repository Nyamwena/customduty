class Importer:
    def __init__(self, num_items):
        self.num_items = num_items
        self.items = []
        self.total_dutiable_value = 0

    def add_item(self, price_usd):
        self.items.append(price_usd)
        self.total_dutiable_value += price_usd

    def compute_duty(self, exchange_rate):
        duty_rate = 0.4  # 40% duty rate
        duty_zwl = self.total_dutiable_value * exchange_rate * duty_rate
        return duty_zwl


class CustomsDutyCalculator:
    def __init__(self):
        self.importers = []

    def assess_importers(self):
        num_importers = int(input("Enter the number of importers to assess: "))
        exchange_rate = float(input("Enter the Exchange Rate applicable today: "))

        for i in range(num_importers):
            num_items = int(input(f"Enter the number of items for importer {i + 1}: "))
            importer = Importer(num_items)
            for _ in range(num_items):
                price_usd = float(input("Enter the value for duty purposes (in USD) for each item: "))
                importer.add_item(price_usd)
            self.importers.append(importer)

        self.display_duty_amounts(exchange_rate)

    def display_duty_amounts(self, exchange_rate):
        print("\nDuty Amounts for Each Importer:")
        for i, importer in enumerate(self.importers, start=1):
            duty_zwl = importer.compute_duty(exchange_rate)
            print(f"Importer {i}: ZWL {duty_zwl:.2f}")

    def run(self):
        while True:
            self.assess_importers()
            choice = input("\nDo you want to assess another set of importers? (yes/no): ")
            if choice.lower() != 'yes':
                break


if __name__ == "__main__":
    calculator = CustomsDutyCalculator()
    calculator.run()
