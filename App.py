import streamlit as st
from io import BytesIO
from datetime import datetime
from functions import generate_docx, create_download_link, set_background_image, set_page_style
import streamlit as st
from io import BytesIO



def main():
    set_background_image('images\jjh.jpg')
    set_page_style()
    
    st.sidebar.title("Resume Generator")
    st.sidebar.markdown("Navigate through sections")

    st.markdown("<div class='main-content'>", unsafe_allow_html=True)  # Begin main content styling

    st.title("Create Your Professional Resume")

    # Personal Information
    st.header("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name*", placeholder="JOHN DOE", key='name')
        phone = st.text_input("Phone*", placeholder="(123) 456-7890", key='phone')
    with col2:
        email = st.text_input("Email*", placeholder="john.doe@example.com", key='email')
        linkedin = st.text_input("LinkedIn Profile (optional)", placeholder="linkedin.com/in/yourprofile", key='linkedin')

    website = st.text_input("Personal Website (optional)", placeholder="yourwebsite.com", key='website')
    summary = st.text_area("Summary*", placeholder="Brief summary about yourself.", key='summary')

    # User experience option
    user_type = st.selectbox("Are you a Fresher or Experienced?", ["Select", "Fresher", "Experienced"])

    # Highest Qualification section (mandatory for all users)
    st.header("Highest Qualification")
    qualification = {}
    
    col1, col2 = st.columns(2)
    with col1:
        degree = st.text_input("Degree*", placeholder="BSc in Computer Science", key='degree')
    with col2:
        institution = st.text_input("Institution*", placeholder="XYZ University", key='institution')

    education_status = st.selectbox("Education Status*", ["Completed", "Pursuing"], key='education_status')
    today = datetime.today().date()
    
    if education_status == "Completed":
        education_date = st.date_input("Completion Date*", value=today, key='completion_date')
    else:
        education_date = st.date_input("Expected Education Date*", value=today, key='expected_education_date')

    if degree and institution:
        qualification = {
            'degree': degree,
            'institution': institution,
            'education_date': education_date
        }

    # Experience section (only shown for experienced)
    experience = []
    if user_type == "Experienced":
        st.header("Experience")
        exp_count = st.number_input("Number of Experiences", min_value=1, max_value=7, step=1, key='exp_count')
        for i in range(exp_count):
            st.subheader(f"Experience {i + 1}")
            col1, col2 = st.columns(2)
            with col1:
                job_title = st.text_input(f"Job Title {i + 1}*", placeholder="Software Engineer", key=f"job_title_{i}")
            with col2:
                company = st.text_input(f"Company {i + 1}*", placeholder="ABC Corp", key=f"company_{i}")
            
            start_date = st.text_input(f"Start Date {i + 1}", placeholder="June 2023", key=f"start_date_{i}")
            end_date = st.text_input(f"End Date {i + 1}", placeholder="August 2024", key=f"end_date_{i}")
            responsibilities = st.text_area(f"Responsibilities {i + 1}*", placeholder="Describe your responsibilities.", key=f"responsibilities_{i}")

            if job_title and company:
                experience.append({
                    'job_title': job_title,
                    'company': company,
                    'start_date': start_date,
                    'end_date': end_date,
                    'responsibilities': responsibilities
                })

    # Skills section with box styling
    st.header("Skills")
    skills = st.multiselect(
        "Select Skills*", 
        options=["Python", "Java", "C++", "JavaScript", "HTML", "CSS", "SQL"], 
        key='skills'
    )

    # Projects section
    st.header("Projects (optional)")
    projects = []
    proj_count = st.number_input("Number of Projects", min_value=0, max_value=10, step=1, key='proj_count')
    for i in range(proj_count):
        st.subheader(f"Project {i + 1}")
        title = st.text_input(f"Project Title {i + 1}*", placeholder="Project Title", key=f"project_title_{i}")
        description = st.text_area(f"Project Description {i + 1}*", placeholder="Brief description of the project", key=f"description_{i}")
        role = st.text_input(f"Your Role in Project {i + 1}*", placeholder="Your role in the project", key=f"role_{i}")
        if title and description:
            projects.append({
                'title': title,
                'description': description,
                'role': role
            })

    # Awards section
    st.header("Awards (optional)")
    awards = []
    award_count = st.number_input("Number of Awards", min_value=0, max_value=10, step=1, key='award_count')
    for i in range(award_count):
        st.subheader(f"Award {i + 1}")
        title = st.text_input(f"Award Title {i + 1}*", placeholder="Award Title", key=f"award_title_{i}")
        reason = st.text_area(f"Award Reason {i + 1}*", placeholder="Reason for the award", key=f"award_reason_{i}")
        if title and reason:
            awards.append({
                'title': title,
                'reason': reason
            })

    # Font selection
    font_name = st.selectbox("Select Font*", options=["Arial", "Courier New", "Georgia", "Times New Roman"], index=0)

    # Button to generate resume
    if st.button("Generate Resume"):
        details = {
            'name': name,
            'email': email,
            'phone': phone,
            'linkedin': linkedin,
            'website': website,
            'summary': summary,
            'experience': experience,
            'education': qualification,  # Change to reflect highest qualification
            'skills': skills,
            'projects': projects,
            'awards': awards
        }
        doc = generate_docx(details, font_name)
        with BytesIO() as docx_file:
            doc.save(docx_file)
            docx_file.seek(0)
            st.markdown(create_download_link(docx_file.getvalue(), "resume.docx"), unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)  # End main content styling

if __name__ == "__main__":
    main()
