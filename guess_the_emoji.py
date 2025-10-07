import random

def guess_the_emoji():
    emojis = {
        "😀": "A common symbol for happiness",
        "🔥": "Something very cool or hot",
        "❤️": "Used to express love",
        "☕": "Something you drink in the morning",
        "🌧️": "Weather with clouds and water",
        "🎮": "Used for playing video games",
        "📚": "Used by students for studying",
        "🐍": "A type of reptile and also a programming language"
    }

    print("🎯 Welcome to 'Guess the Emoji' Game!")
    print("You have 3 chances to guess each emoji name correctly.\n")
    
    score = 0
    rounds = 5

    for i in range(rounds):
        emoji, hint = random.choice(list(emojis.items()))
        print(f"Round {i+1}/{rounds}")
        print(f"Hint: {hint}")
        
        for attempt in range(3, 0, -1):
            guess = input(f"Your guess ({attempt} tries left): ").strip().lower()
            if guess in emoji_name(emoji):
                print(f"✅ Correct! The emoji was {emoji}\n")
                score += 1
                break
            else:
                print("❌ Wrong guess!")
        else:
            print(f"😅 Out of tries! The correct emoji was {emoji}\n")

    print(f"🏁 Game Over! Your final score: {score}/{rounds}")

def emoji_name(emoji):
    mapping = {
        "😀": ["smile", "happy", "grin"],
        "🔥": ["fire", "lit", "hot"],
        "❤️": ["heart", "love"],
        "☕": ["coffee", "tea"],
        "🌧️": ["rain", "rainy", "cloud"],
        "🎮": ["game", "controller"],
        "📚": ["book", "study", "reading"],
        "🐍": ["snake", "python"]
    }
    return mapping.get(emoji, [])

if __name__ == "__main__":
    guess_the_emoji()
