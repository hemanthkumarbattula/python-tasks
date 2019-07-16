#! /usr/bin/env python3


def ConllUReader(treebankfile):
	sentence = {}
	for line in treebankfile:
		if line.startswith("#"):
			continue

		# parse sentence end
		elif line.isspace():
			if sentence != {}:
				yield sentence
			sentence = {}

		else:
			data = line.split("\t")
			if '-' in data[0] or '.' in data[0]:	# skip the word
				continue
			sentence[int(data[0])] = {"form": data[1], "lemma": data[2], "upos": data[3], "xpos": data[4], "feats": data[5], "head": int(data[6]), "deprel": data[7], "deps": data[8], "misc": data[9].strip()}

	if sentence != {}:
		yield sentence


def displayArcs(arcs, sentence):
	for arc in arcs:
		h, d, l = arc
		print(sentence[h]["form"], "---" + l + "-->", sentence[d]["form"])
	print()


def displayOriginalArcs(sentence):
	for x in sorted(sentence):
		if sentence[x]["head"] > 0:
			print(sentence[sentence[x]["head"]]["form"], "---" + sentence[x]["deprel"] + "-->", sentence[x]["form"])
	print()


def head(i, sentence) :
	return sentence[i]['head']


def deprel(i, sentence):
	return sentence[i]['deprel']


def arc_eager_oracle(stack, buffer, sentence):
	if stack == []:
		return 'SHIFT'
	else:
		# COMPLETE CODE HERE (PART 2)

		i=stack[-1]
		j=buffer[0]
		if head(i,sentence) ==j:
			dere= deprel(i, sentence)
			return "LEFT-ARC-"+dere
		elif head(j,sentence) == 𝑖:
			dere = deprel(j,sentence)
			return "RIGHT-ARC-"+ dere
		elif [k for k in stack if head(j,sentence)== k or head(k,sentence) == j] !=[]:
			return 'REDUCE'
		else:
			return 'SHIFT'


# combines algorithms 1 and 3
def parse_arc_eager(sentence, transition_list = None):

	stack = []
	buffer = [x for x in sorted(sentence)]
	arcs = []
	while buffer != []:
		# if transition list is given, pick the first transition (Algorithm 1)
		if transition_list is not None:
			t = transition_list.pop(0)
		# if no transition list is given, call the oracle (Algorithm 3)
		else:
			t = arc_eager_oracle(stack, buffer, sentence)
		
		# COMPLETE CODE HERE (PART 1) THEN UPDATE TO INCLUDE (PART 3)
		if t=='SHIFT':
			stack.append(buffer.pop(0))
		elif 'LEFT-ARC' in t:
			arcs.append((buffer[0], stack.pop(-1), t.split('-')[2]))

		elif 'RIGHT-ARC' in t:
			stack.append(buffer.pop(0))
			arcs.append((stack[-2], stack[-1], t.split('-')[2]))
		elif t=='REDUCE':
			stack.pop(-1)
	return arcs


# Test procedure for part 1
def test_parse():
	sentence = {
		1: {"form": "the"},
		2: {"form": "cat"},
		3: {"form": "sits"},
		4: {"form": "on"},
		5: {"form": "the"},
		6: {"form": "mat"},
		7: {"form": "today"}
	}
	
	transition_sequence = ["SHIFT", "LEFT-ARC-det", "SHIFT", "LEFT-ARC-nsubj", "SHIFT", "SHIFT", "SHIFT", "LEFT-ARC-det", "LEFT-ARC-case", "RIGHT-ARC-nmod", "REDUCE", "RIGHT-ARC-advmod", "REDUCE"]
	
	arcs = parse_arc_eager(sentence, transition_list=transition_sequence)
	displayArcs(arcs, sentence)


# Test procedure for part 2
def test_oracle():
	sentence = {
		1: {"form": "the", "head": 2, "deprel": "det"},
		2: {"form": "dog", "head": 3, "deprel": "nsubj"},
		3: {"form": "sat", "head": 0, "deprel": "root"},
		4: {"form": "on", "head": 6, "deprel": "case"},
		5: {"form": "the", "head": 6, "deprel": "det"},
		6: {"form": "couch", "head": 3, "deprel": "nmod"},
		7: {"form": "yesterday", "head": 3, "deprel": "advmod"}
	}
	
	stack = []
	buffer = [1, 2, 3, 4, 5, 6, 7]
	transition = arc_eager_oracle(stack, buffer, sentence)
	print(transition)
	
	stack = [1]
	buffer = [2, 3, 4, 5, 6, 7]
	transition = arc_eager_oracle(stack, buffer, sentence)
	print(transition)
	
	stack = [3]
	buffer = [6, 7]
	transition = arc_eager_oracle(stack, buffer, sentence)
	print(transition,'\n')


# Test procedure for part 3
def test_parse_oracle():
	sentence = {
		1: {"form": "the", "head": 2, "deprel": "det"},
		2: {"form": "dog", "head": 3, "deprel": "nsubj"},
		3: {"form": "sat", "head": 0, "deprel": "root"},
		4: {"form": "on", "head": 6, "deprel": "case"},
		5: {"form": "the", "head": 6, "deprel": "det"},
		6: {"form": "couch", "head": 3, "deprel": "nmod"},
		7: {"form": "yesterday", "head": 3, "deprel": "advmod"}
	}
	
	arcs = parse_arc_eager(sentence)
	print("Predicted arcs:")
	displayArcs(arcs, sentence)
	print("Original arcs:")
	displayOriginalArcs(sentence)




if __name__ == "__main__":
	test_parse()
	test_oracle()
	test_parse_oracle()
