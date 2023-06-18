#!/usr/bin/env python

from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)


@app.route('/scrape', methods=['POST'])
def scrape_data():
    id = request.json.get('id')

    try:
        # Execute the scraper script
        result = subprocess.run(['python', 'main.py', str(id)], capture_output=True, text=True)
        output = result.stdout
        error = result.stderr

        if error:
            response = {'success': False, 'message': error}
        else:
            response = {'success': True, 'data': output}

    except Exception as e:
        response = {'success': False, 'message': str(e)}

    return jsonify(response)

if __name__ == '__main__':
    app.run()


