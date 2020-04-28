  
#####################################

#given two strings, write a method to decide if one is a permutation of the other

#if two strings are permutations of each other the have the same character lengths in different orders
#ignoring whitespaces, capitalization and edge cases

# def permutative_strings(str1, str2):
    
#     str1_sorted = sorted(str1)
#     str2_sorted = sorted(str2)
#     if str1_sorted > str2_sorted:
#         diff = len(str1_sorted) - len(str2_sorted)
#         str2_sorted.extend([0] * diff)
#     if len(str2_sorted) > len(str1_sorted):
#         diff2 = len(str2_sorted) - len(str1_sorted)
#         str1_sorted.extend([''] * diff2)
    
#     print(len(str1_sorted), len(str2_sorted))
   
#     for idxa, idxb in zip(str1_sorted, str2_sorted):
#         if idxa != idxb:
#             return  False
#         else:
#             return True
  
  #next attempt => find a barebone replacement for zip

# permutative_strings('loki', 'helaaaa')
  #####################################
# one dict is to keep track of the frequency of each elements (key: element, value: frequency). The other keeps track of frequency of the frequency (key: frequency, value: number of elements that has that frequency
'''
queries = [[1, 3], [2, 3], [3, 5]]
blue = [ [1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1,6], [2, 5], [3, 2] ]

def lola(queri):
    freq = {}
    oc = {}  
    ans = []
    for query in queri:
        q = query[0]
        value = query[1]
        
            
        
        if q == 1:
            #insert
            if not value in oc:
                #if value is not yet in occurrences, add first to occurrences and set it to 0
                oc[value] = 0
            
            if not oc[value] in freq:
                #if freq dictionary doesnt have an occurrences value number we set it to 1
                freq[oc[value]] = 1
            
            #following our rules, we remove / subtract occurrences value by one => should always be kept at 1       
            freq[oc[value]] -= 1
            oc[value] += 1
            if not oc[value] in freq:
                #if freq dictionary doesn't have occurrrences we add it first adn set it to 0
                freq[oc[value]] = 0
            freq[oc[value]] += 1
            
        elif q == 2:
            if oc[value]:
                #delete
                freq[oc[value]] -= 1
                oc[value] -= 1
                freq[oc[value]]+= 1
                

        
        elif q == 3: 
            if value in freq:
                ans.append(1)
            else:
                ans.append(0)
                
    return ans

print(lola(blue))       

################## 
'''       
# def equalizer(arr):
#     frequency = []
#     for i in arr:
#         frequency.append(arr.count(i))
    
#     return len(arr)-max(frequency)

# # print(equalizer(arro))

# def equlizertwo(arr):
#     frequency = []
#     elements = list(set(arr))
    
#     for i in elements:
#         frequency.append(arr.count(i))
    
#     return max(frequency)

# print(equlizertwo(arro))
# print(equalizer(arro))



# def rev(s):

# import re
# delimiters = '()'
# lo = 'foo(bar)baz(blim)boo'
# po = lo.find('(') + len('(')
# op = lo.find(')')

# substring = lo[po:op]
# for i in lo:
#     if i == '(':
#         substring = lo[po:op]
#         reverse = substring[:: -1]
    
# # print(substring)
# # print(reverse)
# print(lo[:po-1] + reverse + lo[:op])
# # 'foorabbazmilbboo'
# # mo = list(lo)
# # # print(mo)
# # so = lo.split('(')
# # # print(so[0])
# # for i in so:
# #     if so[i] == '(':
#         # i == 'a'

# # so = re.split(r'[()]', lo)    
# # print(so)
# from collections import Counter
# def arrMix(arr1, arr2, arr3):

#     arr1.extend(arr2)
#     for j in arr1:
#         for j in arr3:
#             if j in arr1:
#                 arr1.remove(j)
#     data = Counter(arr1)
#     print(data)
#     dataList = list(data.keys())
#     print(dataList)
    
# original = ['one', 'two', 'three']
# nextlist = ['one', 'two', 'five', 'six']
# deletelist =['two', 'five']
# arrMix(original, nextlist, deletelist)

def palindromePermutation(str):
    #write a function to check if 
    #str is a permutation of a palindrome
    
    #palindrome => word/phrase thats the same 
    #forwards and backwards

    #permutation => rearrangement of letters
    
    #input Tact Coa
    #output True (permutations: 'taco cat', 'acto cta', etc)
    
    #palindrome phase 
        #using the two pointer approach
        
    #    for i in range(len(str), 0):
    #         i = 0
    #         j = str.length - 1
    #         while i < j:
    #             i += 1
    #             j -= 1
    #             if str[i] == str[j]:
                    
            
         
         
        
    