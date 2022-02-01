# <<<<<<<<<< Task 1 >>>>>>>>>>>>>
print("<<<<<<<<<< Task 1 >>>>>>>>>>>>>")

line_sum = sum(1 for line in open('sample.txt'))

all_num = 0
cycle = 1

with open("sample.txt") as file:
    file = file.read()

while range(0, line_sum):
    num_meter = 0
    for i in file:
        if i.isdigit():
            num_meter += 1
        elif i == "\n":
            print(f"Line {cycle} = ", num_meter, "number")
            all_num += num_meter
            num_meter = 0
            cycle += 1
        line_sum -= 1

print("In file", all_num, "number")

# <<<<<<<<<< Task 2 >>>>>>>>>>>>>
print("<<<<<<<<<< Task 2 >>>>>>>>>>>>>")

user_num_sum = 0
user_input = input("Enter searching number: ")

for j in file:
    if j == user_input:
        user_num_sum += 1
if user_num_sum == 0:
    print("Your num is not searched")
elif user_num_sum > 0:
    print("In file", user_num_sum, "your searching num")


# <<<<<<<<<< Task 3 >>>>>>>>>>>>>

# have questions

# <<<<<<<<<< Task 4 >>>>>>>>>>>>>
print("<<<<<<<<<< Task 4 >>>>>>>>>>>>>")

for q in file:
    with open("sample2.txt", "a") as file2:
        if q.isdigit():
            continue
        else:
            file2.write(q)

print("Complete")
