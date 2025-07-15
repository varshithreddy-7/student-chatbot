import json

# Load the FAQs from JSON
with open("data/faq.json", "r") as file:
    faq_data = json.load(file)

def get_bot_response(user_input):
    user_input = user_input.lower()

    for item in faq_data:
        for keyword in item["question_keywords"]:
            if keyword in user_input:
                return item["answer"]

    return "Sorry, I don't understand that yet. Try asking about internships, CGPA, resume, or DSA."
