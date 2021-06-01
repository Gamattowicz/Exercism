class PhoneNumber:
    def __init__(self, number):
        numbers = ''.join([num for num in number if num.isdigit()])
        self.number = numbers[1:] if numbers[0] == '1' else numbers

        if len(self.number) != 10:
            raise ValueError('Phone number must have 10 numbers')
        elif self.number.startswith(('0', '1')) or self.number[3] == '0' or \
                self.number[3] == '1':
            raise ValueError('First and fourth number must be digit between 2 '
                             'and 9')

        self.area_code = self.number[0:3]

    def pretty(self):
        return f'({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}'