# Pitching Lessons Scheduling Website

A professional Streamlit-based scheduling application for baseball pitching lessons. This application allows students to book lessons, coaches to manage availability, and handles email confirmations with calendar invites.

## Features

### For Students/Parents
- **Easy Scheduling**: Select date and time from available slots
- **Group Lessons**: Up to 3 students can book the same time slot
- **Contact Information**: Collect name, email, phone, and experience level
- **Payment Options**: Clear information about cash and Venmo payments
- **Email Confirmations**: Automatic confirmation emails with calendar invites

### For Coaches
- **Availability Management**: Set different hours for each day of the week
- **Booking Overview**: View all current and upcoming bookings
- **Student Information**: Access to all student details and special requests
- **Statistics Dashboard**: Track bookings, revenue, and performance metrics

### Technical Features
- **Multi-slot Booking**: 3 students can book the same time slot for group lessons
- **Calendar Integration**: Generates iCal calendar invites
- **Email Notifications**: Template system for confirmation emails
- **Data Export**: Export bookings and settings for backup
- **Responsive Design**: Works on desktop and mobile devices

## Installation

1. **Clone or download the project files**
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   streamlit run main.py
   ```

4. **Open your browser** to `http://localhost:8501`

## Project Structure

```
pitching-scheduler/
├── main.py                 # Main Streamlit application
├── config/
│   └── settings.py         # Configuration and session state
├── utils/
│   ├── email_utils.py      # Email functionality
│   └── calendar_utils.py   # Calendar and booking utilities
├── pages/
│   ├── scheduler.py        # Main scheduling page
│   ├── about.py           # About/coach information page
│   ├── testimonials.py    # Testimonials page
│   └── admin.py           # Admin panel
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Configuration

### Coach Information
Update the coach details in `config/settings.py`:
- Name, email, phone number
- Bio and coaching experience
- Rates and payment methods
- Venmo handle for payments

### Email Setup (Production)
For production use, configure SMTP settings in `config/settings.py`:
```python
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': 'your-email@gmail.com',
    'sender_password': 'your-app-password'
}
```

### Availability Settings
- Default availability can be set in `config/settings.py`
- Coaches can modify availability through the Admin panel
- Supports different hours for each day of the week

## Usage

### For Students
1. Go to the "Schedule Lesson" tab
2. Select your preferred date and time
3. Fill in your contact information
4. Review booking summary and payment info
5. Confirm your booking

### For Coaches (Admin Panel)
1. Go to the "Admin" tab
2. **Availability**: Set your weekly schedule
3. **Bookings**: View and manage current bookings
4. **Settings**: Update coach information and session settings

## Group Lessons

The system supports up to 3 students per time slot:
- Students can see how many spots are available for each time
- Group lessons are clearly indicated during booking
- Each student books individually but shares the session time

## Payment Handling

The system is designed for offline payments:
- **Cash**: Students pay at the lesson
- **Venmo**: Clear instructions and handle provided
- No online payment processing required

## Production Deployment

### Recommended Next Steps:
1. **Database Integration**: Replace session state with PostgreSQL or SQLite
2. **Email Configuration**: Set up SMTP for actual email sending
3. **Authentication**: Add password protection for admin panel
4. **Domain & Hosting**: Deploy to Streamlit Cloud, Heroku, or similar
5. **SSL Certificate**: Ensure secure connections for customer data

### Hosting Options:
- **Streamlit Cloud**: Free tier available, easy deployment
- **Heroku**: Good for small applications
- **DigitalOcean**: More control, requires setup
- **AWS/Google Cloud**: Enterprise-level hosting

## Customization

### Branding
- Update colors in the Streamlit theme
- Replace placeholder coach photo
- Customize testimonials and success stories

### Functionality
- Modify session duration (currently 1 hour)
- Adjust maximum students per slot (currently 3)
- Add new fields to booking form
- Customize email templates

## Support

For technical issues or customization needs:
1. Check the troubleshooting section below
2. Review the code comments for guidance
3. Consider hiring a developer for advanced modifications

## Troubleshooting

### Common Issues:
- **Import Errors**: Make sure all dependencies are installed
- **Email Not Sending**: Check SMTP configuration and credentials
- **Data Not Persisting**: Session state resets when app restarts
- **Time Zone Issues**: Verify timezone settings in configuration

### Development Mode:
The current setup uses Streamlit's session state for data storage. This means:
- Data resets when the app restarts
- Suitable for testing and development
- For production, implement database storage

## License

This project is provided as-is for educational and commercial use. Modify as needed for your specific requirements.

## Version History

- **v1.0**: Initial release with core scheduling functionality
- **v1.1**: Added group lesson support (3 students per slot)
- **v1.2**: Enhanced admin panel and coach settings
