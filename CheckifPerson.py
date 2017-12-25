from SPARQLWrapper import SPARQLWrapper, JSON

def get_property(entity):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)
    query = "PREFIX db: <http://dbpedia.org/resource/> SELECT ?p ?o WHERE { db:"+entity+" ?p ?o }"
    sparql.setQuery(query)  

    return sparql.query().convert()

#replace spaces in words with underscore
entity_to_be_checked = ['Rajinikanth','New_York', 'Add','Priyanka_Chopra', 'Clever', 'Dabangg']
for i in entity_to_be_checked:
	flag = 0
	prop = get_property(i)
	for j in prop['results']['bindings']:
		if "Person" in j['o']['value']:
			flag = 0
			break
			# print(j['o']['value'])
		else:
			flag =1 
			pass
	if flag == 1:
		print(i,"is not a person")
	else:
		print(i,"is a person")
