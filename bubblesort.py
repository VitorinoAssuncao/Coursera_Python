import time
import random

def list_creator(size):
    rand_list = []
    for i in range(size -1):
        rand_list.append(random.randrange(1000)) 
    return rand_list

def bubble_sort(data_list):
    end = len(data_list)
    for i in range(end-1,0,-1):
        for j in range(0,i):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1],data_list[j]
                print(data_list)
    return data_list