import json
import difflib

DATABASE_FILE_PATH = '/Users/enesbal/Desktop/smart-chatbot/Database.json'

def load_database():
    with open(DATABASE_FILE_PATH, 'r') as File:
        return json.load(File)

def write_database(datas):
    with open(DATABASE_FILE_PATH, 'w') as File:
        json.dump(datas, File, indent=2)

def find_close_match(prompt, prompts):
    compatible_datas = difflib.get_close_matches(prompt, prompts, n=1, cutoff=0.6)
    return compatible_datas[0] if compatible_datas else None

def find_answer(prompt, Database):
    for question_answers in Database["prompts"]:
        if question_answers["prompt"] == prompt:
            return question_answers["answer"]
    return None

def chat_bot():
    Database = load_database()

    while True:
        prompt = input('Your: ')

        if prompt.lower() in ['out', 'çık']:
            break

        incoming_result = find_close_match(prompt, [question_answers["prompt"] for question_answers in Database["prompts"]])

        if incoming_result:
            answer_given = find_answer(prompt, Database)
            print(f"Bot: {answer_given}")
        else:
            print("Bot: Bunu nasıl cevaplayacağımı bilmiyorum. Öğretir misiniz? ")
            new_answer = input("Öğretmek için yazabilirsiniz veya 'geç' ya da 'pass' diyebilirsiniz. ")
            if new_answer.lower() not in ['geç', 'pass']:
                Database["prompts"].append({
                    "prompt": prompt,
                    "answer": new_answer
                })
                write_database(Database)
                print("Bot: Teşekkürler, sayenizde yeni bilgiler öğrendim. ")

if __name__ == '__main__':
    chat_bot()


"""import json
import difflib

def load_database():
    with open('/Users/enesbal/Desktop/smart-chatbot/Database.json','r') as File:
        return json.load(File)

def write_database(datas):
    with open('/Users/enesbal/Desktop/smart-chatbot/Database.json','w') as File:
        json.dump(datas,File,indent=2)


def find_close_match(prompt,prompts):
    compatible_datas=difflib.get_close_matches(prompt,prompts,n=1,cutoff=0.6)
    # compatible data: eşleşen veriler
    # get_close_matches: input, liste, kaç değer dödüreceği, yüzde kaç eşleşiyosa döndürsün

    return compatible_datas[0] if compatible_datas else None

def find_answer(prompt,Database):
    for question_answers in Database[prompt]:
        if question_answers["prompt"] == prompt:
            return question_answers["answer"]
    return None


def chat_bot():
    Database=load_database()

    while True:
        prompt=input('Your: ')

        if (prompt == ('out' or 'çık')):
            break

        incoming_result=find_close_match(prompt,[question_answers["prompt"] for question_answers in Database["prompts"]])

        if incoming_result:
            answer_given=find_answer(prompt,Database)
            print(f"Bot: {answer_given}")
        else:
            print("Bot: Bunu nasıl cevaplayacağımı bilmiyorum. Öğretir misiniz? ")
            new_answer=input("Öğretmek için yazabilirsiniz veya 'geç' ya da 'pass' diyebilirsiniz. ")
            if new_answer != 'geç' or 'pass':
                Database["prompts"].append({
                    "prompt":prompt,
                    "answer":new_answer
                })
                write_database(Database)
                print("Bot: Teşekkürler, sayenizde yeni bilgiler öğrendim. ")

if __name__ == '__main__' :
    chat_bot()    

"""