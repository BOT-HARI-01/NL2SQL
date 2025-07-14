# NL2SQL

A Natural Language to SQL Query Generator

---

## Project Goal

To build an intelligent system that converts natural language queries into optimized SQL queries — capable of handling **complex and large-scale databases** efficiently.

---

## System Featuring

- **Context-Aware Query Generation**  
  Understands the user's database schema and metadata to generate accurate SQL queries.

- **Efficient Token Usage**  
  Optimized for performance with minimal token overhead — suitable for large databases and cost-sensitive use cases.

- **Auto SQL Correction & Execution**  
  Automatically detects, corrects, and executes malformed or partial queries.

- **Interactive Prompting System**  
  Engages the user in a conversation for vague or ambiguous queries, ensuring clarity and better results.

---

### How to run this code
1. Clone the master branch into your local machine `git clone --single-branch --branch master https://github.com/BOT-HARI-01/NL2SQL.git`
2. run `pip install -r requirements.txt`
3. Setting up LLM'
   - Install Ollama & use any models
     1. Install ollama download a model, in `langchain.ipynb` update without model at initilization part
   - Using online llm's
     1. create an `.env` file for adding api keys,
     2. Here we are usign gemini free api so set the variable `GOOGLE_API_KEY` with your api key
4. Copy the `.db` file into the dir and update the import in the `ipynb` file with your file .db filename
 
