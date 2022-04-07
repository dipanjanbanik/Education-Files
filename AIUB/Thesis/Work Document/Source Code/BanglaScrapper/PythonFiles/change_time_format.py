'''
Title:              Convert bangla date to english date
Author:             Mehedi, Zarin, Dipanjan
Created:            08-MAY-2018, 12:00 AM
Last modified:      24-Jun-2018, 09:09 PM
Last modified by:   Dipanjan
'''

# -*- coding: utf-8 -*-
import re
import datetime

def convert_time(date, month, year):
    bangla_month_name = ['জানুয়ারী', 'ফেব্রুয়ারী', 'মার্চ', 'এপ্রিল', 'মে', 'জুন', 'জুলাই', 'অগাস্ট', 'সেপ্টেম্বর',
                         'অক্টোবর', 'নভেম্বর', 'ডিসেম্বর']
    english_month_name = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september',
                          'october', 'november', 'december']

    bangla_month_number = ['১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '১০', '১১', '১২']
    english_month_number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

    bangla_numbers = ['১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '০']
    english_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    if month in bangla_month_name:
        v = bangla_month_name.index(month)

    english_date = list()
    english_year = list()
    for (x, z) in [(x, z) for x in date for z in year]:
        if '০' in (x, z):
            # print(x + 'next' + z)
            y = bangla_numbers.index(x)
            w = bangla_numbers.index(z)
            english_year.append(english_numbers[w])
            english_date.append(english_numbers[y])
        elif '১' or '০১' in (x, z):
            y = bangla_numbers.index(x)
            w = bangla_numbers.index(z)
            english_year.append(english_numbers[w])
            english_date.append(english_numbers[y])
        elif '২' or '০২' in (x, z):
            y = bangla_numbers.index(x)
            w = bangla_numbers.index(z)
            english_year.append(english_numbers[w])
            english_date.append(english_numbers[y])
        elif '৩' or '০৩' in (x, z):
            y = bangla_numbers.index(x)
            w = bangla_numbers.index(z)
            english_year.append(english_numbers[w])
            english_date.append(english_numbers[y])
        elif '৪' or '০৪' in (x, z):
            y = bangla_numbers.index(x)
            w = bangla_numbers.index(z)
            english_year.append(english_numbers[w])
            english_date.append(english_numbers[y])
        elif '৫' or '০৫' in (x, z):
            y = bangla_numbers.index(x)
            w = bangla_numbers.index(z)
            english_year.append(english_numbers[w])
            english_date.append(english_numbers[y])
        elif '৬' or '০৬' in (x, z):
            y = bangla_numbers.index(x)
            w = bangla_numbers.index(z)
            english_year.append(english_numbers[w])
            english_date.append(english_numbers[y])
        elif '৭' or '০৭' in (x, z):
            y = bangla_numbers.index(x)
            w = bangla_numbers.index(z)
            english_year.append(english_numbers[w])
            english_date.append(english_numbers[y])
        elif '৮' or '০৮' in (x, z):
            y = bangla_numbers.index(x)
            w = bangla_numbers.index(z)
            english_year.append(english_numbers[w])
            english_date.append(english_numbers[y])
        elif '৯' or '০৯' in (x, z):
            y = bangla_numbers.index(x)
            w = bangla_numbers.index(z)
            english_year.append(english_numbers[w])
            english_date.append(english_numbers[y])

    # english_date = [ii for n, ii in enumerate(english_date) if ii not in english_date[:n]]
    # english_year = [ii for n, ii in enumerate(english_year) if ii not in english_year[:n]]
    english_year = english_year[0:4]
    english_date = english_date[3:5]
    string_date = int(''.join(map(str, english_date)))
    string_month = english_month_number[v]
    string_year = int(''.join(map(str, english_year)))

    # print(string_date)
    # print(string_month)
    # print(string_year)
    final_date = datetime.date(string_year, string_month, string_date)
    return final_date

    # return string_date, string_month, string_year


# new = '২৬ জুন, ১০২৮ ইং'
# lst = tsplit(new, (',', 'ইং', ' '))
#
#
# lst = re.split(',| |ইং', new)
# lst = [str for str in lst if str]
# print(lst)
# print(list(lst[2]))
#
# inputstring = list(lst[2])
#
# convert_time(lst[0], lst[1], inputstring)

# import bangla
# k = bangla.convert_english_digit_to_bangla_digit(list(range(0, 12 + 1)))
# k = re.split(',| |\[|\]', k)
# k = [str for str in k if str]
# print(k)


# def tsplit(string, delimiters):
#     """
#     Behaves str.split but supports multiple delimiters.
#     Source: http://code.activestate.com/recipes/577616-split-strings-w-multiple-separators/
#     """
#     delimiters = tuple(delimiters)
#     stack = [string, ]
#
#     for delimiter in delimiters:
#         for i, substring in enumerate(stack):
#             substack = substring.split(delimiter)
#             stack.pop(i)
#             for j, _substring in enumerate(substack):
#                 stack.insert(i + j, _substring)
#
#     return stack
