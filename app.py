from flask import Flask, render_template, request, send_file, send_from_directory
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    uploaded_file = request.files['file_path']
    if uploaded_file:
        file_content = uploaded_file.read().decode("utf-8")
        output_audio_path = request.form['output_audio_path']
        output_audio_path = output_audio_path + ".mp3"
        language = request.form['language']
        tts = gTTS(text=file_content, lang=language, slow=False)
        tts.save(output_audio_path)
        return send_file(output_audio_path, as_attachment=True)
    else:
        return "No file uploaded."

if __name__ == '__main__':
    app.run(debug=True)
