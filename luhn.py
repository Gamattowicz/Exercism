class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        for num in self.card_num:
            if not num.isdigit():
                return False
        single = [int(num) for num in self.card_num[-1::-2]]
        doubled_num = []
        for num in self.card_num[-2::-2]:
            if int(num) * 2 <= 9:
                doubled_num.append(int(num) * 2)
            else:
                doubled_num.append(int(num) * 2 - 9)
        summary = single + doubled_num
        if len(summary) < 2:
            return False
        return sum(summary) % 10 == 0
