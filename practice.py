# my_dict = {
#     '0': {'1', '3'},
#     '1': {'0'},
#     '2': set(),
#     '3': {'0'}
# }

# print(my_dict)

# Print out all of the strings in the following array in alphabetical order, each on a separate line.
my_list = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot',
           'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']
# The expected output is:
# 'Cha Cha'
# 'Foxtrot'
# 'Jive'
# 'Paso Doble'
# 'Rumba'
# 'Samba'
# 'Tango'
# 'Viennese Waltz'
# 'Waltz'
# You may use whatever programming language you'd like.


for each in sorted(my_list):
    print(each)
