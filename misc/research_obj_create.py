# Creates a RO-Crate package with a pdf, csv, and svg file, and adds metadata including author information,
# then writes the crate to 'exp_crate'.
# RO-Crate establishes a lightweight approach to packaging research data and metadata.
# https://pypi.org/project/rocrate/
from rocrate.model.person import Person
from rocrate.rocrate import ROCrate

crate = ROCrate()

paper = crate.add_file("exp/paper.pdf", properties={
    "name": "manuscript",
    "encodingFormat": "application/pdf"
})

table = crate.add_file("exp/results.csv", properties={
    "name": "experimental data",
    "encodingFormat": "text/csv"
})

diagram = crate.add_file("exp/diagram.svg", dest_path="images/figure.svg", properties={
    "name": "bar chart",
    "encodingFormat": "image/svg+xml"
})

alice_id = "https://orcid.org/0000-0000-0000-0000"
bob_id = "https://orcid.org/0000-0000-0000-0001"

alice = crate.add(Person(crate, alice_id, properties={
    "name": "Alice Doe",
    "affiliation": "University of Flatland"
}))

bob = crate.add(Person(crate, bob_id, properties={
    "name": "Bob Doe",
    "affiliation": "University of Flatland"
}))

paper["author"] = [alice, bob]
table["author"] = alice
diagram["author"] = bob

crate.write("exp_crate")
