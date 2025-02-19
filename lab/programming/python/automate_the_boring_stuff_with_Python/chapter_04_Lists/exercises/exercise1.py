#!/usr/bin/python3


"""
Write a function that takes a list value as an argument and returns
a string with all the items separated by a comma and a space, with and
inserted before the last item. For example, passing the previous spam list to
the function would return 'apples, bananas, tofu, and cats'. But your func-
tion should be able to work with any list value passed to it.
"""
spam = ['apples', 'bananas', 'tofu', 'cats']


def format_list(name):
    if not name:
        return ""
    elif len(name) == 1:
        return name[0]
    else:
        return ", ".join(name[:-1]) + f", and {name[-1]}"


formated_list = format_list(spam)
print(formated_list)