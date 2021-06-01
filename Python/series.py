def slices(series, length):
    if length < 1 or len(series) < length:
        raise ValueError("Length of output string must be greater than or equal to the length of series")
    return [series[i:i+length] for i in range(len(series)-length+1)]

