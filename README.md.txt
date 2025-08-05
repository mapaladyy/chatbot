




 🤖 MCA Admission Chatbot

  A terminal-based chatbot built with Python and NLTK to answer questions related to MCA admissions (fees, eligibility, deadlines, placements, etc.).


 Features

  * Intent-based natural language understanding
  * Covers multiple MCA admission topics
  * Uses stemming for flexible keyword matching
  * Loads responses from an external JSON knowledge base
  * Logs user queries and bot responses to a log file



 Tech Stack

Language: Python 3.x
Libraries:`nltk`, `json`
NLP Techniques Used:

  * Tokenization (`nltk.word_tokenize`)
  * Stemming (`PorterStemmer`)



Installation Guide
  Clone the repository

 Create a virtual environment *(optional but recommended)*

 Install required Python packages

  pip install nltk




Running the Bot


python chatbot.py


 Example Interaction:

```
Admission Bot: Hi! Ask me about MCA admissions (type 'quit' to exit)
You: What are the fees?
Bot: The total tuition fee is ₹1,20,000 per year...
```

To exit:

```bash
quit
```


Logging System

* Chat logs are saved to: `conversation_log.txt`
* Includes:
* User query
* Detected intent
* Bot response

License

This project is free and open source


