import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):

    doc = nlp(text)

    result = {
        "name": None,
        "organizations": [],
        "locations": []
    }

    for ent in doc.ents:
        if ent.label_ == "PERSON" and not result["name"]:
            result["name"] = ent.text
        elif ent.label_ == "ORG":
            result["organizations"].append(ent.text)
        elif ent.label_ == "GPE":
            result["locations"].append(ent.text)

    return result