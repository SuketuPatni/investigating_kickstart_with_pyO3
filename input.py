import ks_d1_2021

def compare(list1, list2):
    check = True
    for i in range(0, len(list1), 1):
        if list1[i] != list2[i]:
            check = False
            print(f"Difference in output and expected output in test case {i+1}.")
            print(f"Output: {list1[i]}\nExpected output: {list2[i]}")
    if check:
        print("All tests passed successfully.")

# Test Set #1
answers_list1 = []

with open("test_set_1/ts1_input.txt") as f1:
    test_list_1 = f1.read().split("\n")

def parse_int(string):
    return [int(i) for i in string.strip().split(" ")]

for i in range(1, len(test_list_1), 3):
    vec_1, vec_2, vec_3 = (
        parse_int(test_list_1[i]), 
        parse_int(test_list_1[i + 1]), 
        parse_int(test_list_1[i + 2])
    )

    answers_list1.append(ks_d1_2021.solve(vec_1, vec_2, vec_3))

# print(answers_list)

with open("test_set_1/ts1_output.txt") as f2:
    answer_key1 = [int(k[-1]) for k in f2.read().split("\n")]

# answers_list1[1] = 7

print("Test Set 1:-")
compare(answers_list1, answer_key1)

# Test Set #2
answers_list2 = []

with open("test_set_2/ts2_input.txt") as f3:
    test_list_2 = f3.read().split("\n")

for i in range(1, len(test_list_2), 3):
    vec_1, vec_2, vec_3 = (
        parse_int(test_list_2[i]), 
        parse_int(test_list_2[i + 1]), 
        parse_int(test_list_2[i + 2])
    )
    answers_list2.append(ks_d1_2021.solve(vec_1, vec_2, vec_3))

# print(answers_list) 

with open("test_set_2/ts2_output.txt") as f4:
    answer_key2 = [int(k[-1]) for k in f4.read().split("\n")]

print("\nTest Set 2:-")
# answers_list2[3] = 8
# answers_list2[4] = 5 
compare(answers_list2, answer_key2)