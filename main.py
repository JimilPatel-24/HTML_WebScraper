import os
import streamlit as st
from scrape import scrape_website,extract_body_content,clean_body_content,split_dom_content
from parse import parse_with_gemini
from st_login_form import login_form

#get the login page
client = login_form(allow_guest=False)


if st.session_state.get("authenticated"):
    username = st.session_state.get("username")
    st.success(f"Welcome, {username}!")
    tab1,tab2 = st.tabs(["Web Scraper","Scraping History"])
    with tab1:
        #this tab containes the scraper input/output part

        #Check For Token
        assert os.getenv("GEMINI_API_TOKEN"), "TOKEN NOT LOADED"
        print("token detected")
        
        #intro
        st.title("AI WEBER (HTML BASED AI SCRAPER)")

        #Fetch url as input text
        url = st.text_input("Enter a Website Url:")

        #uses scrape.py functions to clean the DOM content
        if st.button("Scrape Site"):
            with st.spinner(text="Scraping The Website...",show_time=True):
                result = scrape_website(url)
                print(result)    
                body_content = extract_body_content(result)
                cleaned_content = clean_body_content(body_content)
                st.session_state.dom_content = cleaned_content
            with st.expander("View Dom Content"):
                st.text_area("DOM Content",cleaned_content,height=300)

        #uses parse.py to parse the info with help of llm
        if "dom_content" in st.session_state:
            parse_desc = st.text_area("Describe what you want to parse? ")
            if st.button("Parse Content"):
                if parse_desc:
                    with st.status("Using Brains"):
                        st.write("Parsing The Content...")
                        dom_chunks = split_dom_content(st.session_state.dom_content)
                        st.write("Thinking...")
                        result = parse_with_gemini(dom_chunks,parse_desc)
                        st.write("Parsed Content Successfully")
                    if result.strip == parse_desc:
                        st.write("Data Can't Be Processed , Please Check DOM Content For More Info.")
                    else:
                        st.write(result)
                    data = (client.table("scrape_history").insert({"username":username,"url":url,"instruction":parse_desc,"result":result}).execute())
    #history tab 
    with tab2:
        st.header(f"History for {username}")
        fetched_responce = client.table("scrape_history").select("*").eq("username",username).order("created_at",desc=True).execute()
        if fetched_responce.data:
            for i in fetched_responce.data:
                label = f"{i['url']} | {i['created_at'][:10]}"
                with st.expander(label):
                    st.write(f"Instructions Given: {i['instruction']}")
                    st.divider()
                    st.write("Result Obtained: ")
                    st.code(i["result"],language="markdown")
        else:
            st.info("You Haven't Scraped Anything Yet :( )")
    
else:
    st.info("Please log in to use the scraper.")
    
st.markdown("---")
st.markdown(
    "<div style='text-align: right;'>Made with ❤️ by Jimil</div>", 
    unsafe_allow_html=True
)
