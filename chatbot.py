import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt', quiet=True)
class AdmissionChatBot:
    def __init__(self):
        self.ps = PorterStemmer()
        self.load_knowledge_base("knowledge_base.json")
        self.context = {}
    def load_knowledge_base(self, filepath):
        with open(filepath, encoding='utf-8') as f:
            self.knowledge = json.load(f)
    def preprocess(self, text):
        tokens = word_tokenize(text.lower())
        return [self.ps.stem(t) for t in tokens if t.isalnum()]
    def match_intent(self, query):
        tokens = self.preprocess(query)
        intent_keywords = {
    "deadlines": ["deadlin", "last", "date", "close", "due"],
    "eligibility": ["eligib", "qualif", "criteria", "require"],
    "fees": ["fee", "tuit", "cost", "price", "charg", "amount", "₹", "rs"],
    "contact": ["contact", "email", "phone", "reach", "helpdesk"],
    "programs": ["program", "course", "mca", "special", "subject", "field"],
    "installments": ["install", "payment", "emi", "split", "part", "plan"],
    "uniform": ["uniform", "dress", "code", "attire", "clothing"],
    "timings": ["timing", "hour", "schedul", "start", "end", "class", "duration"],
    "specialization": ["special", "stream", "focus", "electiv", "domain"],
    "cultural": ["cultur", "event", "fest", "celebr", "function", "activity"],
    "sports": ["sport", "game", "athlet", "match", "team", "tournament"],
    "campus": ["campus", "facil", "infrastructur", "build", "ground", "wifi"],
    "internships": ["intern", "train", "experi", "project", "industry"],
    "placements": ["placement", "job", "career", "recruit", "opportun"],
    "location": ["locat", "place", "address", "situat", "where"],
    "hostel": ["hostel", "accommod", "room", "stay", "dorm"],
    "canteen": ["canteen", "food", "mess", "dining", "eat"]
}

        for intent, keywords in intent_keywords.items():
            if any(word in tokens for word in keywords):
                return intent
        return None
    def generate_response(self, intent):
        if intent in self.knowledge:
            return self.knowledge[intent]
        return "I am here to help with MCA admissions – ask me about fees, eligibility, programs, campus facilities, placements,installments,uniform,timings,specification,cultural,sports,internships,location,hostel,canteen!"

    def handle_query(self, query):
        intent = self.match_intent(query)
        print(f"Detected intent: {intent}")  
        response = self.generate_response(intent)
        self.log_conversation(query, response, intent)
        return response
    def log_conversation(self, query, response, intent):
        with open("conversation_log.txt", "a", encoding='utf-8') as f:
            f.write(f"User: {query}\nIntent: {intent}\nBot: {response}\n\n")
knowledge_base = {
    "deadlines": "MCA admissions close on September 30, 2025. Late applications are accepted until October 15 with a late fee.",
    "eligibility": "Eligibility: Bachelor's degree with at least 50% marks and a valid entrance exam score.",
    "fees": "The total tuition fee is ₹1,20,000 per year. Scholarships are offered to the top 10% scorers.",
    "contact": "Email: mcaadmissions@spcputtur.ac.in | Phone: +91-9480010171",
    "programs": "We offer MCA programs with specializations in Artificial Intelligence, Cybersecurity, and Data Science.",
    "installments": "You will be given 2 installments to pay the yearly fee.",
    "uniform": "Yes, wearing the college uniform is mandatory on all working days.",
    "timings": "College operates from 9:00 AM to 4:00 PM, Monday to Friday.",
    "specialization": "MCA specializations include Artificial Intelligence, Cybersecurity, and Data Science.",
    "cultural": "Cultural activities such as fests, ethnic days, and talent shows are organized regularly.",
    "sports": "The college provides facilities for cricket, football, badminton, and indoor games.",
    "campus": "Our campus includes a digital library, computer labs, auditoriums, Wi-Fi, and green spaces.",
    "internships": "Internships are provided in collaboration with industry partners during the final semester.",
    "placements": "Top companies like Infosys, Wipro, and TCS recruit from our campus annually.",
    "location": "The college is located in Puttur, Karnataka, near the city center and easily accessible.",
    "hostel": "Separate hostels for boys and girls with Wi-Fi, 24x7 security, and hygienic food.",
    "canteen": "The canteen serves affordable and nutritious meals and snacks throughout the day."
}

if __name__ == "__main__":
    with open("knowledge_base.json", "w", encoding='utf-8') as f:
        json.dump(knowledge_base, f, ensure_ascii=False, indent=4)
    bot = AdmissionChatBot()
    print("Admission Bot: Hi! Ask me about MCA admissions (type 'quit' to exit)\n")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ['quit', 'exit']:
            print("Bot: Thank you! Feel free to reach out for more help.")
            break
        print("Bot:", bot.handle_query(user_input))
