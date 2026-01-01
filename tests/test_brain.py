from core.brain import pensar
from core.agent import Agent

def test_brain():
    agent = Agent()

    while True:
        t = input("👶 Tu: ")
        if not t:
            break

        ctx = pensar(t, agent)
        print("🤖 KidBot:", ctx.response_text)
        print("   trace:", ctx.trace)

if __name__ == "__main__":
    test_brain()
