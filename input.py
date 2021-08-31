import ks_d1_2021
T = int(input())

answers_list = []

for _ in range(0, T, 1):
    vec_1 = [int(i) for i in input().split()]
    vec_2 = [int(i) for i in input().split()]
    vec_3 = [int(i) for i in input().split()]

    answers_list.append(ks_d1_2021.solve(vec_1, vec_2, vec_3))

for i in range(0, T, 1):
    print(f"Case #{i + 1}: {answers_list[i]}")