#!/usr/bin/env python3

import names
import random
from tabulate import tabulate


def generate_random_name():
    return names.get_full_name()


def generate_random_grade():
    return random.randint(0, 100)


def generate_dummy_class_list(num=12):
    class_list_data = []
    for _ in range(num):
        class_list_data.append([generate_random_name(), generate_random_grade()])

    return class_list_data


if __name__ == '__main__':
    class_list = generate_dummy_class_list(10)
    class_list.sort(key=lambda x: x[1], reverse=True)
    print(tabulate(class_list, tablefmt='grid', headers=['Name', 'Grade']))

