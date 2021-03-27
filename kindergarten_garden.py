plants = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets'
}


class Garden:
    def __init__(self, diagram, students=['Alice', 'Bob', 'Charlie',
                                          'David', 'Eve', 'Fred', 'Ginny',
                                          'Harriet', 'Ileana', 'Joseph',
                                          'Kincaid', 'Larry']):
        self.diagram_1, self.diagram_2 = diagram.split('\n')
        students.sort()
        self.students = students

    def plants(self, student):
        index = self.students.index(student)
        if index != 0:
            index *= 2
        result = []
        for plant in (self.diagram_1[index:index+2] + self.diagram_2[
                                               index:index+2]):
            result.append(plants[plant])
        return result