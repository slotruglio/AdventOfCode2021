def getBit(n,list, i):
    zero = 0
    one = 0
    toReturn = ""

    for line in list:
        if line[i] == "0":
            zero += 1
        else: one += 1
    if zero > one:
        if n == 1: toReturn = "0"
        else: toReturn = "1"
    else:
        if n == 1:
            toReturn = "1"
        else: toReturn = "0"
    return toReturn


with open("input.txt", "r") as f:
    lines = f.readlines();

    oxygen = []
    co2 = []

    for line in lines:
        oxygen.append(line.strip())
        co2.append(line.strip())

    oxygen_pattern = ""
    co2_pattern = ""
    for i in range(0, len(lines[0])-1):
        if len(oxygen) > 1:
            oxygen_pattern = oxygen_pattern + getBit(1, oxygen, i)
            oxygen = [ele for ele in oxygen if ele.startswith(oxygen_pattern)]

        if len(co2) > 1:
            co2_pattern = co2_pattern + getBit(0, co2, i)
            co2 = [ele for ele in co2 if ele.startswith(co2_pattern)]

    oxygen_value = int(oxygen[0], 2)
    co2_value = int(co2[0], 2)

    print("oxygen: {}, co2: {}, life: {}".format(oxygen_value, co2_value, oxygen_value*co2_value))
