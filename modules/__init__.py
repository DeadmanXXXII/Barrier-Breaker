"""
Barrier Breaker: A robust multilingual document translation tool.

This package provides utilities for translating documents between multiple languages
using the Helsinki-NLP MarianMT library and offers extensible support for additional functionality.
"""

# Import key modules and classes for convenient access
from .translator import Translator
from .utils import load_languages, save_translations

# Define version and metadata
__version__ = "1.0.0"
__author__ = "Your Name"
__license__ = "MIT"

# Utility functions to initialize the library
def initialize():
    """Initialize the translation tool (e.g., preload models)."""
    print("Initializing the translation package...")
