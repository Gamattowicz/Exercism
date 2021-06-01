class Garden:
    seeds = {
        'G': 'Grass',
        'C': 'Clover',
        'R': 'Radishes',
        'V': 'Violets'
    }
    children = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
                'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students=children):
        self.diagram_1, self.diagram_2 = diagram.splitlines()
        self.students = sorted(students)
        self.cups = {}

        for i in range(len(self.diagram_1) // 2):
            seed_type = [self.diagram_1[i * 2], self.diagram_1[i * 2 + 1], self.diagram_2[i * 2], self.diagram_2[i * 2 + 1]]
            self.cups[self.students[i]] = [self.seeds[i] for i in seed_type]

    def plants(self, student):
        return self.cups[student]
