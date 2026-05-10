import streamlit as st

try:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

    from supabase import create_client
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    

except Exception as e:
    st.error(f"❌ Supabase connection failed: {e}")
    supabase = None