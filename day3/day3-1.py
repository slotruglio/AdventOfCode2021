with open("input.txt", "r") as f:
    lines = f.readlines()

    gamma = ""
    epsilon = ""

    for i in range(0, len(lines[0])-1):
        zero = 0
        one = 0
        for line in lines:
            line = line.strip()
            if line[i] == "0":
                zero += 1
            else: one += 1
        if(zero > one):
            gamma = gamma + str(0)
            epsilon = epsilon + str(1)
        else:
            gamma = gamma + str(1)
            epsilon = epsilon + str(0)

    gamma_rate = int(gamma, 2)
    epsilon_rate = int(epsilon, 2)

    print("gamma: ", gamma_rate)
    print("epsilon: ", epsilon_rate)
    print("power consumption: ", gamma_rate*epsilon_rate)



