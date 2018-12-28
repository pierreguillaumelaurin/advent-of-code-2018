with open("../../input/01/input.txt", "r") as input:
    data = input.readlines()

numbers = [int(i) for i in data]

frequency = 0
past_frequencies = []

for i in numbers:
    frequency += i
    if frequency in past_frequencies:
        print(frequency)
        break
    else:
        past_frequencies.append(frequency)
