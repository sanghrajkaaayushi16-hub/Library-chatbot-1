import streamlit as st
print("===================================")
print("       LIBRARY CHATBOT")
print("===================================")
print("Welcome to the Library Help Desk!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Welcome to the Library Help Desk.")

    elif "timing" in user or "hours" in user or "open" in user:
        print("Bot: Our library is open from 9:00 AM to 5:00 PM.")

    elif "book" in user and ("available" in user or "availability" in user):
        print("Bot: Please provide the book title to check its availability.")

    elif "issue" in user or "borrow" in user:
        print("Bot: You can borrow up to 3 books using your library card.")

    elif "return" in user:
        print("Bot: Please return your books to the library counter.")

    elif "fine" in user or "late" in user:
        print("Bot: A late return fine may apply to overdue books.")

    elif "membership" in user or "library card" in user:
        print("Bot: Visit the library desk to register for membership.")

    elif "location" in user or "where" in user:
        print("Bot: The library is located inside the college campus.")

    elif "thank" in user:
        print("Bot: You're welcome! Happy reading.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I didn't understand. Please ask about library timings, books, membership, issuing, or returns.")

print("\nThank you for using the Library Chatbot!")
