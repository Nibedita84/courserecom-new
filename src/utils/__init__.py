from src.exception import CourseRecomException
import os, sys
import yaml


def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r') as filename:
            return yaml.safe_load(filename)
    except Exception as e:
        raise CourseRecomException(e, sys)




### to 
import ast
def convert(text):
    L = []
    for i in text:
        L.append(i['name']) 
    return L


def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ",""))
    return L1


def collapse1(L):
    L1 = []
    for i in L:
        for j in i:
            L1.append(j)
    return L1


def recommend(course, similarity): 
    index = finald[finald['Title'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(finald.iloc[i[0]].Title)