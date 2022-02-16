from random import choice

def get_jokes(joke,unic=False):
    result = []
    if not unic:
        for i in range(joke):
            result.append(choice(nouns) +" "+ choice(adverbs) + " "+ choice(adjectives))
    else:
        while (len(nouns) > 0 and len(adverbs) > 0 and len(adjectives) > 0):
            no = choice(nouns)
            ad = choice(adverbs)
            adj = choice(adjectives)
            result.append(no + " " + ad + " " + adj)
            nouns.remove(no)
            adverbs.remove(ad)
            adjectives.remove(adj)

    return result

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"," зелень","House"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print(get_jokes(500))