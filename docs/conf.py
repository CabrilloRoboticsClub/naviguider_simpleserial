import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "naviguider-simpleserial"
copyright = "2023, PNI Sensor"
author = "PNI Sensor"

version = "0.0.1"
release = "0.0.1"

extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]


todo_include_todos = True
