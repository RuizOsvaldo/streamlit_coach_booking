import streamlit as st
import pandas as pd
from datetime import datetime
from utils.calendar_utils import format_booking_summary, get_upcoming_bookings

def show_admin_page():
    """Display the admin panel"""
    
    st.header("Admin Panel")
    st.write("*Note: In production, this would be password protected*")
    
    # Create admin sub-tabs
    admin_tab1, admin_tab2, admin_tab3 = st.tabs(["📅 Availability", "📋 Bookings", "⚙️ Settings"])
    
    with admin_tab1:
        show_availability_settings()
    
    with admin_tab2:
        show_bookings_management()
    
    with admin_tab3:
        show_coach_settings()

def show_availability_settings():
    """Display and manage availability settings"""
    
    st.subheader("Set Weekly Availability")
    st.write("Configure your available hours for each day of the week.")
    
    for day in st.session_state.availability.keys():
        col1, col2, col3, col4 = st.columns([2, 1, 2, 2])
        
        with col1:
            enabled = st.checkbox(
                day,
                value=st.session_state.availability[day]['enabled'],
                key=f"enabled_{day}"
            )
        
        with col2:
            if enabled:
                st.write("✅ Available")
            else:
                st.write("❌ Closed")
        
        with col3:
            if enabled:
                start_time = st.time_input(
                    "Start",
                    value=datetime.strptime(st.session_state.availability[day]['start'], '%H:%M').time(),
                    key=f"start_{day}"
                )
        
        with col4:
            if enabled:
                end_time = st.time_input(
                    "End",
                    value=datetime.strptime(st.session_state.availability[day]['end'], '%H:%M').time(),
                    key=f"end_{day}"
                )
        
        # Update session state
        st.session_state.availability[day]['enabled'] = enabled
        if enabled:
            st.session_state.availability[day]['start'] = start_time.strftime('%H:%M')
            st.session_state.availability[day]['end'] = end_time.strftime('%H:%M')
    
    if st.button("💾 Save Availability Settings"):
        st.success("Availability settings saved successfully!")

def show_bookings_management():
    """Display and manage current bookings"""
    
    st.subheader("Booking Management")
    
    if not st.session_state.bookings:
        st.info("No bookings yet.")
        return
    
    # Show upcoming bookings
    upcoming = get_upcoming_bookings(st.session_state.bookings, days_ahead=7)
    
    if upcoming:
        st.write("### Upcoming Bookings (Next 7 Days)")
        for booking in upcoming:
            show_booking_card(booking)
        st.markdown("---")
    
    # Show all bookings in table format
    st.write("### All Bookings")
    
    bookings_data = [format_booking_summary(booking) for booking in 
                    sorted(st.session_state.bookings, key=lambda x: x['datetime'])]
    
    bookings_df = pd.DataFrame(bookings_data)
    
    # Add action buttons
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.dataframe(bookings_df, use_container_width=True)
    
    with col2:
        if st.button("📧 Send Reminder Emails"):
            st.info("Reminder emails would be sent to upcoming students")
        
        if st.button("📊 Export Bookings"):
            csv = bookings_df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"bookings_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
    
    # Booking statistics
    show_booking_statistics()

def show_booking_card(booking):
    """Display a single booking in card format"""
    
    col1, col2, col3 = st.columns([2, 2, 1])
    
    with col1:
        st.write(f"**{booking['name']}**")
        st.write(f"📧 {booking['email']}")
        st.write(f"📞 {booking['phone']}")
    
    with col2:
        st.write(f"📅 {booking['datetime'].strftime('%A, %B %d')}")
        st.write(f"🕐 {booking['datetime'].strftime('%I:%M %p')}")
        st.write(f"🎯 {booking['experience_level']}")
    
    with col3:
        if st.button(f"
