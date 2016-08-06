import spacy
import glob

def get_person_names(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    # get all proper nouns
    cleaned = [name.lemma_ for name in doc.ents if name.label_ == 'PERSON' ]

    return list(set(cleaned))

def main():
    text = input('Please enter the text:\n')
    persons = get_person_names(text)
    print(persons)

def test():
    files = glob.glob('samples/*.txt')

    for name in files:
        text = open(name).read()
        persons = get_person_names(text)

        print('TEXT:')
        print(text, '\n')
        print('List of person names:', persons)
        print('\n--------------\n')

if __name__ == '__main__':
    test()
    main()
