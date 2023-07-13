# **Extractive Text Summarization**

This project is a **TextRank** implementation of [Samizadah (2022)](https://arxiv.org/pdf/2212.09701.pdf). It also takes some code and inspiration from [here](https://github.com/summanlp/textrank/blob/master/summa/keywords.py).

Read the full report at `report.pdf`

## **How to Use**

### _Dependencies_

`spaCy` and its English model `en_core_web_md` are necessary dependencies.

### _Run the Python script_

To run the summarizer, enter the following command in the Terminal:

    python summarize.py

### _Entering Text_

Once the python script is run, a prompt will guide the user. Paste a text of your choice and press the 1) `Enter` and 2) `Ctrl-d` keys to submit.

Press `Ctrl-c` to exit.

## **Summary Details**

The summarizer will output:

- a summary (the most important sentences)
- the 5 most important keywords

The summary will be approximately 20% of the original text.
