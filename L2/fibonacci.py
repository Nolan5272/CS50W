sequence = [0,1]
sequence_des_len = 10

sequence_des_len = int(input("Input Desired Length of Fibonacci Sequence (one interger): "))

for s in range(sequence_des_len):
    if(s > 1):
        sequence.append(sequence[s-1] + sequence[s-2])
        print(sequence[s])
    else:
        print(sequence[s])