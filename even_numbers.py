original_list = [2, 15, 42, 76, 20, 3, 5, 1]
even_no = list(filter(lambda x: x % 2 == 0, original_list))
print('list of even numbers:', even_no)

# output
# list of even numbers: [2, 42, 76, 20]
