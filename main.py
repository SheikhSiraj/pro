import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config("Resume Application", page_icon="favicon.ico", layout="centered")

# Load the CSS for custom styling
with open("CSS.css") as code:
    st.markdown(f"<style> {code.read()} </style>", unsafe_allow_html=True)

# Additional inline CSS for animations
st.markdown("""
    <style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .fade-in {
        animation: fadeIn 2s;
    }
    h1, h2, h3 {
        transition: color 0.5s;
    }
    h1 {
        color: #4CAF50;
    }
    h2 {
        color: #2196F3;
    }
    h3 {
        color: #FF5722;
    }
    </style>
""", unsafe_allow_html=True)

# Front page content
st.title("Resume Application")
st.header("Introduction")
st.write("This application allows users to input their data and generate a resume in DOCX format, with options for customization through various design templates.")

# Button to navigate to the app page
create = st.button("Create Your Resume!")
if create:
    st.write("Button clicked!")  # Debug statement
    switch_page("App")


st.header("Features")

st.subheader("1. Generate a Document")

st.subheader("- User Data Input")
st.write("- Users can input their personal and professional information required for creating a resume.")
st.write("- The application will guide users through different sections such as personal details, educational background, work experience, skills, and other relevant information.")

st.subheader("- Document Generation")
st.write("- Once all necessary information is provided, users can generate their resume.")
st.write("- The resume will be created in DOCX format.")
st.write("- Users can download the generated resume directly to their computer.")

st.subheader("2. Customize Resume Design")

st.subheader("- Customization Options")
st.write("- Users who wish to customize their resume design can access the 'View Digital Resume' button.")
st.write("- This feature offers four distinct design templates for the resume, each with unique attributes.")

st.subheader("- Template Features")
st.write("- The four design templates offer different layouts and styles, catering to various aesthetic preferences and professional needs.")
st.write("- Users can personalize their resumes by adjusting features such as color, font style, font size, and more.")
st.write("- These customization options allow users to create a visually appealing and professional resume.")

st.subheader("- Print Option")
st.write("- After customizing the resume, users can print the final version directly from the application.")

st.header("Workflow")

st.write("1. *Input Data:*")
st.write("   - Users start by entering their details in the provided fields.")
st.write("   - Sections include personal information, education, work experience, skills, and other optional sections.")

st.write("2. *Generate Resume:*")
st.write("   - After completing all input fields, users can generate their resume.")
st.write("   - The resume will be compiled into a DOCX file, which can be downloaded.")

st.write("3. *Customize Resume (Optional):*")
st.write("   - Users can choose to customize their resume by clicking on the 'View Digital Resume' button.")
st.write("   - They can select one of the four available templates.")
st.write("   - Users can modify the template to suit their preferences by changing colors, fonts, and text sizes.")

st.write("4. *Print Resume:*")
st.write("   - Once satisfied with the customization, users can print their resume directly from the application.")

st.header("Conclusion")
st.write("The Resume Generator and Customization Application provides a comprehensive solution for users to create and personalize their resumes. With the ability to input data, generate a DOCX file, customize templates, and print the final document, users can easily create professional resumes tailored to their needs.")

