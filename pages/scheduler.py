import streamlit as st
from datetime import datetime, timedelta
import uuid
from utils.email_utils import send_confirmation_email
from utils.calendar_utils import get_available_slots

def show_scheduler_page():
    """Display the main scheduling page"""
    
    st.header("Schedule Your Pitching Lesson")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Select Date & Time")
        
        # Date selection
        min_date = datetime.now().date()
        max_date = min_date + timedelta(days=30)  # Allow booking 30 days in advance
        
        selected_date = st.date_input(
            "Choose a date:",
            min_value=min_date,
            max_value=max_date,
            value=min_date
        )
        
        # Get available slots
        available_slots = get_available_slots(
            selected_date, 
            st.session_state.availability, 
            st.session_state.bookings
        )
        
        if available_slots:
            selected_time = st.selectbox(
                "Choose a time:",
                available_slots,
                format_func=lambda x: x.strftime('%I:%M %p')
            )
        else:
            st.warning("No available slots for this date. Please choose another date.")
            selected_time = None
    
    with col2:
        st.subheader("Your Information")
        
        name = st.text_input("Full Name*", placeholder="Enter your full name")
        email = st.text_input("Email Address*", placeholder="your@email.com")
        phone = st.text_input("Phone Number*", placeholder="(555) 123-4567")
        
        # Additional information
        experience_level = st.selectbox(
            "Experience Level:",
            ["Beginner", "Intermediate", "Advanced", "High School", "College"]
        )
        
        special_requests = st.text_area(
            "Special Requests or Goals:",
            placeholder="Any specific areas you'd like to focus on..."
        )
    
    st.markdown("---")
    
    # Booking summary and confirmation
    if selected_time and name and email and phone:
        show_booking_summary(selected_date, selected_time, name, email, phone, experience_level, special_requests)
    else:
        if selected_time:
            st.info("Please fill in all required fields to complete your booking.")

def show_booking_summary(selected_date, selected_time, name, email, phone, experience_level, special_requests):
    """Display booking summary and handle confirmation"""
    
    booking_datetime = datetime.combine(selected_date, selected_time)
    
    st.subheader("Booking Summary")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Date:**", selected_date.strftime('%A, %B %d, %Y'))
    with col2:
        st.write("**Time:**", selected_time.strftime('%I:%M %p'))
    with col3:
        st.write("**Duration:**", "1 hour")
    
    st.write("**Student:**", name)
    st.write("**Rate:**", st.session_state.coach_info['rates'])
    
    st.info(f"💳 **Payment:** {st.session_state.coach_info['payment_methods']}")
    if 'venmo_handle' in st.session_state.coach_info:
        st.write(f"Venmo: **{st.session_state.coach_info['venmo_handle']}**")
    
    if st.button("📅 Confirm Booking", type="primary"):
        handle_booking_confirmation(
            name, email, phone, booking_datetime, 
            experience_level, special_requests
        )

def handle_booking_confirmation(name, email, phone, booking_datetime, experience_level, special_requests):
    """Process the booking confirmation"""
    
    # Create booking
    booking = {
        'name': name,
        'email': email,
        'phone': phone,
        'datetime': booking_datetime,
        'experience_level': experience_level,
        'special_requests': special_requests,
        'booking_id': str(uuid.uuid4())[:8]
    }
    
    st.session_state.bookings.append(booking)
    
    # Send confirmation email (simulated)
    if send_confirmation_email(booking, st.session_state.coach_info):
        st.success("🎉 Booking confirmed! You will receive a confirmation email shortly.")
        st.balloons()
        
        # Show next steps
        st.markdown("### What's Next?")
        st.write("1. Check your email for confirmation details")
        st.write("2. Add the lesson to your calendar")
        st.write("3. Prepare payment (cash or Venmo)")
        st.write("4. Arrive 10 minutes early with your glove")
        
    else:
        st.error("Booking saved but email notification failed. Please contact the coach directly.")
        st.write(f"**Coach Email:** {st.session_state.coach_info['email']}")
        st.write(f"**Coach Phone:** {st.session_state.coach_info['phone']}")
