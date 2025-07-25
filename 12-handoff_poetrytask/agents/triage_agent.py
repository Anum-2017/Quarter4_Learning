from agents.lyric_analyst import analyze_lyric
from agents.narrative_analyst import analyze_narrative
from agents.dramatic_analyst import analyze_dramatic

def triage(poem: str):
    poem_lower = poem.lower()

    # ✅ 1. First: check for dramatic poem keywords
    if any(word in poem_lower for word in [
        "stage", "curtain", "actor", "monologue", "audience",
        "applause", "spotlight", "mask", "performance", "figure"
    ]):
        return "🎭 Dramatic Analyst", analyze_dramatic

    # ✅ 2. Then: check for lyric poem keywords
    elif any(word in poem_lower for word in [
        "i feel", "my heart", "lonely", "love", "joy", "sorrow",
        "cloud", "breeze", "daffodils", "dream"
    ]):
        return "🎵 Lyric Analyst", analyze_lyric

    # ✅ 3. Then: check for narrative poem keywords
    elif any(word in poem_lower for word in [
        "once", "then", "after", "suddenly", "character", "journey",
        "he", "she", "story"
    ]):
        return "📖 Narrative Analyst", analyze_narrative

    # ✅ 4. Fallback (if nothing matches)
    else:
        return "🎭 Dramatic Analyst", analyze_dramatic



