inp = open("input.txt", "r")

numberlists_list = []
line_num_counts = []
for line_index, line in enumerate(inp):
    line = line.strip()
    if len(line) == 0:
        exit(f'Строка #{line_index + 1} пуста')
    numbers = []
    for num in line.split(","):
        numbers.append(int(num))
    numbers_count = len(numbers)
    if numbers_count < 1 or numbers_count > 10:
        exit(f'Количество чисел ({numbers_count}) в строке #{line_index + 1} вне разрешенного диапазона [1-10]')
    numberlists_list.append(numbers)
    line_num_counts.append(numbers_count)
print(f'\nКоличество строк: {len(numberlists_list)}')

longest_line_num_count = line_num_counts[0]
longest_line_index = 0
shortest_line_num_count = line_num_counts[0]
shortest_line_index = 0

# Самая длинная и самая короткая строки:
for line_num_count in line_num_counts:
    if line_num_count > longest_line_num_count:
        longest_line_num_count = line_num_count
    elif line_num_count < shortest_line_num_count:
        shortest_line_num_count = line_num_count
longest_line_index = line_num_counts.index(longest_line_num_count) + 1
shortest_line_index = line_num_counts.index(shortest_line_num_count) + 1
print(f'Самая длинная строка # {longest_line_index}: {longest_line_num_count}')
print(f'Самая короткая строка # {shortest_line_index}: {shortest_line_num_count}')

line_sums_list = list(map(sum, numberlists_list))
max_sum_index = 0
min_sum_index = 0
max_sum_num = line_sums_list[0]
min_sum_num = line_sums_list[0]
# строка с наибольшей и наименьшей суммой чисел
for line_num_sum in line_sums_list:
    if line_num_sum > max_sum_num:
        max_sum_num = line_num_sum
    elif line_num_sum < min_sum_num:
        min_sum_num = line_num_sum
max_sum_index = line_sums_list.index(max_sum_num) + 1
min_sum_index = line_sums_list.index(min_sum_num) + 1
print(f'Наибольшая сумма в строке # {max_sum_index}: {max_sum_num}')
print(f'Наименьшая сумма в строке # {min_sum_index}: {min_sum_num}')

for line_index, sublist in enumerate(numberlists_list):
    odd_num_list = []
    even_num_list = []
    for number in sublist:
        if number % 2 == 0:
            even_num_list.append(number)
        else:
            odd_num_list.append(number)
    numbers_count = len(sublist)
    length_even_num = len(even_num_list)
    length_odd_num = len(odd_num_list)
    sum_even_num = sum(even_num_list)
    sum_odd_num = sum(odd_num_list)
    percent_even_num = length_even_num / (numbers_count / 100)
    percent_odd_num = length_odd_num / (numbers_count / 100)
    print(f'\nСтрока #{line_index +1}:')
    print(f'  Количество четных чисел: {length_even_num}')
    print(f'  Количество нечетных чисел: {length_odd_num}')
    print(f'  Сумма четных чисел: {sum_even_num}')
    print(f'  Сумма нечетных чисел: {sum_odd_num}')
    print(f'  Четных чисел в % от общего количества чисел: {percent_even_num}%')
    print(f'  Нечетных чисел в % от общего количества чисел: {percent_odd_num}%')
