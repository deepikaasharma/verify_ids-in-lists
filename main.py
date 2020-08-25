"""Write a function called verify_ids. This function takes two lists as arguments, and will return a boolean of whether those two lists have the same id()."""

list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
def verify_ids(list1, list2):
  return id(list1)==id(list2)

print(verify_ids(list1, list2))


"""Write a function called modify_third_elem that takes two arguments. The first argument is a list that is at least length 3, and the second argument is an element that will replace the item in the 3rd position of the list. This function will return the modified list.

Note: Be sure to follow the best practices taught in the previous lesson by not modifying the list that is passed as a parameter, but rather, a copy of that list.
"""
some_list =[1,2,3,4]
some_element = 'Deepika'
def modify_third_elem(some_list, some_element):
 modified_list = some_list.copy()
 modified_list[2] = some_element
 return modified_list

print(modify_third_elem(some_list, some_element))