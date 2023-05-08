import openai
import logging
from flask import Flask, render_template, request, send_from_directory
from flask_caching import Cache
from openai_api import openai_api

# logging.basicConfig(filename='app.log', level=logging.DEBUG)

app = Flask(__name__, template_folder="templates")
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

openai.api_key = "YOUR_API_KEY"

app.register_blueprint(openai_api, url_prefix='/openai')


@app.route("/")
def home():
    logging.info('home function called')
    return render_template('home.html', image_path='static/background_html.jpg')


@app.route("/results", methods=['POST'])
@cache.cached(timeout=3600)
def results():
    prompt = request.form.get('prompt')
    if prompt is None:
        message = "Please enter a prompt."
    else:
        try:
            response = openai.Completion.create(
                engine="davinci",
                prompt=prompt,
                max_tokens=50
            )
            message = response.choices[0].text
        except Exception as e:
            message = "An error occurred: {}".format(e)
            logging.exception('Error in results function:')

    return render_template('results.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
