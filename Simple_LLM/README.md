# Simple FastAPI for Q&A LLM System  
To activate your virtual environment, install dependencies and build the app, run the following commands in your terminal. I used venv, you can also use conda or others. 

# install the virtual environment package
pip install virtualenv
# create the virtual environmnet
python3 -m venv first_llm
# activate the virtual environmnet (linux)
source first_llm/bin/activate
# install all requirements
pip install -r requirements.txt
# run a simple app and print response on terminal
python3 simple.py
# to create api endpoints, expose and test them out 
uvicorn app:app --host 127.0.0.1 --port 5000 --reload
# Request body for testing in Postman
    {
        "question": "which is bigger? 9.11 or 9.9?",
        "model": "llama-3.1-8b-instant",
        "temperature": 0.2
    }
