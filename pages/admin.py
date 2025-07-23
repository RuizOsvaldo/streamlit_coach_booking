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
        if st.button(f"Cancel", key=f"cancel_{booking['booking_id']}"):
            if st.button(f"Confirm Cancel", key=f"confirm_cancel_{booking['booking_id']}"):
                st.session_state.bookings = [
                    b for b in st.session_state.bookings 
                    if b['booking_id'] != booking['booking_id']
                ]
                st.success("Booking cancelled")
                st.rerun()
    
    st.markdown("---")

def show_booking_statistics():
    """Display booking statistics"""
    
    if not st.session_state.bookings:
        return
    
    st.subheader("Booking Statistics")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        total_bookings = len(st.session_state.bookings)
        st.metric("Total Bookings", total_bookings)
    
    with col2:
        upcoming_count = len(get_upcoming_bookings(st.session_state.bookings, 30))
        st.metric("Upcoming (30 days)", upcoming_count)
    
    with col3:
        # Calculate revenue (assuming $75 per session)
        total_revenue = total_bookings * 75
        st.metric("Total Revenue", f"${total_revenue}")
    
    with col4:
        # Calculate average bookings per day for available days
        available_days = sum(1 for day_info in st.session_state.availability.values() if day_info['enabled'])
        avg_bookings = round(total_bookings / max(available_days, 1), 1) if available_days > 0 else 0
        st.metric("Avg Bookings/Day", avg_bookings)

def show_coach_settings():
    """Display coach settings and configuration"""
    
    st.subheader("Coach Information Settings")
    
    # Editable coach information
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Coach Name", value=st.session_state.coach_info['name'])
        email = st.text_input("Email", value=st.session_state.coach_info['email'])
        phone = st.text_input("Phone", value=st.session_state.coach_info['phone'])
    
    with col2:
        rates = st.text_input("Rates", value=st.session_state.coach_info['rates'])
        payment_methods = st.text_input("Payment Methods", value=st.session_state.coach_info['payment_methods'])
        venmo_handle = st.text_input("Venmo Handle", value=st.session_state.coach_info.get('venmo_handle', ''))
    
    bio = st.text_area("Bio", value=st.session_state.coach_info['bio'], height=100)
    
    if st.button("💾 Save Coach Settings"):
        st.session_state.coach_info.update({
            'name': name,
            'email': email,
            'phone': phone,
            'rates': rates,
            'payment_methods': payment_methods,
            'venmo_handle': venmo_handle,
            'bio': bio
        })
        st.success("Coach settings saved successfully!")
    
    st.markdown("---")
    
    # Session settings
    st.subheader("Session Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        max_students = st.number_input(
            "Maximum students per time slot",
            min_value=1,
            max_value=10,
            value=3,
            help="How many students can book the same time slot for group lessons"
        )
    
    with col2:
        session_duration = st.selectbox(
            "Session Duration",
            options=[60, 90, 120],
            index=0,
            format_func=lambda x: f"{x} minutes"
        )
    
    # Notification settings
    st.subheader("Notification Settings")
    
    email_notifications = st.checkbox("Send email notifications", value=True)
    reminder_emails = st.checkbox("Send reminder emails 24h before session", value=True)
    
    if st.button("💾 Save Session Settings"):
        st.success("Session settings saved successfully!")
    
    st.markdown("---")
    
    # Data management
    st.subheader("Data Management")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📥 Export All Data"):
            # Create export data
            export_data = {
                'bookings': st.session_state.bookings,
                'availability': st.session_state.availability,
                'coach_info': st.session_state.coach_info,
                'testimonials': st.session_state.testimonials
            }
            st.download_button(
                label="Download JSON Export",
                data=str(export_data),
                file_name=f"pitching_lessons_data_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
    
    with col2:
        if st.button("🗑️ Clear All Bookings", type="secondary"):
            if st.button("⚠️ Confirm Delete All", type="secondary"):
                st.session_state.bookings = []
                st.success("All bookings cleared!")
                st.rerun()
