import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import streamlit as st
from config.settings import EMAIL_CONFIG

def create_email_body(booking_info, coach_info):
    """Create the email body for booking confirmation"""
    
    subject = f"Pitching Lesson Confirmation - {booking_info['datetime'].strftime('%B %d, %Y at %I:%M %p')}"
    
    body = f"""
Dear {booking_info['name']},

Your pitching lesson has been confirmed!

Lesson Details:
Date: {booking_info['datetime'].strftime('%A, %B %d, %Y')}
Time: {booking_info['datetime'].strftime('%I:%M %p')}
Duration: 1 hour
Coach: {coach_info['name']}
Rate: {coach_info['rates']}

Coach Contact Information:
Email: {coach_info['email']}
Phone: {coach_info['phone']}

Payment Information:
{coach_info['payment_methods']}
Venmo: {coach_info.get('venmo_handle', 'Ask coach for details')}

Please arrive 10 minutes early and bring your glove and water bottle.

Best regards,
{coach_info['name']}
    """
    
    return subject, body

def create_coach_notification_email(booking_info, coach_info):
    """Create email notification for the coach"""
    
    subject = f"New Booking: {booking_info['name']} - {booking_info['datetime'].strftime('%B %d, %Y at %I:%M %p')}"
    
    body = f"""
New Pitching Lesson Booking!

Student Details:
Name: {booking_info['name']}
Email: {booking_info['email']}
Phone: {booking_info['phone']}
Experience Level: {booking_info['experience_level']}

Lesson Details:
Date: {booking_info['datetime'].strftime('%A, %B %d, %Y')}
Time: {booking_info['datetime'].strftime('%I:%M %p')}
Duration: 1 hour

Special Requests:
{booking_info['special_requests'] if booking_info['special_requests'] else 'None'}

Booking ID: {booking_info['booking_id']}
    """
    
    return subject, body

def send_confirmation_email(booking_info, coach_info):
    """
    Send confirmation email to student and notification to coach
    Note: This is a template - in production you'd need to configure SMTP
    """
    
    try:
        # In a real implementation, you would:
        # 1. Set up SMTP connection
        # 2. Create email with calendar invite
        # 3. Send to both student and coach
        
        # For now, we'll simulate successful email sending
        student_subject, student_body = create_email_body(booking_info, coach_info)
        coach_subject, coach_body = create_coach_notification_email(booking_info, coach_info)
        
        # Simulate email sending
        print(f"Email sent to {booking_info['email']}: {student_subject}")
        print(f"Notification sent to {coach_info['email']}: {coach_subject}")
        
        return True
        
    except Exception as e:
        print(f"Email sending failed: {str(e)}")
        return False

def send_email_smtp(to_email, subject, body, attachment=None):
    """
    Production-ready email sending function
    Uncomment and configure for actual email sending
    """
    
    # Uncomment below for production use:
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['sender_email']
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        if attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment)
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                'attachment; filename= calendar_invite.ics'
            )
            msg.attach(part)
        
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
        text = msg.as_string()
        server.sendmail(EMAIL_CONFIG['sender_email'], to_email, text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"SMTP Error: {str(e)}")
        return False
    """
    pass
