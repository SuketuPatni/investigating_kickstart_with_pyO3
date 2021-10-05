import ks_d1_2021

# The old code to take inputs for test cases.

# T = int(input())
# answers_list = []
# for _ in range(0, T, 1):
    # vec_1 = [int(i) for i in input().split()]
    # vec_2 = [int(i) for i in input().split()]
    # vec_3 = [int(i) for i in input().split()]

    # answers_list.append(ks_d1_2021.solve(vec_1, vec_2, vec_3))

# for i in range(0, T, 1):
#     print(f"Case #{i + 1}: {answers_list[i]}")


# The new tests:-

def compare(list1, list2):
    check = True
    length = len(list1)
    for i in range(0, length, 1):
        if list1[i] != list2[i]:
            check = False
            print(f"Difference in output and expected output in test case {i+1}.")
            print(f"Output: {list1[i]}")
            print(f"Expected output: {list2[i]}")
    if check:
        print("All tests passed successfully.")

# Test Set #1
answers_list1 = []

f1 = open("test_set_1/ts1_input.txt")
test_list = f1.read().split("\n")

for i in range(1, len(test_list), 3):
    vec_1 = [int(j) for j in test_list[i].strip().split(" ")]
    vec_2 = [int(j) for j in test_list[i + 1].strip().split(" ")]
    vec_3 = [int(j) for j in test_list[i + 2].strip().split(" ")]
    answers_list1.append(ks_d1_2021.solve(vec_1, vec_2, vec_3))

# print(answers_list) # debugging
f2 = open("test_set_1/ts1_output.txt")
answer_key1 = [int(k[-1]) for k in f2.read().split("\n")]

# answers_list1[1] = 7 # to check testing

print("Test Set 1:-")
compare(answers_list1, answer_key1)

# Test Set #2
answers_list2 = []

f3 = open("test_set_2/ts2_input.txt")
test_list2 = f3.read().split("\n")

for i in range(1, len(test_list2), 3):
    vec_1 = [int(j) for j in test_list2[i].strip().split(" ")]
    vec_2 = [int(j) for j in test_list2[i + 1].strip().split(" ")]
    vec_3 = [int(j) for j in test_list2[i + 2].strip().split(" ")]
    answers_list2.append(ks_d1_2021.solve(vec_1, vec_2, vec_3))

# print(answers_list) # debugging
f4 = open("test_set_2/ts2_output.txt")
answer_key2 = [int(k[-1]) for k in f4.read().split("\n")]

print("\nTest Set 2:-")
# answers_list2[3] = 8 # to check testing
# answers_list2[4] = 5 
compare(answers_list2, answer_key2)
