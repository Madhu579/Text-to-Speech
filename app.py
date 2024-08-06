from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('tts.html')

@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    output_audio_path = request.form['output_audio_path']
    output_audio_path = output_audio_path + ".mp3"
    language = request.form['language']

    # Check the option chosen by the user
    option = request.form['option']

    # If user chooses to upload a file
    if option == 'file':
        uploaded_file = request.files['file_path']
        if uploaded_file:
            file_content = uploaded_file.read().decode("utf-8")
            tts = gTTS(text=file_content, lang=language, slow=False)
            tts.save(output_audio_path)
            return send_file(output_audio_path, as_attachment=True)
        else:
            return "No file uploaded."

    # If user chooses to enter text directly
    elif option == 'text':
        text_content = request.form.get('text_content')
        if text_content:
            tts = gTTS(text=text_content, lang=language, slow=False)
            tts.save(output_audio_path)
            return send_file(output_audio_path, as_attachment=True)
        else:
            return "No text provided."

if __name__ == '__main__':
    app.run(debug=True)
