import streamlit as st

def show_testimonials_page():
    """Display the testimonials page"""
    
    st.header("What Parents & Players Say")
    
    # Display testimonials
    for testimonial in st.session_state.testimonials:
        display_testimonial(testimonial)
    
    st.markdown("---")
    show_success_stories()
    
    st.markdown("---")
    show_call_to_action()

def display_testimonial(testimonial):
    """Display a single testimonial"""
    
    with st.container():
        st.markdown(f"""
        <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; margin: 10px 0;">
            <p style="font-style: italic; margin-bottom: 10px;">"{testimonial['text']}"</p>
            <p style="font-weight: bold; text-align: right;">- {testimonial['name']}</p>
        </div>
        """, unsafe_allow_html=True)

def show_success_stories():
    """Display success stories and achievements"""
    
    st.subheader("Success Stories")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Recent Achievements
        
        🎯 **Velocity Improvements**
        - Average 5-8 mph increase in first 3 months
        - Multiple players reaching 80+ mph
        
        ⚾ **Team Success**
        - 15+ players made varsity teams
        - Several scholarship recipients
        - Multiple all-star selections
        """)
    
    with col2:
        st.markdown("""
        ### Player Development
        
        📈 **Skill Progression**
        - Improved command and control
        - Better pitch selection
        - Enhanced mental approach
        
        🏆 **Recognition**
        - League MVP awards
        - Tournament championships
        - College recruitment interest
        """)

def show_stats_overview():
    """Display coaching statistics"""
    
    st.subheader("Coaching Track Record")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Years Coaching", "15+")
    
    with col2:
        st.metric("Players Trained", "200+")
    
    with col3:
        st.metric("Avg Velocity Gain", "6 mph")
    
    with col4:
        st.metric("College Commits", "25+")

def show_call_to_action():
    """Display call to action section"""
    
    st.subheader("Ready to improve your pitching?")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.write("""
        Join our community of successful pitchers and take your game to the next level! 
        Whether you're just starting out or looking to refine advanced techniques, 
        personalized coaching can make all the difference.
        """)
        
        st.markdown("""
        **What sets us apart:**
        - Individualized training programs
        - Proven track record of success  
        - Focus on both physical and mental development
        - Flexible scheduling to fit your needs
        - Affordable rates with payment flexibility
        """)
    
    with col2:
        if st.button("📅 Schedule Your First Lesson", type="primary", use_container_width=True):
            st.switch_page("Schedule Lesson")
        
        st.markdown("---")
        
        st.markdown("**Quick Contact:**")
        st.write(f"📧 {st.session_state.coach_info['email']}")
        st.write(f"📞 {st.session_state.coach_info['phone']}")

def show_parent_info():
    """Display information specifically for parents"""
    
    st.subheader("Information for Parents")
    
    with st.expander("What parents should know"):
        st.markdown("""
        **Safety First**
        - All training emphasizes proper mechanics to prevent injury
        - Age-appropriate instruction and expectations
        - Regular check-ins about player comfort and progress
        
        **Communication**
        - Progress updates after each session
        - Recommendations for at-home practice
        - Open communication about goals and concerns
        
        **Investment in Development**
        - Focus on long-term skill building, not just quick fixes
        - Teaching fundamentals that will serve players throughout their careers
        - Building confidence and love for the game
        """)

def add_testimonial_form():
    """Form for adding new testimonials (admin use)"""
    
    with st.expander("Add New Testimonial (Admin Only)"):
        new_name = st.text_input("Parent/Player Name")
        new_text = st.text_area("Testimonial Text")
        
        if st.button("Add Testimonial"):
            if new_name and new_text:
                new_testimonial = {'name': new_name, 'text': new_text}
                st.session_state.testimonials.append(new_testimonial)
                st.success("Testimonial added successfully!")
                st.rerun()
            else:
                st.error("Please fill in both fields.")
