import streamlit as st

st.set_page_config(
    page_title="Poms Home",
    page_icon="🏠",
    layout="wide",
    # initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://github.ibm.com/Naoki-Muramoto1/poms/issues",
        "Report a bug": "https://github.ibm.com/Naoki-Muramoto1/poms/issues",
        "About": "# This is a header. This is an *extremely* cool app!",
    },
)


st.title("poms")
