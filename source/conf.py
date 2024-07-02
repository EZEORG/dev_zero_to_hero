# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Dev_zero_to_hero'
copyright = '2024, ezelab'
author = 'ezelab'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "myst_parser",
  "sphinx.ext.autodoc",
  "sphinx.ext.intersphinx",
  "sphinx.ext.extlinks",
  "sphinx.ext.todo",
  "sphinx.ext.viewcode",
  "sphinxcontrib.mermaid",
  "sphinx_tabs.tabs",
  "sphinxemoji.sphinxemoji",
  "sphinx_copybutton",
  "sphinx_design",
  "sphinx_comments"
]

templates_path = ['_templates']
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store']

language = 'zh'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'shibuya'
html_static_path = ['_static']


html_css_files = [
 "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]

