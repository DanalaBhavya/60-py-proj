tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
}

def RomanToDecimal(roman):
    sum = 0
    for i in range(len(roman) - 1):
        l = roman[i]
        r = roman[i + 1]
        if tallies[l] < tallies[r]:
            sum -= tallies[l]
        else:
            sum += tallies[l]
    sum += tallies[roman[-1]]
    return sum