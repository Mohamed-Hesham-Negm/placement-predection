import streamlit as st
import pandas as pd
import numpy as np
import pickle

model = pickle.load(open(r"model_LogisticRegression.pkl","rb"))

st.title("Placement Predection")

st.write("CGPA - It is the overall grades achieved by the student.")
CGPA = st.slider("CGPA",min_value=0 ,max_value=10 ,value=5)

st.write("Internships - It tells the number of internships a student has done.")
Internships = st.slider("Internships",min_value=0 ,max_value=10 ,value=5)

st.write("Projects - Number of projects a student has done.")
Projects = st.slider("Projects",min_value=0 ,max_value=10 ,value=5)

st.write("Workshops/Certifications - As there are multiple courses available online student opt for them to upskill themselves.")
Workshops_Certifications = st.slider("Workshops/Certifications",min_value=0 ,max_value=10 ,value=5)

st.write("ApptitudeTestScore - Aptitude test are generally a part of the recruitment process to understand the Quant and logical thinking of the student.")
AptitudeTestScore  = st.slider("AptitudeTestScore ",min_value=50 ,max_value=100 ,value=75)

st.write("SoftSkillrating - Communication is a key role that plays in the placement or in any aspect of the life.")
SoftSkillsRating  = st.slider("SoftSkillsRating ",min_value=0 ,max_value=10 ,value=5)

st.write("ExtraCurricularActivities - This helps provide and insight about the personality of an individual regarding how much he is active other than the academic.")
ExtracurricularActivities  = st.selectbox("ExtracurricularActivities (0 for NO , 1 for YES)",[0,1])

st.write("PlacementTraining - It is provided to students in college to ace the placement process.")
PlacementTraining   = st.selectbox("PlacementTraining  (0 for NO , 1 for YES)",[0,1])

st.write("SSC - Senior Secondary")
SSC_Marks  = st.slider("SSC_Marks ",min_value=0 ,max_value=100 ,value=50)

st.write("HSC - Higher Secondary Marks.")
HSC_Marks  = st.slider("HSC_Marks  ",min_value=0 ,max_value=100 ,value=50)

features = np.array([CGPA,Internships,Projects,Workshops_Certifications,AptitudeTestScore,SoftSkillsRating
                     ,ExtracurricularActivities,PlacementTraining,SSC_Marks,HSC_Marks])


if st.button("predict"):
    predection = model.predict([features])
    if predection == 1 :
        st.write("This person placed")
    else :
        st.write("This person not placed")    