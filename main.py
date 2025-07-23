import streamlit as st
from datetime import datetime, timedelta
import pandas as pd
import uuid

from utils.email_utils import send_confirmation_email
from utils.calendar_utils import get_available_slots
from config.settings import initialize_session_state
from pages import about, testimonials, admin, scheduler

# Page configuration
st.set_page_config(
    page_title="Elite Pitching Lessons",
    page_icon="⚾",
    layout="wide"
)

def main():
    # Initialize session state
    initialize_session_state()
    
    st.title("⚾ Elite Pitching Lessons")
    st.markdown("---")
    
    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📅 Schedule Lesson", "👨‍🏫 About", "💬 Testimonials", "⚙️ Admin"])
    
    with tab1:
        scheduler.show_scheduler_page()
    
    with tab2:
        about.show_about_page()
    
    with tab3:
        testimonials.show_testimonials_page()
    
    with tab4:
        admin.show_admin_page()

if __name__ == "__main__":
    main()
