AI COMPANY BROCHURE GENERATOR
============================

An AI-powered web application that generates professional company
brochures by scraping public company websites and summarizing the
content using Large Language Models (LLMs).


FEATURES
--------
- Scrapes public company websites using BeautifulSoup
- Automatically selects relevant pages (About, Careers, Docs, Blog)
- Generates concise, professional company brochures using AI
- Interactive web interface built with Gradio
- Clean, modular, production-style Python codebase


TECH STACK
----------
- Python
- Gradio
- OpenAI API (default LLM backend)
- BeautifulSoup & Requests for web scraping
- Prompt engineering with structured outputs


PROJECT STRUCTURE
-----------------
company-brochure-generator/
│
├── app.py              # Gradio UI entry point
├── brochure.py         # Brochure generation logic
├── scrapper.py         # Website scraping utilities
├── prompts.py          # System and user prompts
├── requirements.txt    # Project dependencies
└── README.txt


SETUP INSTRUCTIONS
------------------
1. Clone the repository
   git clone https://github.com/barnit07/company-brochure-generator.git
   cd company-brochure-generator

2. Create and activate a virtual environment

   Windows:
   python -m venv .venv
   .venv\Scripts\activate

   macOS / Linux:
   python -m venv .venv
   source .venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Create a .env file
   OPENAI_API_KEY=your_api_key_here


RUNNING THE APPLICATION
-----------------------
python app.py

The Gradio application will start locally and open in the browser.
A temporary public sharing link may also be generated.


USAGE NOTES
-----------
- Best results are obtained using official public company websites
- Login-restricted websites (e.g., LinkedIn) may return limited content


WHY THIS PROJECT
----------------
This project demonstrates:
- End-to-end AI application development
- LLM orchestration and prompt engineering
- Real-world web scraping and data extraction
- Clean software design and modular architecture
- Deployment-ready interactive UI


LICENSE
-------
MIT License
