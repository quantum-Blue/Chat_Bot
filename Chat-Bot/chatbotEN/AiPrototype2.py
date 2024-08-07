# Doesn't WORK

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# ChatBot oluşturma
chatbot = ChatBot("SimpleBot")

# Dil modeli eğitimi
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

# Sohbet
print("Bot: Merhaba, benim adım SimpleBot. Size nasıl yardımcı olabilirim?")

while True:
    user_input = input("Siz: ")
    if user_input.lower() == "quit":
        print("Bot: Güle güle!")
        break
    response = chatbot.get_response(user_input)
    print("Bot:", response)

