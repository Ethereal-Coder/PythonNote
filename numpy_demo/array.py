# !/usr/bin/env python
# encoding: utf-8  
"""
Created by sunyh-vm on 19-4-23
Description:
"""

import random

import numpy as np


def array_creat():
    t1 = np.array([1, 2, 3])
    print(t1)
    print(type(t1))
    print(t1.data)
    print(t1.dtype)

    t2 = np.array(range(10))
    print(t2)
    print(type(t2))

    t3 = np.arange(10)
    print(t3)

    t4 = np.arange(2, 10, 2)
    print(t4)

    t5 = np.array([1, 0, 1, 0], dtype=np.bool)
    print(t5)
    t6 = t5.astype(np.int8)
    print(t6)

    t7 = np.array([random.random() for x in range(10)])
    print(t7)
    t8 = np.round(t7, 2)
    print(t8)
    pass


def array_shape():
    t1 = np.arange(12)
    print(t1.shape)

    t2 = np.array([[1, 2, 3], [4, 5, 6]])
    print(t2.shape)

    t3 = t2.reshape(3, 2)
    print(t2)
    print(t3)

    t4 = t1.reshape(2, 3, 2)
    print(t1)
    print(t4)

    print(t1.reshape(1, 12))
    print(t1.reshape(12, 1))

    t5 = t2.flatten()
    print(t5)

    pass


def array_calculate():
    t1 = np.array([[1, 2], [3, 4]])
    print(t1)
    print(t1+1)
    print(t1*2)
    print('-' * 20)

    t2 = np.array([[5, 6], [7, 8]])
    print(t1+t2)
    print(t1*t2)
    print('-' * 20)

    t4 = np.array([[5, 6]])
    print(t1 + t4)
    print(t1 * t4)
    print('-' * 20)

    t5 = np.array([[5]])
    print(t1 + t5)
    print(t1 * t5)
    print('-'*20)

    t6 = np.array([[5], [6]])
    print(t1 + t6)
    print(t1 * t6)
    print('-' * 20)

    # operands could not be broadcast together with shapes (2,2) (4,)
    # t3 = np.array([5, 6, 7, 8])
    # print(t1 + t3)
    # print(t1 * t3)
    pass


if __name__ == "__main__":
    # array_creat
    # array_shape()
    array_calculate()