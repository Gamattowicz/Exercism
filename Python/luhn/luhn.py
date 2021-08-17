class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")
        self.total = 1

        if self.card_num.isdigit() and len(self.card_num) > 1:
            first_num = [int(num) for num in self.card_num[-1::-2]]
            double_num = [int(num) for num in self.card_num[-2::-2]]
            for i, v in enumerate(double_num):
                if v * 2 > 9:
                    double_num[i] = v * 2 - 9
                else:
                    double_num[i] = v * 2
            self.total = sum(first_num + double_num)

    def valid(self):
        return self.total % 10 == 0
