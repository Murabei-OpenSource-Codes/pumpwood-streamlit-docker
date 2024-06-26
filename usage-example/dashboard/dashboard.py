import os
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
from pumpwood_streamlit.dashboard import PumpwoodStreamlitDashboard


class Dashboard(PumpwoodStreamlitDashboard):
    def set_page_config(self):
        #######################
        # Page configuration
        st.set_page_config(
            page_title="US Population Dashboard",
            page_icon="🏂",
            layout="wide",
            initial_sidebar_state="expanded")

    def main_view(self):
        alt.themes.enable("dark")

        #######################
        # Load data
        st.title('O dash mudou!')
