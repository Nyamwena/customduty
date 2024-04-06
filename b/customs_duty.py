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


class CustomsDuty:
    def __init__(self):
        self.importers = []

    def assess_importers(self, num_importers, exchange_rate):
        for i in range(num_importers):
            num_items = int(input(f"Enter the number of items for importer {i + 1}: "))
            importer = Importer(num_items)
            for _ in range(num_items):
                price_usd = float(input("Enter the value for duty purposes (in USD) for each item: "))
                importer.add_item(price_usd)
            self.importers.append(importer)

        return self.compute_duties(exchange_rate)

    def compute_duties(self, exchange_rate):
        duties = []
        for importer in self.importers:
            duty_zwl = importer.compute_duty(exchange_rate)
            duties.append(duty_zwl)
        return duties
