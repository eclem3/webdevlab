import streamlit as st
import info
import pandas as pd
import numpy as np
import json

st.subheader("The purpose of this page is to learn all about me! :)")

def slider(): #NEW
    st.subheader("Guess my age!")
    age = st.slider("How old do you think I am?", 0, 60, 25)
    st.write("I'm ", age, "years old")
    if age == 18:
        st.write("Correct! :)")
slider()

def button(): #NEW
        st.button("Reset", type="primary")
        if st.button("Click Me!"):
            st.write("Pink!")
        else:
            st.write("What is Ella's favorite color?")
button()

#if "counter" not in st.session_state:
   # st.session_state.counter = 0

#if "color" not in st.session_state:
    #st.session_state.color = "What is Ella's favorite color?"

#st.write(st.session_state)

#st.write("color question:", st.session_state.color)

#button = st.button("Click Me")
#"before pressing button", st.session_state
#if button:
   # st.session_state.counter += 1
   # if st.session_state.counter%2 == 0
     #   st.session_state.color = "What is Ella's favorite color?"
    #if st.session_state.counter%2 == 1
     #   st.session_state.color = "Pink!"
    #"after pressing button", st.session_state


def fun_facts(sibling_data, food_data, pets_data):
    tab1, tab2, tab3 = st.tabs(["Fun Fact 1", "Fun Fact 2", "Fun Fact 3"])
    with tab1:
        for title, details in sibling_data.items():
            expander=st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
                chart_data = pd.DataFrame(
                {
                    "siblings_count": [4, 5],
                    "Siblings": ["brothers","sisters"]
                
                }
            )           
            st.bar_chart(chart_data, x= "Siblings",y="siblings_count",y_label="Amount")             
    with tab2:
        for title, details in food_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
                
    with tab3:
        for title, (details, image) in pets_data.items():
            expander=st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    st.write("---")
fun_facts(info.sibling_data, info.food_data, info.pets_data)
        
def personal_traits(traits_data):
    st.header("Personality Traits")
    for skill, percentage in traits_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill,'')}")
        st.progress(percentage)
    
personal_traits(info.traits_data)
st.subheader("My Music Artist Ratings")
def fav_artist(chart_data):
    df = pd.DataFrame(chart_data)
    st.bar_chart(df, x="year", y="yield")
fav_artist(info.chart_data)


def mini_quiz(): #NEW
    st.title("Mini Quiz")
    with open("quiz_data.json") as f:
        quiz_data = json.load(f)
    if "answers" not in st.session_state:
        st.session_state.answers = [None] * len(quiz_data)
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    for idx, item in enumerate(quiz_data):
        st.write(f"**Q{idx+1}. {item['question']}**")
        st.session_state.answers[idx] = st.radio(
            f"Choose one:",
            item["choices"],
            key=f"q_{idx}"
            )
        st.write("---")
    if st.button("Submit Answers"):
        st.session_state.submitted = True
    if st.session_state.submitted:
        st.subheader("Results")
        score = 0
        for idx, item in enumerate(quiz_data):
            user_ans = st.session_state.answers[idx]
            correct_ans = item["answer"]
            if user_ans == correct_ans:
                st.success(f"Q{idx+1}: Correct - {user_ans}")
                score += 1
            else:
                st.error(f"Q{idx+1}: Incorrect - You chose '{user_ans}', correct answer is '{correct_ans}'")
        st.markdown(f"### Your Total Score: **{score} / {len(quiz_data)}**")
mini_quiz()
