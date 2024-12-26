# Manages, queries, and manipulates RDF graphs, including extracting data from the web, creating and adding
# custom triples, and printing various properties and formats.
# https://rdflib.readthedocs.io/en/stable/gettingstarted.html
from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD


def read_graph():
    # from rdflib import Graph

    # Create a Graph
    g = Graph()

    # Parse in an RDF file hosted on the Internet
    g.parse("http://www.w3.org/People/Berners-Lee/card")
    # Last attempt. OK, why doesn't anything else work?
    # g.parse("http://www.w3.org/People/Westhaver/card")  # Susan

    # Loop through each triple in the graph (subj, pred, obj)
    for subj, pred, obj in g:
        # Check if there is at least one triple in the Graph
        if (subj, pred, obj) not in g:
            raise Exception("It better be!")

    # Print the number of "triples" in the Graph
    print(f"Graph g has {len(g)} statements.")
    # Prints: Graph g has 86 statements.

    # Print out the entire Graph in the RDF Turtle format
    print(g.serialize(format="turtle"))


def sparql_query():
    # from rdflib import Graph

    # Create a Graph, pare in Internet data
    g = Graph().parse("http://www.w3.org/People/Berners-Lee/card")

    # Query the data in g using SPARQL
    # This query returns the 'name' of all ``foaf:Person`` instances
    q = """
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>

        SELECT ?name
        WHERE {
            ?p rdf:type foaf:Person .

            ?p foaf:name ?name .
        }
    """

    # Apply the query to the graph and iterate through results
    for r in g.query(q):
        print(r["name"])


def add_people(g):
    # Create an RDF URI node to use as the subject for multiple triples
    donna = URIRef("http://example.org/donna")

    # Add triples using store's add() method.
    g.add((donna, RDF.type, FOAF.Person))
    g.add((donna, FOAF.nick, Literal("donna", lang="en")))  # notice lang=en
    g.add((donna, FOAF.name, Literal("Donna Summer")))
    g.add((donna, FOAF.mbox, URIRef("mailto:donna@example.org")))  # notice URIRef

    # Add another person
    wave = URIRef("http://example.org/waverly")

    # Add triples using store's add() method.
    g.add((wave, RDF.type, FOAF.Person))
    g.add((wave, FOAF.nick, Literal("waverly", datatype=XSD.string)))  # notice datatype
    g.add((wave, FOAF.name, Literal("Waverly Earp")))
    g.add((wave, FOAF.mbox, Literal("w.earp@example.org", datatype=XSD.anyURI)))  # notice anyURI


def print_raw(g):
    # Iterate over triples in store and print them out.
    print("\n--- printing raw triples ---")
    for s, p, o in g:
        print((s, p, o))


def print_mailbox(g):
    # For each foaf:Person in the store, print out their mbox property's value.
    print("\n--- printing mboxes ---")
    for person in g.subjects(RDF.type, FOAF.Person):
        for mbox in g.objects(person, FOAF.mbox):
            print(mbox)


def print_all(g):
    # Bind the FOAF namespace to a prefix for more readable output
    g.bind("foaf", FOAF)

    # print all the data in the Notation3 format
    print("\n--- printing n3 ---")
    print(g.serialize(format='n3'))


def create_graph():
    # from rdflib import Graph, Literal, RDF, URIRef
    # from rdflib.namespace import FOAF, XSD

    # Create a Graph
    g = Graph()

    # Add people to graph
    add_people(g)

    # PRINT
    print_raw(g)
    print_mailbox(g)
    print_all(g)


def create1():
    import uuid
    from rdflib import Graph, Literal, RDF, URIRef, BNode
    # Create a Graph
    g = Graph()
    annotation = URIRef("http://www.w3.org/ns/oa/Annotation")
    body = URIRef("http://www.w3.org/ns/oa/body")
    source = URIRef("http://www.w3.org/ns/oa/source")
    target = URIRef("http://www.w3.org/ns/oa/target")
    fragment_selector = URIRef("http://www.w3.org/ns/oa/FragmentSelector")
    selector = URIRef("http://www.w3.org/ns/oa/Selector")
    til = URIRef("http://snomed.info/id/56972008")
    has_probability = URIRef("https://bmi.stonybrookmedicine.edu/ns/hasProbability")

    anno = URIRef("urn:uuid:" + uuid.uuid4().hex)

    target_b = BNode()
    selection_b = BNode()
    prob_b = BNode()

    g.add((anno, RDF.type, annotation))
    g.add((anno, body, prob_b))
    g.add((prob_b, has_probability, Literal(0.874)))
    g.add((prob_b, RDF.type, til))
    g.add((anno, target, target_b))
    g.add((target_b, RDF.type, fragment_selector))
    g.add((target_b, selector, selection_b))
    g.add((selection_b, RDF.value, Literal("<polygon points=\"220,10 300,210 170,250 123,234>/>")))
    g.add((target_b, source, URIRef("http://imagebox.com/files/webfiles/image.svs")))

    g.bind("oa", URIRef("http://www.w3.org/ns/oa/"))
    g.bind("prob_b", URIRef("https://bmi.stonybrookmedicine.edu/ns/"))

    print(g.serialize(format='ttl'))


# read_graph()
# sparql_query()
create_graph()
# create1()

exit(0)
