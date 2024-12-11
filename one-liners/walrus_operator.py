"""
Walrus operator looks like this below. Introduced in python 3.8
`:=`
Source: https://www.youtube.com/watch?v=MEMDi9mTCiU&t=249s
"""


def analyze_text(text: str) -> dict:
    """
    here below the code
        `
            "words": (words := text.split())
        `
    replaces this code:
        `
            words = text.split()
            "words" = words
        `
    """
    details: dict = {
        "words": (words := text.split(",")),
        "total_words": len(words),
        "total_chars": len("".join(words)),
        "reversed_words": [x[::-1] for x in words],
        "List_reversed": words[::-1],
    }
    return details


def check_eligibility(age: float) -> str:
    if (age := round(age)) >= 18:
        return f"Age: {age} is eligible"
    return f"Age: {age} is not eligible"


print(analyze_text("Jairam, Sairam"))
print(check_eligibility(20.3))
