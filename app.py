from flask import Flask, render_template, request, send_from_directory
from flask_caching import Cache
import openai

app = Flask(__name__, template_folder="templates")
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


openai.api_key = "MY_API_KEY"


@app.route("/")
def home():
    return render_template('home.html', image_path='static/background_html.jpg')


@app.route("/results", methods=['POST'])
@cache.cached(timeout=300)
def results():
    prompt = request.form.get('prompt')
    if prompt is None:
        message = "Please enter a prompt."
    else:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=60
            )
            message = response.choices[0].text
        except Exception as e:
            message = "An error occurred: {}".format(e)
    return render_template('results.html', message=message)


if __name__ == "__main__":
    app.run(debug=True)
