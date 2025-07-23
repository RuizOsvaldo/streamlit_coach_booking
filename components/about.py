import streamlit as st

def show_about_page():
    """Display the about page"""
    
    st.header("About Your Coach")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://via.placeholder.com/300x400/4CAF50/FFFFFF?text=Coach+Photo", 
                caption=st.session_state.coach_info['name'])
    
    with col2:
        st.subheader(st.session_state.coach_info['name'])
        st.write(st.session_state.coach_info['bio'])
        
        st.markdown("**Contact Information:**")
        st.write(f"📧 {st.session_state.coach_info['email']}")
        st.write(f"📞 {st.session_state.coach_info['phone']}")
        st.write(f"💰 {st.session_state.coach_info['rates']}")
        st.write(f"💳 **Payment:** {st.session_state.coach_info['payment_methods']}")
        if 'venmo_handle' in st.session_state.coach_info:
            st.write(f"**Venmo:** {st.session_state.coach_info['venmo_handle']}")
    
    st.markdown("---")
    show_coaching_details()

def show_coaching_details():
    """Display detailed coaching information"""
    
    st.subheader("What You'll Learn")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Pitching Mechanics:**
        - Proper grip and release
        - Wind-up and delivery
        - Balance and follow-through
        - Arm slot optimization
        """)
        
        st.markdown("""
        **Physical Development:**
        - Strength and conditioning
        - Flexibility and mobility
        - Injury prevention
        - Velocity development
        """)
    
    with col2:
        st.markdown("""
        **Mental Game:**
        - Focus and concentration
        - Pitch selection strategy
        - Dealing with pressure
        - Confidence building
        """)
        
        st.markdown("""
        **Game Situations:**
        - Working with different counts
        - Pitch sequencing
        - Location and command
        - Situational pitching
        """)
    
    st.markdown("---")
    
    # Training philosophy
    st.subheader("Training Philosophy")
    st.write("""
    Every pitcher is unique, and my coaching approach reflects that. I focus on:
    
    - **Individual Assessment**: Understanding each player's strengths and areas for improvement
    - **Progressive Development**: Building skills systematically from fundamentals to advanced techniques
    - **Mental Resilience**: Developing the mental toughness needed to succeed under pressure
    - **Injury Prevention**: Teaching proper mechanics to ensure long-term health and success
    - **Fun and Engagement**: Keeping sessions enjoyable while maintaining high standards
    """)
    
    # Session structure
    st.subheader("What to Expect in Your Session")
    
    with st.expander("Session Structure (60 minutes)"):
        st.markdown("""
        **Warm-up (10 minutes)**
        - Dynamic stretching and arm care
        - Light throwing progression
        
        **Mechanical Work (30 minutes)**
        - Video analysis if needed
        - Drill work and technique refinement
        - Live throwing with feedback
        
        **Situational Practice (15 minutes)**
        - Game-like scenarios
        - Mental approach discussion
        
        **Cool-down & Summary (5 minutes)**
        - Arm care routine
        - Key takeaways and homework
        """)
    
    # What to bring
    st.subheader("What to Bring")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Required:**
        - Baseball glove
        - Water bottle
        - Athletic clothing
        - Baseball cleats or sneakers
        """)
    
    with col2:
        st.markdown("""
        **Optional:**
        - Personal baseballs (if you have preferences)
        - Notebook for taking notes
        - Any previous coaching feedback
        """)

def show_facility_info():
    """Display facility information"""
    
    st.subheader("Training Facility")
    st.write("""
    Our sessions take place at a professional-grade indoor facility equipped with:
    - Full-length pitching mound
    - Radar gun for velocity tracking
    - Video analysis equipment
    - Climate-controlled environment
    - Ample parking available
    """)
    
    # Add facility location (you can customize this)
    st.write("📍 **Location:** 123 Baseball Drive, Your City, State 12345")
    st.write("🚗 **Parking:** Free parking available on-site")