import textwrap
from agents.poet_agent import generate_poem
from agents.triage_agent import triage
import handoff

def main():
    title, poem = generate_poem()

    print("\n📜 Your Poem:\n")
    print(f"\n📝 Title: {title}\n")
    print(poem)

    print("\n📊 Analyzing your poem...\n")

    agent_name, analysis_fn = triage(poem)
    analysis = handoff.handoff(poem, analysis_fn)

    wrapped_analysis = textwrap.fill(analysis, width=80)
    print(wrapped_analysis)

    print(f"\n🤖 Last Agent Used: {agent_name}\n")

if __name__ == "__main__":
    main()

