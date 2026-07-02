try:
    import streamlit as st
except ImportError:
    st = None
    print("Streamlit is not installed. Install it with 'pip install streamlit' to run the dashboard.")
import pandas as pd
import datetime as dt
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go