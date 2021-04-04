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
        self.diagram_1, self.diagram_2 = diagram.split('\n')
        self.students = sorted(students)

    def plants(self, student):
        index = self.students.index(student) * 2

        return [self.seeds[plant] for plant in (self.diagram_1[index:index+2] +
                                                self.diagram_2[index:index+2])]