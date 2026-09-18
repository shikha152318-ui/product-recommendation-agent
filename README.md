# Product Recommendation + Policy Agent

A simple AI‑powered agent that recommends products and fetches store policies based on user queries.  
Built with **Python, Transformers (Flan‑T5), and REST APIs**.

---

##  Features
- Product recommendations from a local API (`/api/products`)
- Policy lookups (return, exchange, shipping) from `/api/policies`
- Keyword + price filter support (e.g., "jeans under 1000")
- Summarization powered by Hugging Face `flan-t5-large`
- Interactive chat loop for user queries

---

## Tech Stack
- **Python 3.9+**
- **Requests** for API calls
- **Transformers (Hugging Face)** for text generation
- **Flask (backend API)** – assumed running locally
- **Command line interface** for chat

---

## ▶️ How to Run

 **Install dependencies**  
   ```bash
   pip install -r requirements.txt
```
 ---

## Run the Flask Server
python api.py

 ---

## Run the agent
python agent.py

