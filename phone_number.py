class PhoneNumber:
    def __init__(self, number):
        self.number = ''.join([num for num in number if num.isdigit()])

        if self.number[0] == '1':
            self.number = self.number.replace('1', '', 1)

        if len(self.number) != 10:
            raise ValueError('Phone number must have 10 numbers')
        elif self.number.startswith(('0', '1')) or self.number[3] == '0' or \
                self.number[3] == '1':
            raise ValueError('First and fourth number must be digit between 2 '
                             'and 9')

        self.area_code = self.number[0:3]

    def pretty(self):
        return f'({self.number[0:3]})-{self.number[3:6]}-{self.number[6:10]}'