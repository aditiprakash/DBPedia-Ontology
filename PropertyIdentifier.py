from SPARQLWrapper import SPARQLWrapper, JSON

def get_property(entity):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setReturnFormat(JSON)
    query = "PREFIX db: <http://dbpedia.org/resource/> SELECT ?p ?o WHERE { db:"+entity+" ?p ?o }"
    sparql.setQuery(query)  

    return sparql.query().convert()

#separate first and second name by an underscore
names = ['Rajinikanth','New_York', 'Add','Priyanka_Chopra', 'Clever', 'Dabangg']
for i in names:
	flag = 0
	m = get_property(i)
	for j in m['results']['bindings']:
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
