import requests,spacy,syllapy

from spacy.matcher import Matcher
import random
nlp = spacy.load("en_core_web_sm")

matcher2 = Matcher(nlp.vocab)
matcher3 = Matcher(nlp.vocab)
matcher4 = Matcher(nlp.vocab)

pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
           {'POS':  {"IN": ["NOUN", "VERB"]} }]
matcher2.add("TwoWords", [pattern])
pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
           {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
           {'POS':  {"IN": ["NOUN", "VERB", "ADJ", "ADV"]} }]
matcher3.add("ThreeWords", [pattern])
pattern = [{'POS':  {"IN": ["NOUN", "ADP", "ADJ", "ADV"]} },
           {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
           {'IS_ASCII': True, 'IS_PUNCT': False, 'IS_SPACE': False},
           {'POS':  {"IN": ["NOUN", "VERB", "ADJ", "ADV"]} }]
matcher4.add("FourWords", [pattern])

def NewsFromBBC():
	
	# BBC news api
	query_params = {
	"country":"in",
	"source": "bbc-news",
	"sortBy": "top",
	"pageSize":10,
	"apiKey": "4dbc17e007ab436fb66416009dfb59a8"
	}
	main_url = " https://newsapi.org/v1/articles"

	# fetching data in json format
	res = requests.get(main_url, params=query_params)
	open_bbc_page = res.json()

	# getting all articles in a string article
	article = open_bbc_page["articles"]
	# empty list which will
	# contain all trending news
	#results = []
	text_block = ""
	for ar in article:
		text_block=" ".join([text_block,ar["title"]])
	#print(text_block)

	doc = nlp(text_block)
	matches2 = matcher2(doc)
	matches3 = matcher3(doc)
	matches4 = matcher4(doc)

	g_5 = []
	g_7 = []
	#print(doc)
	for match_id, start, end in matches2 + matches3 + matches4:
		string_id = nlp.vocab.strings[match_id]  # Get string representation
		span = doc[start:end]  # The matched span

		syl_count = 0
		for token in span:
			syl_count += syllapy.count(token.text)
		if syl_count == 5:
			if span.text not in g_5:
				g_5.append(span.text)
		if syl_count == 7:
			if span.text not in g_7:
				g_7.append(span.text)
	
	print("Enter for a new haiku. ^C to quit\n")
	while (True):
		print("%s\n%s\n%s" %(random.choice(g_5),random.choice(g_7),random.choice(g_5)))
		input("\n")

NewsFromBBC()
