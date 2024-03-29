import os
from flask import json
import matplotlib.pyplot as plt
import base64
from io import BytesIO

SERVER_ENDPOINT = 'http://localhost:5000'

def generate_vis(data):
    filePath = os.environ['RESULT_FILE_PATH']
    with open(filePath, 'w') as file:
        text = dumps_json(data)
        file.write(text)


def loads_json(data):
    return json.loads(data)


def dumps_json(data):
    return json.dumps(data)

def render_pyplot_figure():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    bufferValue = buffer.getvalue()
    buffer.close()
    b64 = base64.b64encode(bufferValue)
    b64String = b64.decode('utf-8')
    dataUrl = f'data:image/png;base64,{b64String}'
    print(dataUrl)