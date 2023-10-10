###from flask import Flask
import pickle
##import numpy as np
import streamlit as st
import pandas as pd
import dill



def recommend(course):
    index = course[course['index'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:6]:
        print(course.iloc[i[0]].Title)

st.title('Course Recommender System')

courses_dict = pickle.load(open('courses.pkl','rb'))
courses = pd.DataFrame(courses_dict)
##similarity = pickle.load(open('model.pkl','rb'))


selected_course = st.selectbox('select the course', courses['index'].values)


if st.button('Recommend'):
    ##recommend(selected_course)
    st.write(selected_course)