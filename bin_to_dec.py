# Napisz funkcję, która pobierze stringa zawierającego liczbę w systemie dwójkowym
# i wypisze ją w systemie dziesiętnym.
# Przetestuj ją dla liczb '0', '101' i '1000000'.

def bin_to_dec(binary_number):
    decimal_number = 0
    power_of_two = 0
    for digit in binary_number[::-1]:
        decimal_number = decimal_number + int(digit) * 2 ** power_of_two
        power_of_two += 1
    return decimal_number


print(bin_to_dec('0'))
print(bin_to_dec('101'))
print(bin_to_dec('1000000'))

# s[::-1] - zwraca odwrócony string, czyli np zamiast 'ola' dostajemy 'alo'
# zapis x += 1 jest równoważny z zapisem: x = x + 1
