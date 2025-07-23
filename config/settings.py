import streamlit as st

def initialize_session_state():
    """Initialize all session state variables"""
    
    if 'bookings' not in st.session_state:
        st.session_state.bookings = []

    if 'availability' not in st.session_state:
        st.session_state.availability = {
            'Monday': {'enabled': True, 'start': '09:00', 'end': '17:00'},
            'Tuesday': {'enabled': True, 'start': '09:00', 'end': '17:00'},
            'Wednesday': {'enabled': True, 'start': '09:00', 'end': '17:00'},
            'Thursday': {'enabled': True, 'start': '09:00', 'end': '17:00'},
            'Friday': {'enabled': True, 'start': '09:00', 'end': '17:00'},
            'Saturday': {'enabled': True, 'start': '08:00', 'end': '16:00'},
            'Sunday': {'enabled': False, 'start': '10:00', 'end': '14:00'}
        }

    if 'coach_info' not in st.session_state:
        st.session_state.coach_info = {
            'name': 'Coach Mike Johnson',
            'email': 'coach@pitchinglessons.com',
            'phone': '(555) 123-4567',
            'bio': 'Former college pitcher with 15+ years coaching experience',
            'rates': '$75 per hour session',
            'payment_methods': 'Cash or Venmo accepted',
            'venmo_handle': '@CoachMike-Baseball'
        }

    if 'testimonials' not in st.session_state:
        st.session_state.testimonials = [
            {'name': 'Sarah Johnson', 'text': 'Coach Mike helped my son improve his fastball velocity by 8 mph in just 2 months!'},
            {'name': 'Tom Rodriguez', 'text': 'Excellent technique instruction and very patient with young players.'},
            {'name': 'Lisa Chen', 'text': 'Professional coaching that really makes a difference. Highly recommended!'}
        ]

# Email configuration (for production use)
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': 'your-email@gmail.com',
    'sender_password': 'your-app-password'  # Use app-specific password for Gmail
}

# Application settings
APP_SETTINGS = {
    'max_booking_days_ahead': 30,
    'session_duration_hours': 1,
    'timezone': 'America/New_York'
}
