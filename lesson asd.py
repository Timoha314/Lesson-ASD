from collections import Counter
def lesson(n, arr1):
    def generate_pair_sums(arr):
        pair_sums = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                pair_sums.append(arr[i] + arr[j])
        return pair_sums
    arr1_counter = Counter(arr1)
    arr1.sort()
    result = []
    a1 = arr1[0] // 2
    result.append(a1)
    arr1_counter[arr1[0]] -= 1
    if arr1_counter[arr1[0]] == 0:
        del arr1_counter[arr1[0]]
    while len(result) != n:
        current_sums = generate_pair_sums(result)
        for s in current_sums:
            if s in arr1_counter and arr1_counter[s] > 0:
                arr1_counter[s] -= 1
                if arr1_counter[s] == 0:
                    del arr1_counter[s]
        if arr1_counter:
            next_sum = min(arr1_counter)
            next_number = next_sum - result[0]
            result.append(next_number)
            arr1_counter[next_sum] -= 1
            if arr1_counter[next_sum] == 0:
                del arr1_counter[next_sum]
    return result

with open('input.txt', 'r') as file:
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))
result = lesson(n, arr)
with open('output.txt', 'w') as output_file:
    for num in result:
        output_file.write(str(int(num)) + '\n')
print(result)
