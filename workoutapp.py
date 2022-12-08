import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt 
from workoutdict import *
from workout_generator import *

# dropdown menu class
class Dropdown:
    # constructor for the menu options on the app
    def __init__(self, workout_today, previous_workout, weekly_workout, home, workout_planner, daily_macro_tracker):
        self.workout_today = workout_today
        self.previous_workout = previous_workout
        self.weekly_workout = weekly_workout
        self.home = home
        self.workout_planner = workout_planner
        self.daily_macro_tracker = daily_macro_tracker


# function that passes in a url for the background of the application
def add_bg_fromm_url(url):
    try:
        st.markdown(
            f"""
            <style>
            .stApp{{
                background-image: url({url});
                background-attachment: fixed;
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html= True
        )
    except:
        pass
# calls the function to fetch the background
add_bg_fromm_url("https://images.unsplash.com/photo-1604339454409-701c5278c546?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=627&q=80")

# creates a dropdown class with the menu option names
dropdown = Dropdown("Random workout", "Yesterday", "Weekly", "Home Page", "Choose your workout", "Daily Macro Goals")

# creates the side panel on the interface which passes in the dropdown class for the dropdown menu
selection = st.sidebar.radio("Welcome to my App! - Please select Home Page for FAQ or check out the random workout!",([dropdown.home, dropdown.workout_today, dropdown.workout_planner, dropdown.daily_macro_tracker]))

# creates the homepage introduction
if selection == "Home Page":
    st.header("Introduction")
    st.write("Hello, Welcome to my app!")
    st.write("This fitness app is aimed to help reduce the time spent creating workout plans as well as keeping track of your daily diet")
    st.write("This project idea came to life when many of my friends ask me for my workout plans. It takes a long time planning everybody's \
         workouts so I thought, why not try and automate it")
    st.write("This app is still work in progress and not everything is automated to where it should. \
        please stay in touch for all the latest updates")

# creates the body of random workout page
if selection == "Random workout":
    st.header("Daily random list of workouts")
    st.write(" ")

    # iterates through random workout and intensity generator and writes it into the app as bullets
    for x, y in zip(workout.get_workout_today(), random_intensity()):
            st.write(
                f"""
                * Exercise : {''.join(x)} - {''.join(y)} 
                """
                )   
    
# creates the body of workout planner page
if selection == "Choose your workout":
    st.header("Choose your workouts")
    multi_selector = st.multiselect("Exercise choices",exercise_key())

    rep_selector = st.multiselect("Intensity", intensity_list)
    submit = st.button("Submit")

    # error handling when selecting workouts from 2 boxes that do not have same index value
    try:
        download_csv = pd.DataFrame(multi_selector,rep_selector)
    except ValueError:
        st.error("Please fill both box")

    if submit:
        for i, j in zip(multi_selector, rep_selector):
            st.write(
                f"""
                * Exercise : {''.join(i)} - {''.join(j)} 
                """
                )

    # error handling when selecting workouts from 2 boxes that do not have same index value
    try:
        export_csv = st.download_button("Export CSV", download_csv.to_csv(), "text/csv")
    except NameError:
        st.error("Please fill intensity box")

# creates the body of macro tracker page
if selection == "Daily Macro Goals":
    st.header("Daily Macro Goals")
    daily_calories = st.text_input("Daily calorie goal")
    protein_tracker = st.text_input("Protein in grams")
    carb_tracker = st.text_input("Carbohydrates in grams")
    fat_tracker = st.text_input("Total fats in grams")
    calories_tracker = st.text_input("Total calorie intake today")
    check = st.button("Submit")

# initializes plot for pie chart and takes user input as data
    if check:
        remaining_calories = int(daily_calories) - int(calories_tracker)
        fig, axs= plt.subplots(1,2, figsize=(13,100))
        axs[0].pie([protein_tracker,carb_tracker,fat_tracker], labels = ["Protein", "Carb", "Fat"], autopct="%1.1f%%")
        axs[0].set_title("Macro Distribution")
        axs[1].pie([calories_tracker, remaining_calories], labels = ["Total daily calories", "Calories remaining"], autopct="%1.1f%%")
        axs[1].set_title("Calorie Distribution")
        st.pyplot(fig)