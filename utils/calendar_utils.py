from datetime import datetime, timedelta
from icalendar import Calendar, Event
import uuid
import pytz

def get_available_slots(selected_date, availability, existing_bookings, max_slots_per_time=3):
    """Get available time slots for a given date with multiple bookings per slot"""
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
        # Count how many bookings exist for this time slot
        bookings_count = sum(
            1 for booking in existing_bookings
            if (booking['datetime'].date() == selected_date and 
                booking['datetime'].time() == current_time.time())
        )
        
        # Add slot if there's still capacity
        if bookings_count < max_slots_per_time:
            slots_remaining = max_slots_per_time - bookings_count
            slots.append({
                'time': current_time.time(),
                'available_spots': slots_remaining,
                'total_spots': max_slots_per_time
            })
        
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

def is_slot_available(date, time, existing_bookings, max_slots_per_time=3):
    """Check if a specific date/time slot has available capacity"""
    booking_datetime = datetime.combine(date, time)
    
    # Count existing bookings for this time slot
    bookings_count = sum(
        1 for booking in existing_bookings
        if booking['datetime'] == booking_datetime
    )
    
    return bookings_count < max_slots_per_time

def get_slot_capacity_info(date, time, existing_bookings, max_slots_per_time=3):
    """Get capacity information for a specific time slot"""
    booking_datetime = datetime.combine(date, time)
    
    bookings_count = sum(
        1 for booking in existing_bookings
        if booking['datetime'] == booking_datetime
    )
    
    return {
        'booked': bookings_count,
        'available': max_slots_per_time - bookings_count,
        'total': max_slots_per_time,
        'is_full': bookings_count >= max_slots_per_time
    }

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
