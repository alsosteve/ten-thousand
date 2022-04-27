class Banker:
    balance = 0
    shelved = 0

    def shelf(self, x):
        self.shelved = x

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0

    def clear_shelf(self):
        self.shelved = 0