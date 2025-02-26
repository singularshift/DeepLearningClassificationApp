import streamlit as st

def apply_custom_styles():
    """CSS styles for dark mode, fonts, and UI"""
    st.markdown(
        """
        <style>
            /* Background color */
            body {
                background-color: #121212;
                color: white;
                font-family: 'Orbitron', sans-serif;
            }
            /* Centering elements */
            .centered {
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            }
            /* Title styling */
            .title {
                font-size: 38px;
                font-weight: bold;
                text-align: center;
                color: #00FF41; /* Neon green */
            }
            /* Description styling */
            .description {
                text-align: center;
                font-size: 18px;
                color: #B0B0B0;
            }
            /* Upload box */
            .uploaded-file {
                border: 2px solid #00FF41;
                border-radius: 10px;
                padding: 10px;
                background-color: #222;
            }
            /* Button styling */
            .stButton>button {
                background-color: #0417ff !important;
                color: white !important;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 8px;
                transition: 0.3s;
            }
            .stButton>button:hover {
                background-color: #404fff !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def show_header():
    """Ttitle and description of the app"""
    st.markdown('<h1 class="title">🚀 CIFAR-10 Image Classifier | Deep Learning EDHEC</h1>', unsafe_allow_html=True)
    st.markdown('<h3 class="title">Luke O Donovan & Julius Walkenhorst</h1>', unsafe_allow_html=True)
    st.markdown('<p class="description">Upload an image (make sure that it has the right 32x32 format), and our model will predict what it is! It supports 10 categories: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck!</p>', unsafe_allow_html=True)
    st.markdown('<p class="description">After you uploaded your image, scroll down, click on "Classify", and let the magic happen!</p>', unsafe_allow_html=True)
    st.markdown("---")
