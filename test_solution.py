from unittest import TestCase
from closestPair import solution
import random
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def test_case(length: int = 10000):
    lst1 = [random.randint(-10**9, 10**9) for _ in range(length)]
    lst2 = [random.randint(-10**9, 10**9) for _ in range(length)]
    return lst1, lst2


class TestSolution(TestCase):
    def test_solution(self):
        pair_number_list = []
        test_duration_list = []
        test_asimpt_list = []
        for i in range(1000, 21000, 1000):
            with self.subTest(i=i):
                pair_number_list.append(i)
                tick = datetime.now()
                [x, y] = test_case(i)
                solution(x, y)
                tock = datetime.now()
                diff = tock - tick
                print(diff.total_seconds(), i)
                test_duration_list.append(diff.total_seconds())
                test_asimpt_list.append(i * np.log(i))
        plt.plot(pair_number_list, test_duration_list, 'b')
        plt.show()
        plt.plot(pair_number_list, test_asimpt_list, 'r')
        plt.show()
