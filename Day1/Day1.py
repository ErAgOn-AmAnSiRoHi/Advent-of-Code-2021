def NumberofIncreases(data):
    increases = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            increases += 1
    return increases


with open("inputday1.txt") as f:
    one = [int(x) for x in f.read().split()]

print("PART 1", NumberofIncreases(one))

three = []
for i in range(2, len(one)):
    three.append(one[i] + one[i - 1] + one[i - 2])

print("PART 2", NumberofIncreases(three))
