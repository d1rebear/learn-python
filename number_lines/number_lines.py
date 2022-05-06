inp = open("input.txt", "r")

numberlists_list = []
line_num_counts = []
for line_index, line in enumerate(inp):
    line = line.strip()
    if len(line) == 0:
        exit(f'Line #{line_index + 1} is empty')
    numbers = []
    for num in line.split(","):
        numbers.append(int(num))
    numbers_count = len(numbers)
    if numbers_count < 1 or numbers_count > 10:
        exit(f'Count of numbers ({numbers_count}) in line #{line_index + 1} is out of range [1-10]')
    numberlists_list.append(numbers)
    line_num_counts.append(numbers_count)
    #print(f'Количество чисел в строке #{line_index + 1}: {numbers_count}')
print(f'Количество строк: {len(numberlists_list)}')


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

# even_index = 0
# odd_index = 0
# even_index_id = sublist[0]
# odd_index_id = sublist[0]
#список четных чисел
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
    print(f'Количество четных чисел в строке # {line_index +1}: {length_even_num}')
    print(f'Количество нечетных чисел в строке # {line_index + 1}: {length_odd_num}')
    print(f'Сумма четных чисел в строке # {line_index + 1}: {sum_even_num}')
    print(f'Сумма нечетных чисел в строке # {line_index + 1}: {sum_odd_num}')
    print(f'Четных чисел в % от общего количества чисел # {line_index + 1}: {percent_even_num}%')
    print(f'Нечетных чисел в % от общего количества чисел # {line_index + 1}: {percent_odd_num}%')

# even_nums_list = list(map(lambda i: i % 2 == 0, numberlists_list))
# print(even_nums_list)

# for i in range (1,30):
#     if i % 2== 0:
#         print (str(i) + ' =четное')
#     else:
#         print (str(i) + ' =нечетное')


#print(sum(numberlists_list[0]))

#sum_numbers = []
#number_id = sum(numberlists_list[0])
#sum_numbers.append(sum(numberlists_list[0]))
#print(sum_numbers)


# for x in numberlists_list:
#     sum_numbers.extend(x)
# print(sum_numbers)
# print(numbers)

# for max_sum_numbers_str in sum_numbers):
#     if max_sum_numbers_str > 0:
#         number_id = max_sum_numbers_str
#     index_of_var = numberlists_list.index(number_id)
# print(number_id)



# numbers_count_list.sort()
#
# print(f'Самая длинная строка под номером #{line_index + 1}: {numbers_count_list[-1]}')
# print(numbers_count_list)

# a = [18, 52, 23, 41, 32]
#
# #variable to store largest number
# ln = a[0] if a else None
#
# #find largest number
# for i in a:
# 	if i>ln:
# 		ln=i

# print("Largest element is: ",ln)

# вытаскиваем числа  из индексированной строки
# сравниваем эти числа

#for line_index, line in enumerate(lines)

# lines = [
#     "6,2,4,1,7",
#     "3,1,6",
#     "1"
# ]
#
# lines_count = 0
# for line_index, line in enumerate(lines):
#     line = line.strip()
#     if len(line) <= 0:
#         continue
#     lines_count += 1
#     numbers_as_str = line.split(',')
#     numbers = []
#
#     num_count = 0
#     for num_as_str in numbers_as_str:
#         num = int(num_as_str)
#         numbers.append(num)
#         num_count += 1
#     if num_count < 2 or num_count > 10:
#         exit(f'Count of numbers in line #{line_index} is out of range [2-10]')
#     print(f'line #{line_index}: {numbers}')
# print(f'lines_count: {lines_count}')
