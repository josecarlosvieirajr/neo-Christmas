from flask import Flask, render_template, request
from flask_cors import CORS

from backend.view.api_view import transcribe_audio_to_text

app = Flask(__name__)
CORS(app)


@app.route("/")
def menu():
    return render_template('index.html')

#
# @app.route("/bibleGen")
# def bible_gen():
#     wc = TextGenerator()
#     context = {
#         'Novo Evangelho': wc.get_text()
#     }
#     return render_template('bible.html', context=context)
#
#
# # @app.route("/businessGen", methods=['POST', 'GET'])
# # def business_gen():
# #     for key, value in request.form.items():
# #         wc = BusinessGen(value)
# #         context = {
# #             f'Pesquisa Sobre {value}': wc.run()
# #         }
# #     return render_template('business.html', context=context)
#
#
# @app.route("/brainGen", methods=['POST', 'GET'])
# def brain_gen():
#     for key, value in request.form.items():
#         context = {
#             f'Pesquisa Sobre ': {value}
#         }
#     return render_template('brain.html', context=context)
#
#
# @app.route("/brainGenText", methods=['POST', 'GET'])
# def brain_text_gen():
#     context2 = ''
#     for key, value in request.form.items():
#         context2 = [value, value, value]
#     return render_template('brain_text.html', context=context2)


app.add_url_rule('/send_audio_file', methods=['POST'], view_func=transcribe_audio_to_text)

if __name__ == "__main__":
    app.run(debug=True, threaded=False, host='0.0.0.0', port=5000)
