import editdistance
from typing import Dict, List, Set, Union

# builds a graph out of the given list of words, returning the graph in a dict of (node, connections[])
def build_graph(words: List[str]) -> Dict[str, Set[str]]:
	result = dict()
	for word in words:
		result[word] = set(filter(lambda x: editdistance.eval(word, x) == 1, words))
	return result

def find_path(from_word: str, to_word: str, graph: Dict[str, Set[str]], traversed: Set[str]) -> Union[List[str], None]:
	traversed.add(from_word)
	
	if not from_word in graph:
		return None
	
	if to_word in graph[from_word]:
		return [from_word, to_word]
	
	# obtain shortest result
	next_words = filter(lambda x: not x in traversed, graph[from_word])
	results = list(filter(lambda x: x != None, [find_path(x, to_word, graph, traversed) for x in next_words]))
	sorted_results = sorted(results, key=lambda x: len(x))

	return [from_word] + sorted_results[0] if len(sorted_results) > 0 else None

def shortest_string_path(str_a: str, str_b: str, words: Dict[str, bool]) -> List[str]:
	words_l = list(words.keys())
	words_l.append(str_a)
	words_l.append(str_b)

	graph = build_graph(words_l)
	path = find_path(str_a, str_b, graph, set())
	return path