from summarization_utils import extract_sentences
from keyword_utils import extract_keywords
import sys

def summarize(text):
    sentence_extraction = extract_sentences(text)
    combined = " ".join(sentence_extraction)
    keyword_extraction = extract_keywords(combined)

    print_text(sentence_extraction, summary=True)
    print_text(keyword_extraction, summary=False)

def print_text(text, summary=True):
    if summary:
        print("Summary:")
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