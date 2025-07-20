import json
import difflib

# Load FAQs
with open('data/faq.json', 'r') as f:
    faq_data = json.load(f)

def get_answer(user_question):
    questions = [faq['question'] for faq in faq_data]
    best_match = difflib.get_close_matches(user_question, questions, n=1, cutoff=0.5)

    if best_match:
        for faq in faq_data:
            if faq['question'] == best_match[0]:
                return faq['answer']
    return "Sorry, I couldn't find an answer to that. Please try asking differently."
