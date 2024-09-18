from datetime import datetime
from pathlib import Path

import streamlit as st
from PIL import Image

#Updated 09/18/2024

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
    "LinkedIn": "https://www.linkedin.com/in/weitaoshi",
    "GitHub": "https://github.com/wtshi15",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
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

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Banking Intern | Industrial and Commercial Bank of China**")
st.write("May 2024 – July 2024")
st.write(
    """
- ► Secured signatures as bank representative for 7.6M yuan worth of home and vehicle loans
- ► Educated staff on English-based tech skills for faster management of cameras and computers
- ► Developed 12 automated macro scripts for data entry tasks using Playwright and Selenium
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Research Intern | UT Southwestern Medical Center**")
st.write("June 2022 - July 2022")
st.write(
    """
- ► Organized Excel spreadsheets for research on digestive diseases and colon cancer
- ► Executed 900 PCR Test Trials to differentiate lab mice genes for further research
"""
)

# --- PROJECTS ---
st.write('\n')
st.subheader("Projects")
st.write("---")

# --- PROJECT 1
st.write("🚧", "**AI Research Team | Anhui University**")
st.write("May 2024 - Present")
st.write(
    """
- ► Conducted research on video editing, computer vision, and video healing using Stable Diffusion
- ► Documented research findings in 30 pages covering GPTs, vector encoding, and NLP
"""
)

# --- PROJECT 2
st.write('\n')
st.write("🏆", "**1st Place Hackathon | Business Analytics Association (BAXA)**")
st.write("March 2024")
st.write(
    """
- ► Solved database and programming challenges using SQL, Python, and Pandas
- ► Led a team of 4 to win 1st place despite technical hurdles and a DDOS attack
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Pandas, NumPy, PyTorch, TensorFlow, Selenium), SQL, R
- 📊 Data Visualization: MS Excel, Tableau, Matplotlib, Seaborn
- 📚 Modeling: K Means Clustering, Linear Regression, Decision Trees
- 🗄️ Databases: MySQL, Oracle, SQLite
"""
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Hands-on experience with Python, SQL, and Excel
- ✔️ Strong grasp of statistical principles and their applications
- ✔️ Excellent team-player with leadership experience
"""
)
