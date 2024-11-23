# utils.py
import json
import os

def load_languages(filepath):
    """
    Load the list of supported languages from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file containing language mappings.
    
    Returns:
        dict: A dictionary of language codes and names.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Language file not found: {filepath}")
    
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def save_translations(translations, output_path):
    """
    Save translated content to a file.
    
    Args:
        translations (dict): A dictionary with keys as section names and values as translated text.
        output_path (str): Path to save the output file.
    """
    with open(output_path, "w", encoding="utf-8") as file:
        for section, text in translations.items():
            file.write(f"[{section}]\n{text}\n\n")

def detect_file_type(file_path):
    """
    Detect the type of a file based on its extension.
    
    Args:
        file_path (str): Path to the file.
    
    Returns:
        str: File type (e.g., 'txt', 'docx', 'pdf').
    """
    return os.path.splitext(file_path)[1][1:].lower()
