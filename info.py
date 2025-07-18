import streamlit as st
import pandas as pd

#CHANGE BELOW
profile_picture = "images/IMG_0768.JPG"
about_me = "I'm Ella Clem. I am a student at the Georgia Institute of Technology. "


#CHANGE BELOW (OPTIONAL)
linkedin_image_url = "https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"
github_image_url = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
email_image_url = "https://logowik.com/content/uploads/images/513_email.jpg"

#CHANGE BELOW
my_linkedin_url = "https://www.linkedin.com/in/ella-clem-8a7b202b9/"
my_github_url = "https://github.com/your-github-username"
my_email_address = "eclem3@gatech.edu"


education_data ={
    'Degree': 'Bachelor of Science in Business Administration',
    'Institution': 'Georgia Institute of Technology',
    'Location': 'Atlanta, GA',
    'Graduation Date': '2029',
    'GPA': '4.0'
}
course_data = {
    "code":["CS 1301", "ECON 2106", "MGT 3606", "MGT 3313"], 
    "names":["Intro to CS", "Principles of Microeconomics", "International Business Law", "Social Media Marketing"], 
    "semester_taken":["1st", "1st", "4th", "3rd"],
    "skills":["Basic Coding", "Budgeting", "Legal Business Understanding", "Creativity"],
    }
experience_data = {
    "Social Media Manager": (["- Created social media posts for multiple businesses",
                                                                          "- Worked for companies like MK Design Group and Happy Bellie Family Farms", "- Grew account attention and following"],"images/Instagram_icon.png.webp"),
    "Sports Coach":(["- Coached both recreational soccer and gymnastics.",
                                                           "- Taught kids coachability and teamwork", "- Taught kids coachability and teamwork"],"images/coach.jpg"),
    "Business Owner":(["- Creator and co-owner of Happy Bellie Family Farms Microgreens."],"images/Microgreens.jpg")

}

projects_data = {
    "Professiobal Webpage": "Coded a webpage to present professional information about my skills, community involvment, and fun facts!", 
}

programming_data = {
    "Python": 20,
}

#CHANGE BELOW (OPTIONAL)
programming_icons = {
    "Python": "🐍",
    "Java": "☕",
    "C": "🔍",
}
spoken_icons = {"English": "🇬🇧",
    "Spanish":"🇪🇸"
}

#CHANGE BELOW
spoken_data = {
    "English": "Fluent",
    "Spanish": "Proficient",
}
leadership_data = {
    "DECA VP of Leadership": (["- Ran a Business oriented student organization of over 300 students."],"images/deca.png"), "UFA Mountain Soccer Captain": (["- Led my soccer team in both vistory and loss during our season."],"images/ball.png"),

}
activity_data={
    "Elementary School Mentorship": ["- Mentored elementary school students", 
            "- Fostered friendship and community with kids"]
}

sibling_data={
    "**I have nine siblings!!!**": ["- I am the youngest", 
            "- I have 5 sisters and 4 brothers"]
}
food_data={
    "My favorite food is french fries": ["- Chick-fil-a and McDonald's are the best!"],
}
pets_data={
    "This is my dog, Piper.": (["- Shes a pitbull/bulldog mix."],"images/piper.JPG"), "This is my dog, Jameson.": (["- He's a Golden Retriever."],"images/IMG_2128.JPG"),

}
traits_data = {
    "Creative": 90, "Messy": 20, "Responsible": 95, "Fun": 75, "Ambitious": 95, "Sarcastic": 95,
}

chart_data = {
    "yield":[9,6,9,5,10],
    "year":["Tate Macrae","Taylor Swift","Noah Kahan", "Ariana Grande","Charli XCX"]
}
home_picture = "images/IMG_2420 2.jpeg"
quiz_data =[
    {"question": "What is my favorite color?", "choices": ["Blue", "Pink", "Green", "Purple"], "answer": "Pink"},
    {"question": "What is my favorite music artist?", "choices": ["Charli XCX", "Ariana Grande", "Noah Kahan", "Taylor Swift"], "answer": "Charli XCX"},
    {"question": "How many dogs do I have?", "choices": ["0", "1", "2", "3"], "answer": "2"},
    {"question": "How old am I?", "choices": ["15", "18", "20", "17"], "answer": "18"},
    {"question": "How many sisters do I have?", "choices": ["1", "3", "5", "7"], "answer": "5"}
]
def set_background(color="#FFC0CB"):
    """Set the background color of the main app container."""
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
