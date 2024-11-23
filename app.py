from flask import Flask, request, render_template, send_file
import os
from modules.file_handler import read_file, write_to_txt
from modules.translator import translate_text
from modules.grammar_corrector import correct_grammar

app = Flask(__name__)
UPLOAD_FOLDER = "uploads/"
OUTPUT_FOLDER = "outputs/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["file"]
        source_lang = request.form["source_lang"]
        target_lang = request.form["target_lang"]

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Process file
        text = read_file(file_path)
        translated_text = translate_text(text, source_lang, target_lang)
        corrected_text = correct_grammar(translated_text, lang=target_lang + "-US")

        # Save output
        output_path = os.path.join(OUTPUT_FOLDER, f"translated_{file.filename}.txt")
        write_to_txt(output_path, corrected_text)

        return send_file(output_path, as_attachment=True)

    return render_template("index.html")
