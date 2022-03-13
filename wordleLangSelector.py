
class URL:
    TR = "https://www.bundle.app/wordle-tr/"
    ENG = "https://www.nytimes.com/games/wordle/index.html"


class Database:
    DATABASE_TR_JSON_1 = "./Databases/TRwordlist.json"
    DATABASE_TR_TXT_BUNDLE = "./Databases/TRwordlist_bundle.txt"
    DATABASE_ENG_TXT_1 = "./Databases/ENGwordlist.txt"
    DATABASE_ENG_TXT_2 = "./Databases/ENGwordlist2.txt"

class FirstWord:
    TR = "sakin"
    ENG = "sores"

def chooseLanguage(lang):
    
    if lang == "TR":
        url = URL.TR
        word_database = Database.DATABASE_TR_JSON_1
        first_word = FirstWord.TR
    elif lang == "ENG":
        url = URL.ENG
        word_database = Database.DATABASE_ENG_TXT_2
        first_word = FirstWord.ENG

    return url, word_database, first_word
