import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Human Post Editor Tool", page_icon="📝", layout="wide")

st.title("📝 Gemini Human-Style Blog Post Editor")
st.write("Apni AI ya raw post yahan paste karein aur ise humanized, SEO-optimized blog post me badlein.")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    raw_content = st.text_area("Yahan apni post paste karein:", height=300)
    
    if st.button("Edit & Humanize Post"):
        if raw_content.strip():
            with st.spinner("Post ko human style me edit kiya ja raha hai..."):
                prompt = f"""
                You are an expert professional blog editor. 
                Re-write and edit the following blog post to make it sound 100% written by a knowledgeable human blogger.

                Guidelines for Editing:
                1. Language & Tone: Natural, engaging, and conversational Hindi. Avoid AI jargon like 'nishkarsh', 'iske ilawa', 'gahan adhyayan'.
                2. Structure: Use proper HTML tags (<h2>, <h3>, <strong>, <ul>, <li>).
                3. Formatting: Make short 2-3 line paragraphs. Add a highlighted 'Key Takeaways' box at the top.
                4. Human Touch: Add relatable examples, rhetorical questions, and smooth transitions.
                5. SEO: Naturally retain core topics and keywords without keyword stuffing.

                Original Post Content:
                {raw_content}
                """
                
                model = genai.GenerativeModel('gemini-2.5-flash')
                response = model.generate_content(prompt)
                
                st.subheader("✨ Edited Output:")
                st.markdown(response.text)
                
                st.subheader("📋 Raw HTML Code (Copy-Paste for Blogger):")
                st.code(response.text, language='html')
        else:
            st.error("Kripya edit karne ke liye content darj karein!")
else:
    st.info("Shuru karne ke liye sidebar me apni Gemini API Key dalein.")
