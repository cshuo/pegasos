# coding: utf-8
import numpy as np
import math
import sys
from random import randint

def hinge_update(w,t,y,x):
    '''使用hinge函数进行w的迭代更新'''
    indic = 0
    if w.dot(x) * y < 1:
        indic = 1
    sub_gradient = lamda * w - indic * float(y) * x
    sub_w = w - sub_gradient / (lamda * float(t))
    return sub_w

def log_update(w,t,y,x):
    '''使用logit函数进行w的迭代更新'''
    indice = w.dot(x) * y
    sub_gradient = lamda * w - float(y) * x / (1 + np.exp(indice))
    sub_w = w - sub_gradient / (lamda * float(t))
    return sub_w

def pegasos(s, y, test_s, test_y, type = 0):
    '''Pegasos算法主体，迭代更新𝒲'''
    intervals = range(1,11)
    T = 5 * s.shape[0]
    w = np.zeros(s.shape[1])
    for t in xrange(T):
        i = randint(0, s.shape[0]-1)
        if type == 0:
            w = hinge_update(w, t+1, y[i], s[i])
        else:
            w = log_update(w, t+1, y[i], s[i])
        #打印错误率
        if float(t+1) * 10 / (T - T % 10) in intervals:
            error_rt =  cal_error_ratio(w, test_s, test_y)
            print float(t+1) / (T - T % 10), "T ", error_rt
    return w


def cal_error_ratio(w, s, y):
    '''计算训练器的错误率'''
    error_num = 0
    for i in xrange(s.shape[0]):
        if w.dot(s[i]) * y[i] <= 0:
            error_num += 1
    return float(error_num) / s.shape[0]


def read_data(filename):
    '''从文本读取数据'''
    data_list = []
    with open(filename) as file_r:
        for line in file_r:
            vec = map(int, line.strip().split(','))
            data_list.append(vec)
    d_mat = np.array(data_list)
    #向量以及对应标签
    return d_mat[:,:-1], d_mat[:,-1]


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print "wrong paras!!!"
        sys.exit(0)
    lamda = float(sys.argv[3])
    type_loss = int(sys.argv[4])
    s,y = read_data(sys.argv[1])
    test_s, test_y= read_data(sys.argv[2])
    pegasos(s, y, test_s, test_y, type_loss)
