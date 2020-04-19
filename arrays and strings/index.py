  
#####################################

#given two strings, write a method to decide if one is a permutation of the other

#if two strings are permutations of each other the have the same character lengths in different orders
#ignoring whitespaces, capitalization and edge cases

def permutative_strings(str1, str2):
  while len(str1) == len(str2):
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)
  
    for idxa, idxb in zip(str1_sorted, str2_sorted):
      if idxa != idxb:
        return  False
      else:
        return True
  
  #next attempt => find a barebone replacement for zip
  
  #####################################