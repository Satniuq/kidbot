from core.brain import pensar

while True:
    t = input("👶 Tu: ")
    if not t:
        break

    print("🤖 KidBot:", pensar(t))

