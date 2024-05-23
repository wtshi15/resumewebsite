
#test zone
# import streamlit as st

# # Title of the app
# st.title("My Portfolio Website")

# # Display a greeting message
# st.write("hello world!!!")

# # Display more content to verify
# st.header("About Me")
# st.write("This is a simple portfolio website created using Streamlit.")




from datetime import datetime
from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV Website | Weitao Shi"
PAGE_ICON = ":computer:"
NAME = "Weitao Shi"
DESCRIPTION = """
Junior Business Honors Student at UT Austin, Focusing on Analytics and Computer Science
"""
EMAIL = "wtshi15@gmail.com"
SOCIAL_MEDIA = {
    # "YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://www.linkedin.com/in/weitaoshi",
    "GitHub": "https://github.com/wtshi15",
    # "Project Portfolio": "https://twitter.com",
}
# PROJECTS = {
#     "🏆 Sales Dashboard - Comparing sales across three stores": "https://youtu.be/Sb0A9i6d320",
#     "🏆 Income and Expense Tracker - Web app with NoSQL database": "https://youtu.be/3egaMfE9388",
#     "🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
#     "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
# }


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
# st.title("Hello World!")

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# # --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)

# d = {"wt":"s", "xm":"s"}
# teachers = ["xm"]
# duedate = "25/3/2024"
# subidate = datetime.strptime(duedate, "%d/%m/%Y")
# present = datetime.now()


# with st.popover("Username"):
#     st.markdown("Please enter your username")
#     username1 = st.text_input("Username: ")

# with st.popover("Password"):
#     st.markdown("Please enter your password")
#     password1 = st.text_input("Password ")

# submittable = False

# s1, s2, s3 = ('\n', '\n', '\n')
# if username1 in d and password1 == d[username1]:
#     s1 = ("Logging in... \n")
#     if username1 not in teachers:
#         if subidate.date() < present.date():
#             s2 = ("Submission date invalid.\n")
            
#         else:
#             s2 = ("Submission date valid.\n")
#             s3 = ("Please submit your file\n")
#             submittable = True
# else:
#     s1 = ("Please log in. \n")

# st.write(s1,s2)
# st.write(s2)
# st.write(s3)

# st.write("Students please submit your homework before the deadline.")
# st.write("The deadline is ", duedate)
# uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# if submittable:
#     for uploaded_file in uploaded_files:
#         bytes_data = uploaded_file.read()
#         st.write("filename:", uploaded_file.name)
#         st.write(bytes_data)

# # --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



# # --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Summer Intern | UT Southwestern Medical Center**")
st.write("June 2022 - July 2022")
st.write(
    """
- ► Organized Excel spreadsheets for experimental results on mice Slfn5 heredity for digestive diseases and colon cancer
- ► Executed 900 PCR Test Trials to generate critical data for identifying and differentiating useful lab mice genes
- ► Implemented effective repair for 2 lab machines for heightened security and sample preservation
"""
)

# # --- JOB 2
# st.write('\n')
# st.write("🚧", "**Data Analyst | Liberty Mutual Insurance**")
# st.write("01/2018 - 02/2022")
# st.write(
#     """
# - ► Built data models and maps to generate meaningful insights from customer data, boosting successful sales eﬀorts by 12%
# - ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of $300K
# - ► Compiled, studied, and inferred large amounts of data, modeling information to drive auto policy pricing
# """
# )

# # --- JOB 3
# st.write('\n')
# st.write("🚧", "**Data Analyst | Chegg**")
# st.write("04/2015 - 01/2018")
# st.write(
#     """
# - ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
# - ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
# - ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
# """
# )



# # --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Pandas, Scikit-learn, NumPy), R, SQL
- 📊 Data Visulization: MS Excel, Matplotlib, Seaborn
- 📚 Modeling: K Means Clustering, Multiple Linear Regression, Association Rule Learning, Decision Trees
- 🗄️ Databases: MySQL, SQLite, MS Azure
"""
)

# # --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 7 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")