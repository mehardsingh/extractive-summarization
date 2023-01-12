from constants import POS_TAGS, MAX_ITERS, CONVERGENCE
import spacy

nlp = spacy.load("en_core_web_md")

class Vertex:
  def __init__(self, text_unit):
    self.text_unit = text_unit
    self.out_edges = []
    self.in_edges = []

  def add_out(self, edge):
    self.out_edges.append(edge)

  def add_in(self, edge):
    self.in_edges.append(edge)

class Edge:
  def __init__(self, text_unit, weight):
    self.text_unit = text_unit
    self.weight = weight

def format_whitespace(text):
  text.replace('\n', ' ')
  return text

def filter_doc(doc):
  filtered = []
  for token in doc:
    if not token.is_stop and not token.is_punct and token.vector_norm and token.pos_ in POS_TAGS:
      lemma = token.lemma_
      filtered.append(lemma)

  return filtered

def get_neighbors_sum(V):
  neighbors_sum = {}
  for textunit in V:
    vertex = V[textunit]
    neighbors_sum[vertex] = sum(e.weight for e in vertex.out_edges)
  return neighbors_sum

def textrank(V, W, d=0.85):
  neighbors_sum_dict = get_neighbors_sum(V)

  iteration_quantity = 0
  for i in range(MAX_ITERS):
      iteration_quantity += 1
      convergence_achieved = 0
      for lemma in V:
          V_i = V[lemma]
          rank = 1 - d
          for e1 in V_i.in_edges:
              V_j = e1.text_unit
              neighbors_sum = neighbors_sum_dict[V_j]
              if neighbors_sum == 0:
                continue
              rank += d * e1.weight / neighbors_sum * W[V_j.text_unit]

          if abs(W[lemma] - rank) <= CONVERGENCE:
              convergence_achieved += 1

          W[lemma] = rank

      if convergence_achieved == len(V):
          break

  return W