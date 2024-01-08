import time
import random

def typing_test(word_list):
    correct_words = 0
    total_words = 0
    start_time = time.time()

    shuffled_words = list(word_list.values())
    random.shuffle(shuffled_words)

    for word in shuffled_words[:5]:
        total_words += 1
        user_input = input(f"Type the word {total_words}/5: '{word}': ")

        if user_input.lower() == "stop":
            print("Typing test stopped.")
            break

        if user_input == word:
            correct_words += 1

    end_time = time.time()

    accuracy = (correct_words / total_words) * 100
    elapsed_time = end_time - start_time
    words_per_minute = (total_words / elapsed_time) * 60

    print("\nTyping Test Results:")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Typing Speed: {words_per_minute:.2f} words per minute")

# Sample word lists (you can replace them with your own)

easy_words = {
    1: "tap",
    2: "wet",
    3: "gap",
    4: "day",
    5: "jet",
    6: "dig",
    7: "sky",
    8: "hot",
    9: "rat",
    10: "kit",
    11: "sad",
    12: "few",
    13: "how",
    14: "lap",
    15: "fry",
    16: "rug",
    17: "wed",
    18: "law",
    19: "dot",
    20: "far",
    21: "joy",
    22: "lug",
    23: "ray",
    24: "key",
    25: "tag",
    26: "hut",
    27: "owl",
    28: "jug",
    29: "aid",
    30: "raw",
    31: "rip",
    32: "cup",
    33: "lid",
    34: "beg",
    35: "nap",
    36: "hop",
    37: "gem",
    38: "lip",
    39: "sip",
    40: "rug",
    41: "toy",
    42: "job",
    43: "mud",
    44: "wag",
    45: "jog",
    46: "cup",
    47: "top",
    48: "pen",
    49: "lip",
    50: "sad",
    51: "hot",
    52: "rag",
    53: "kit",
    54: "jug"
}

medium_words = {
    1: "task",
    2: "weep",
    3: "glad",
    4: "days",
    5: "jest",
    6: "disk",
    7: "skip",
    8: "host",
    9: "rate",
    10: "kite",
    11: "said",
    12: "fuel",
    13: "show",
    14: "leap",
    15: "fray",
    16: "rugs",
    17: "weds",
    18: "laws",
    19: "dots",
    20: "farm",
    21: "joys",
    22: "lugs",
    23: "rays",
    24: "keys",
    25: "tags",
    26: "huts",
    27: "owls",
    28: "jugs",
    29: "aids",
    30: "raws",
    31: "ripe",
    32: "cups",
    33: "lids",
    34: "begs",
    35: "naps",
    36: "hops",
    37: "gems",
    38: "lips",
    39: "sips",
    40: "rugs",
    41: "toys",
    42: "jobs",
    43: "muds",
    44: "wags",
    45: "jogs",
    46: "cups",
    47: "tops",
    48: "pens",
    49: "lips",
    50: "sads",
    51: "hots",
    52: "rags",
    53: "kits",
    54: "jugs"
}

hard_words = {
    1: "tasks",
    2: "weeps",
    3: "glads",
    4: "diary",
    5: "jests",
    6: "disks",
    7: "skips",
    8: "hosts",
    9: "rated",
    10: "kites",
    11: "sired",
    12: "fuels",
    13: "shown",
    14: "leaps",
    15: "frays",
    16: "rugsy",
    17: "wedsy",
    18: "lawsy",
    19: "dotty",
    20: "farms",
    21: "joysy",
    22: "lugsy",
    23: "raysy",
    24: "keysy",
    25: "tagsy",
    26: "hutsy",
    27: "owlsy",
    28: "jugsy",
    29: "aidsy",
    30: "rawsy",
    31: "riped",
    32: "cupsy",
    33: "lidsy",
    34: "begsy",
    35: "napsy",
    36: "hopsy",
    37: "gemsy",
    38: "lipsy",
    39: "sipsy",
    40: "rugsy",
    41: "toysy",
    42: "jobsy",
    43: "mudsy",
    44: "wagsy",
    45: "jogsy",
    46: "cupsy",
    47: "topsy",
    48: "pensy",
    49: "lipsy",
    50: "sadsy",
    51: "hotsy",
    52: "ragsy",
    53: "kitsy",
    54: "jugsy"
}

common_words = {
    1: "the", 2: "and", 3: "you", 4: "was", 5: "that", 6: "with", 7: "for", 8: "are", 9: "have", 10: "this",
    11: "not", 12: "but", 13: "can", 14: "all", 15: "from", 16: "there", 17: "some", 18: "what", 19: "when", 20: "where",
    21: "which", 22: "they", 23: "said", 24: "one", 25: "about", 26: "out", 27: "like", 28: "time", 29: "into", 30: "has",
    31: "day", 32: "more", 33: "could", 34: "two", 35: "who", 36: "him", 37: "see", 38: "its", 39: "now", 40: "my",
    41: "over", 42: "just", 43: "than", 44: "other", 45: "would", 46: "make", 47: "first", 48: "up", 49: "people", 50: "know",
    51: "use", 52: "each", 53: "very", 54: "your"
}


print("Easy Typing Test:")
typing_test(easy_words)

print("\nMedium Typing Test:")
typing_test(medium_words)

print("\nHard Typing Test:")
typing_test(hard_words)

print("\ncommon_words :")
typing_test(common_words)

