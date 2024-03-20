###from flask import Flask
import pickle
##import numpy as np
import streamlit as st
import pandas as pd
import dill



st.title('Course Recommender System')

courses_dict = pickle.load(open('courses.pkl','rb'))
courses = pd.DataFrame(courses_dict)
##similarity = pickle.load(open('model.pkl','rb'))

def recommend(course):
    coursed = pd.read_csv('/Users/Nivi/Documents/courserecom-new/transformed_data.csv')
    index = coursed[coursed['Title'] == course].index[0]
    similarity = pd.DataFrame(pickle.load(open('/Users/Nivi/Documents/courserecom-new/model.pkl', 'rb')))
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    
    course_list = []
    for i in distances[1:6]:
        course_list.append(coursed.iloc[i[0]].Title)

    return course_list

selected_course = st.selectbox('select the course', courses['index'].values)


if st.button('Recommend'):
    recommendations = recommend(selected_course)
    for i in recommendations:
        st.write(i)