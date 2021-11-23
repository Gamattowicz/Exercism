def saddle_points(matrix):
    if not matrix:
        return []

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError(r"Inappropriate matrix")

    row_max = []
    column_min = []

    for row in range(len(matrix)):
        max_value = max(matrix[row])
        for column, value in enumerate(matrix[row]):
            if value == max_value:
                row_max.append((row + 1, column + 1))

    for col in range(len(matrix[0])):
        column = [matrix[row][col] for row in range(len(matrix))]
        min_value = min(column)
        for row, value in enumerate(column):
            if value == min_value:
                column_min.append((row + 1, col + 1))

    result = set.intersection(set(row_max), set(column_min))

    return [{"row": row, "column": column} for row, column in result]
