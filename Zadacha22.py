# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются 
# в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# Метод вернет список чисел, количество и значения которых будут введены с консоли.
def create_a_list_of_numbers_from_user(): 
    size = int(input("Введите количество чисел в наборе: "))
    if size < 1:
        print("Неверно указан размер списка: введите натуральное число.")
    else:
        our_list = list()
        for i in range(size):
            our_list.append(int(input("Введите целое число: ")))
    return our_list

our_n_list = create_a_list_of_numbers_from_user()
our_m_list = create_a_list_of_numbers_from_user()
our_n_values= set(our_n_list)
our_m_values = set(our_m_list)
values_common_for_both_lists = list(our_n_values.intersection(our_m_values))
values_common_for_both_lists.sort()
print(values_common_for_both_lists)