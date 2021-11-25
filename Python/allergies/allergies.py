class Allergies:
    allergens = {
        "cats": 128,
        "pollen": 64,
        "chocolate": 32,
        "tomatoes": 16,
        "strawberries": 8,
        "shellfish": 4,
        "peanuts": 2,
        "eggs": 1,
    }

    def __init__(self, score):
        self.score = score % 256
        self.result = []
        for allergen, value in self.allergens.items():
            if self.score - value >= 0:
                self.score -= value
                self.result.append(allergen)

    def allergic_to(self, item):
        return item in self.result

    @property
    def lst(self):
        return self.result
