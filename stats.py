def count_words_(text: str) -> int:
    text_array = text.split()
    word_count = len(text_array)

    return word_count

def count_characters_(text: str) -> dict[str, int]:
    character_hash = dict()
    for c in text:
        c = c.lower()
        if c in character_hash:
            character_hash[c] += 1
        else:
            character_hash[c] = 1
    
    return character_hash

def sort_character_count(character_hash: dict[str, int]) -> list[dict[str, int]]:

    def sort_dict(char_dict):
        return char_dict["num"]
    
    character_count_list = []
    for k in character_hash:
        if k.isalpha():
            character_count_list.append(
                {"char": k,
                "num": character_hash[k]}
            )
    character_count_list.sort(reverse=True, key=sort_dict)

    return character_count_list