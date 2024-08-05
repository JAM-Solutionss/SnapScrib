import streamlit as st
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from backend.config.css import load_css

# Pages
home = st.Page(
    "frontend/pages/home.py",
    title="Home",
    icon=":material/home:"
)

about = st.Page(
    "frontend/pages/about.py",
    title="About",
    icon=":material/info:"
)

# Navigation
pg = st.navigation({"Menu": [home, about]})

pg.run()