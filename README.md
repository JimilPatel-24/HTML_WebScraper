# HTML_WebScraper
An AI-powered web scraping platform built with Streamlit and LangChain. Features automated data extraction via Google Gemini, user authentication, and persistent scrape history using Supabase.
BUILT FOR EDUCATIONAL PURPOSES.

AI-Powered Web Scraper & Explorer

A full-stack experiment in combining traditional web scraping techniques with LLM-based data extraction. This project was built to explore the synergy between Python's scraping ecosystem and the Google Gemini AI.

🚀 The Mission:

The goal of this project was to move beyond static data collection. Instead of just saving raw HTML, this app uses LangChain and Google Gemini to "understand" a page and extract specific information based on user prompts.

🛠️ The Learning Stack:

This repository contains my progress in learning the following tools:

    Streamlit: Building the interactive UI and handling session state.

    LangChain & Google Gemini: Powering the "Brain 🧠" layer to parse and structure raw web data.
    
    Selenium: Orchestrates real browser instances to render dynamic content.
    
    BeautifulSoup4: Handling the heavy lifting of HTML parsing and cleaning.

    Supabase: Managing user authentication and providing a persistent PostgreSQL database for scrape history.

    python-dotenv: Managing sensitive API keys securely.

✨ Features

    AI Data Extraction: Don't just scrape; ask questions about the page (e.g., "What are the main product features listed here?").

    Persistent History: Every successful scrape is logged to a Supabase database, allowing you to revisit your findings later.

    User Authentication: A built-in login system to keep your personal scrape history private.

    Clean Parsing: Automated removal of script and style tags to feed the LLM only relevant text content.

🚧 Current Limitations

    JavaScript Blocks: Currently, the app utilizes Basic parsing (BeautifulSoup & Selenium). This means it may encounter "JavaScript Required" messages on highly protected platforms.
    
    Proxy Support: Exploring rotating proxies to handle rate-limiting.

🤝 Acknowledgments

    This project was inspired by a web scraper tool created by TechWithTim. I have significantly modified, secured, and extended the original concept to create a more powerful and reliable platform.

🧠 Project Reflection

  After completing this project, I have gained a high-accuracy grasp of this specific tech stack. Navigating the complexities of Selenium automation and AI orchestration has significantly sharpened my technical confidence.

    
    
