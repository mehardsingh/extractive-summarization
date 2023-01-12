from utils import Vertex, Edge, filter_doc, textrank, nlp

def sentence_split(doc):
  sentences = []
  for sent in doc.sents:
    sentences.append(sent)
  return sentences

def remove_whitespace_sents(sentences):
    without_whitespace = []
    for sent in sentences:
        if not sent.text.isspace():
            without_whitespace.append(sent)

    return without_whitespace

def create_graph_summarization(sentences):
  num_sentences = len(sentences)

  V = {}
  W = {}
  for i in range(num_sentences):
    sent = sentences[i]
    if not sent in V:
      V[sent.text] = Vertex(sent.text)
      W[sent.text] = 1

  for i in range(num_sentences):
    for j in range(num_sentences):
      if i == j:
        continue

      sent_i = sentences[i]
      sent_j = sentences[j]
      similarity = sent_i.similarity(sent_j)

      V_i = V[sent_i.text]
      V_j = V[sent_j.text]
      e1 = Edge(V_j, similarity)
      e2 = Edge(V_i, similarity)
      V_i.add_out(e1)
      V_j.add_in(e2)

  return V, W

def extract_sentences(text, p=0.2):
  lower = text.lower()
  doc = nlp(lower)
  sentences = sentence_split(doc)
  sentences = remove_whitespace_sents(sentences)

  processed_to_original = {}
  processed_sentences = []
  for i in range(len(sentences)):
    sent = sentences[i]
    tokens = filter_doc(sent)
    combined = ' '.join(tokens)
    sentence_doc = nlp(combined)
    processed_sentences.append(sentence_doc)
    processed_to_original[sentence_doc.text] = (sent.text, i)

  V, W = create_graph_summarization(processed_sentences)
  dic = textrank(V, W)

  ordered_imp = sorted(dic.items(), key=lambda x:x[1], reverse=True)

  original = []
  for processed in ordered_imp:
    original.append(processed_to_original[processed[0]])

  ordered_idx = sorted(original, key=lambda x:x[1], reverse=False)
  sentence_extraction = [p[0] for p in ordered_idx]
  summary_len = int(p * len(sentences))
  limit = sentence_extraction[:summary_len]
  return limit
