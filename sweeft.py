# words = input('Enter some words:  ')
# all_words = words.split(' ')
# distinct_words = set(all_words)
# # print(len(distinct_words))
# print(sorted(all_words))

'''
using given sample input
4 bcdef abcdefg bcde bcdef

'''
# words = 'bcdef abcdefg bcde bcdef'
# all_words = words.split(' ')
# distinct_words = set(all_words)
# print(len(distinct_words))

# def count_d_words(all_words, element):
#     return all_words.count(element)

# print(count_d_words(all_words, 'bcdef'), count_d_words(all_words, 'abcdefg'), count_d_words(all_words, 'bcde'))



# def bigger_is_greater(w):
#     lngth = len(w)
#     for i in range(lngth-2, -1, -1):
#         if ord(w[i]) < ord(w[i+1]):
#             break
#     else:
#         return 'no answer'
#     for j in range(lngth - 1, i, -1):
#         if ord(w[j]) > ord(w[i]):
#             w = w[:i] + w[j] + ''.join(sorted(w[i:j] + w[j+1:]))
#             return w
#     return 'no answer'
# print(bigger_is_greater('acbbdef'))
    


