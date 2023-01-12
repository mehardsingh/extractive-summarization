from utils import filter_doc, textrank, nlp, Vertex, Edge
from constants import WINDOW

def create_graph_keyword(filtered):
  filtered_len = len(filtered)

  V = {}
  W = {}
  for i in range(filtered_len):
    lemma = filtered[i]
    if not lemma in V:
      V[lemma] = Vertex(lemma)
      W[lemma] = 1

  for i in range(filtered_len):
    for j in range(max(0, i - WINDOW), min(filtered_len - 1, i + WINDOW)):
      lemma_i = filtered[i]
      lemma_j = filtered[j]
      similarity = nlp(lemma_i)[0].similarity(nlp(lemma_j)[0])

      V_i = V[lemma_i]
      V_j = V[lemma_j]
      e1 = Edge(V_j, similarity)
      e2 = Edge(V_i, similarity)
      V_i.add_out(e1)
      V_j.add_in(e2)

  return V, W

def extract_keywords(text):
  lower = text.lower()
  doc = nlp(lower)
  filtered = filter_doc(doc)
  V, W = create_graph_keyword(filtered)

  dic = textrank(V, W)
  ordered = sorted(dic.items(), key=lambda x:x[1], reverse=True)
  keywords = [kw[0] for kw in ordered]
  
  return keywords[:5]