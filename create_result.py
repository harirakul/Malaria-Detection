import glob
from dominate import document
from dominate.tags import *
import malaria_prediction

def make(filename):
    with document(title='Malaria Report') as doc:
        h1('Result:')
        div(img(src=filename), _class='photo')
        result = malaria_prediction.predict(filename)
        h2(f"The inputted cell is {result[0]} with a confidence of {round(float(result[1]), 2)}%.")

    return doc.render()