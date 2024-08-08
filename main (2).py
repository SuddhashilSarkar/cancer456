import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Cancer Prediction", page_icon=":guard:", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
home_button = st.sidebar.button("Home")
about_button = st.sidebar.button("About")
prediction_button = st.sidebar.button("Prediction Tool")
learn_more_button = st.sidebar.button("Learn More")
contact_button = st.sidebar.button("Contact")

# Header
st.title("Cancer Prediction")
st.markdown(
    """
    <style>
    .css-1g7v5xk {
        background-color: #252627;
        color: #F9E7E7;
    }
    .css-1v0mbdj {
        color: #F9E7E7;
    }
    .css-1y4m7ee {
        background-color: #BE0E49;
        color: #F9E7E7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Content based on button clicks
if home_button:
    st.markdown("## Home")
    st.markdown("Empowering early detection through technology.")
    if st.button("Try the Prediction Tool", key="try_tool"):
        st.button("Prediction Tool")

elif about_button:
    st.markdown("## About the Project")
    st.write("This project aims to provide a reliable tool for predicting cancer based on user input, using advanced machine learning models.")

elif prediction_button:
    st.markdown("## Cancer Prediction Tool")
    # Form for prediction tool (details to be added based on your model)
    st.text_input("Enter mean radius:")
    st.text_input("Enter mean texture:")
    if st.button("Predict"):
        st.write("Prediction results will be displayed here.")

elif learn_more_button:
    st.markdown("## Learn More About Cancer")
    st.write(
        """
        **Understanding Cancer**
        Cancer is a broad term for a group of diseases characterized by the uncontrolled growth and spread of abnormal cells...

        **Common Types of Cancer**
        - Breast Cancer
        - Lung Cancer
        - Prostate Cancer
        - Colorectal Cancer
        - Skin Cancer

        **Symptoms to Watch For**
        - Unexplained weight loss
        - Persistent fatigue
        - Lumps or swelling
        - Persistent cough
        - Changes in bowel or bladder habits
        - Unusual bleeding

        **Cancer Risk Factors**
        - Lifestyle Choices
        - Environmental Exposure
        - Genetic Factors
        - Age

        **Cancer Prevention**
        - Avoiding Tobacco
        - Maintaining a Healthy Diet
        - Staying Physically Active
        - Protecting Yourself from the Sun
        - Getting Vaccinated

        **Treatment Options**
        - Surgery
        - Radiation Therapy
        - Chemotherapy
        - Immunotherapy
        - Targeted Therapy
        - Hormone Therapy

        **Living with Cancer**
        Receiving a cancer diagnosis can be overwhelming, but there are resources available to help manage the emotional, physical, and practical aspects of the disease.

        **Resources for Support**
        - [American Cancer Society](https://www.cancer.org)
        - [Cancer Research UK](https://www.cancerresearchuk.org)
        - [National Cancer Institute](https://www.cancer.gov)
        """
    )

elif contact_button:
    st.markdown("## Contact Us")
    # Form for contact (details to be added)
    st.text_input("Your Name")
    st.text_input("Your Email")
    st.text_area("Your Message")
    if st.button("Send"):
        st.write("Thank you for reaching out!")

# Footer
st.markdown(
    """
    <footer style="background-color: #BE0E49; color: #F9E7E7; text-align: center; padding: 10px;">
        <p>&copy; 2024 Cancer Prediction Project. All rights reserved.</p>
        <a href="#privacy-policy" style="color: #F9E7E7; text-decoration: underline;">Privacy Policy</a> |
        <a href="#terms-of-use" style="color: #F9E7E7; text-decoration: underline;">Terms of Use</a>
    </footer>
    """,
    unsafe_allow_html=True
)
