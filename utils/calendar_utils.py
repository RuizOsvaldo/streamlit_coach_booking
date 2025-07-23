from datetime import datetime, timedelta
from icalendar import Calendar, Event
import uuid
import pytz

def get_available_slots(selected_date, availability, existing_bookings):
    """Get available time slots for a given date"""
    day_name = selected_date.strftime('%A')
    
    if not availability[day_name]['enabled']:
        return []
    
    start_time = datetime.strptime(availability[day_name]['start'], '%H:%M').time()
    end_time = datetime.strptime(availability[day_name]['end'], '%H:%M').time()
    
    # Generate hourly slots
    slots = []
    current_time = datetime.combine(selected_date, start_time)
    end_datetime = datetime.combine(selected_date, end_time)
    
    while current_time < end_datetime:
        # Check if slot is already booked
        is_booked = any(
            booking['datetime'].date() == selected_date and 
            booking['datetime'].time() == current_time.time()
            for booking in existing_bookings
        )
        
        if not is_booked:
            slots.append(current_time.time())
        
        current_time += timedelta(hours=1)
    
    return slots

def create_calendar_invite(booking_info, coach_info):
    """Create an iCal calendar invite"""
    cal = Calendar()
    cal.add('prodid', '-//Pitching Lessons Scheduler//mxm.dk//')
    cal.add('version', '2.0')
    
    event = Event()
    event.add('summary', f'Pitching Lesson with {coach_info["name"]}')
    event.add('dtstart', booking_info['datetime'])
    event.add('dtend', booking_info['datetime'] + timedelta(hours=1))  # 1-hour sessions
    event.add('dtstamp', datetime.now())
    event.add('uid', str(uuid.uuid4()))
    
    description = f"""
Pitching Lesson Details:
Student: {booking_info['name']}
Email: {booking_info['email']}
Phone: {booking_info['phone']}
Coach: {coach_info['name']}
Rate: {coach_info['rates']}
Payment: {coach_info['payment_methods']}

Please bring payment in cash or send via Venmo to {coach_info.get('venmo_handle', 'TBD')} after the lesson.
    """
    event.add('description', description)
    event.add('location', 'Pitching Facility')
    
    cal.add_component(event)
    return cal.to_ical()

def is_slot_available(date, time, existing_bookings):
    """Check if a specific date/time slot is available"""
    booking_datetime = datetime.combine(date, time)
    
    return not any(
        booking['datetime'] == booking_datetime
        for booking in existing_bookings
    )

def get_upcoming_bookings(bookings, days_ahead=7):
    """Get bookings for the next N days"""
    now = datetime.now()
    future_date = now + timedelta(days=days_ahead)
    
    upcoming = [
        booking for booking in bookings
        if now <= booking['datetime'] <= future_date
    ]
    
    return sorted(upcoming, key=lambda x: x['datetime'])

def format_booking_summary(booking):
    """Format booking information for display"""
    return {
        'Date': booking['datetime'].strftime('%Y-%m-%d'),
        'Time': booking['datetime'].strftime('%I:%M %p'),
        'Student': booking['name'],
        'Email': booking['email'],
        'Phone': booking['phone'],
        'Level': booking['experience_level'],
        'ID': booking['booking_id']
    }
