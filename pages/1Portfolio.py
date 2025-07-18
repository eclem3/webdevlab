
import streamlit as st
import info
import pandas as pd

#About Me
def about_me_section():
    st.header("About Me")
    st.image(info.profile_picture, width = 200)
    st.write(info.about_me)
    st.write("This app delves into the facts, skills, and experiences of Ella Clem through interactive graphs, tabs, visuals, and quizzes about her!") 
    st.write('---')
about_me_section()

#Sidebar Links
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link=f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width = "75" height="75"></a>'
    st.sidebar.markdown(linkedin_link,unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link=f'<a href="{info.my_github_url}"><img src="data:image/png;base64,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" alt = "Github" width ="65" height ="65" ></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt = "Email" width ="75" height ="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)
links_section()

#Education
def education_section(education_data, course_data):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")
    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I learned"},
        hide_index=True,
        )
    st.write("---")
    
education_section(info.education_data, info.course_data)

#Professional Experience
def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title,(job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experience_section(info.experience_data)
#Projects
def project_section(projects_data):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander= st.expander(f"{project_name}")
        expander.write(project_description)
    st.write("---")
project_section(info.projects_data)

#Skills
def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill}{info.programming_icons.get(skill,'')}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}{info.spoken_icons.get(spoken,'')}:{proficiency}")
    st.write("---")
skills_section(info.programming_data, info.spoken_data)
#Activities
def activities_section(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander=st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)
    st.write("---")
    
activities_section(info.leadership_data, info.activity_data)









    
