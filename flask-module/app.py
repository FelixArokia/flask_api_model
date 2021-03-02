from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import pandas as pd
import json
import base64
from multiprocessing import Value
counter = Value('i', 0)

model_counter = 0

app = Flask(__name__)

@app.route('/', methods=['GET'])
def show_model_counter():
    with counter.get_lock():
        counter.value += 1
        out = counter.value

    return jsonify(count=out)


@app.route('/model_predict/', methods=['POST'])
def makecalc():
    j_data = request.get_json()
    j_data = j_data['data']
    print('j_data: ', j_data)
    prediction = np.array2string(model.predict(j_data))
    predict_proba = np.array2string(model.predict_proba(j_data))
    print(model.predict(j_data))
    print(prediction)

    return jsonify(prediction, predict_proba)


if __name__ == '__main__':
    modelfile = '../models/final_prediction.pickle'
    model = p.load(open(modelfile, 'rb'))

    app.run(debug=True, host='0.0.0.0')