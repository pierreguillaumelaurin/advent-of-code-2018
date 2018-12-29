with open("../input/input.txt", "r") as input:
    data = input.readlines()

numbers = (int(i) for i in data)

is_calibrated = False
frequency = 0
past_frequencies = [0]
counter = 0

while not is_calibrated:
    for i in numbers:
        frequency += i
        if frequency in past_frequencies:
            is_calibrated = True
            print(frequency)
            break
        else:
            past_frequencies.append(frequency)
    print("\033[95m>", "looped through list ", counter, "times...", "last frequency is ", frequency)
    counter += 1
print(frequency)
