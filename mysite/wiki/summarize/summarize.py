from wiki.summarize.summarization_utils import extract_sentences
from wiki.summarize.keyword_utils import extract_keywords
import sys

def summarize(text):
    print("TEXT", text)

    sentence_extraction = extract_sentences(text, p=0.5)
    combined = " ".join(sentence_extraction)
    keyword_extraction = extract_keywords(combined)

    summary = " ".join([s.capitalize() for s in sentence_extraction])
    keywords = ", ".join(keyword_extraction)

    return summary, keywords

def print_text(text, summary=True):
    if summary:
        print("\nSummary:")
    else:
        print("Keywords:")

    for i in range(len(text)):
        print("[{}] {}".format(i + 1, text[i]))

def main():
    while True:
        print("Enter a text to summarize.\nPlease press 1) Enter 2) CTRL-D to submit.\n>>")
        text = sys.stdin.readlines()

        if text == '':
            break

        summarize(" ".join(text))

if __name__ == "__main__":
    main()