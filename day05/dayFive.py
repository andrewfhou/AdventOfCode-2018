from string import ascii_lowercase

with open("input.txt") as file:
    inputString = file.read().strip()


def partOne(inputs):
    i = 0
    while i < len(inputs) - 1:
        j = i + 1
        if inputs[i] != inputs[j] and inputs[i].upper() == inputs[j].upper():
            inputs = inputs[:i] + inputs[i+2:]
            i = max(0, i-1)
        else:
            i += 1

    return len(inputs)


def partTwo(inputs):
    minLen = len(inputs)
    for letter in ascii_lowercase:
        temp = inputs.replace(letter, "").replace(letter.upper(), "")
        minLen = min(minLen, partOne(temp))

    return minLen


def partTwoSlice(inputs):
    minLen = len(inputs)
    for letter in ascii_lowercase:
        i = 0
        while i < len(inputs) - 1:
            temp = inputs
            j = i + 1
            if temp[i].lower == letter and temp[i] != temp[j] and temp[i].upper() == temp[j].upper():
                temp = temp[:i] + temp[i+2:]
                i = max(0, i-1)
            i = i + 1
        minLen = min(minLen, partOne(temp))


print("Part One:", partOne(inputString))
print("Part Two:", partTwo(inputString))
