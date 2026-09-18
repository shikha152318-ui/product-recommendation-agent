# agent.py
import requests
from transformers import pipeline

# --- Call Products API ---
def recommend_api(user_query: str):
    response = requests.get("http://localhost:5000/api/products")
    if response.status_code == 200:
        products = response.json()
        query = user_query.lower()

        results = []
        for p in products:
            name = p.get("name", "").lower()
            category = p.get("category", "").lower()
            price = p.get("price", 0)

            # Match keywords in product name
            if "jeans" in query and "jeans" in name:
                results.append(p)
            elif "t-shirt" in query and "t-shirt" in name:
                results.append(p)
            elif "electronics" in query and category == "electronics":
                results.append(p)
            elif "clothing" in query and category == "clothing":
                results.append(p)

            # Handle price filters
            if ("under" in query or "less than" in query) and any(word.isdigit() for word in query.split()):
                try:
                    limit = int([word for word in query.split() if word.isdigit()][0])
                    if price <= limit:
                        results.append(p)
                except:
                    pass

        return results if results else [{"message": "No products found"}]
    return [{"error": "API failed"}]


# --- Call Policies API ---
def fetch_policy(user_query: str):
    response = requests.get("http://localhost:5000/api/policies")
    if response.status_code == 200:
        policies = response.json()
        if "return" in user_query.lower():
            return policies.get("return_policy")
        elif "exchange" in user_query.lower():
            return policies.get("exchange_policy")
        elif "shipping" in user_query.lower():
            return policies.get("shipping_policy")
        else:
            # If user didn't ask for a policy, return None
            return None
    return None


# --- LLM Summarizer ---
summarizer = pipeline("text2text-generation", model="google/flan-t5-large")

# --- Helper function ---
def format_products(products):
    if not products:
        return "No products found."
    formatted = []
    for p in products:
        formatted.append(
            f"- {p.get('name')} ({p.get('brand')}) – ₹{p.get('price')} | Rating: {p.get('rating')} | {p.get('description')}"
        )
    return "\n".join(formatted)



def generate_response(user_query: str):
    products = recommend_api(user_query)
    policy = fetch_policy(user_query)

    product_text = format_products(products)

    final_answer = f"Here are the products matching your query:\n{product_text}"

    if policy:  # Only show if user asked
        final_answer += f"\n\nPolicy Info:\n{policy}"

    return final_answer


# --- Chat Loop ---
if __name__ == "__main__":
    print("Product Recommendation + Policy Agent Ready! Type 'exit' to quit.")
    while True:
        user_query = input("Ask your question: ")
        if user_query.lower() == "exit":
            break
        print("Agent:", generate_response(user_query))
