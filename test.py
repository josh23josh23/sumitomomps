import streamlit as st

# Set page configuration to use the full width of the browser window
st.set_page_config(layout="wide")

hide_st_style = """
                <style>
                header {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("")

# Embed the website using an iframe
st.markdown(
    """
    <style>
    html, body, .stApp {
        margin: 0;
        padding: 0;
        height: 100vh;
        width: 100vw;
        overflow: hidden; /* Prevent scrollbars if content overflows */
    }
    .iframe-container {
        position: relative;
        height: 100vh; /* Full height of the viewport */
        margin-top: -190px; /* Adjust this value to move the iframe upwards */
        display: flex;
        justify-content: center; /* Center iframe horizontally */
    }
    iframe {
        width: 1760px;
        height: 945px;
        border: none;
    }
    /* Hide the Streamlit header and footer */
    header {display: none;}
    footer {display: none;}
    </style>
    <div class="iframe-container">
        <iframe src="https://snazzy-rolypoly-82b348.netlify.app/" frameborder="0"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)
