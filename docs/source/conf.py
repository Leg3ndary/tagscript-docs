# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "Tagscript-Docs"
copyright = "2022, Ben Z"
author = "_Leg3ndary"

release = "0.1"
version = "0.1.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.ansi",
    "sphinxcontrib.tagscript",
    'sphinx_panels'
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_static_path = ["style.css"]
html_theme = "sphinx_rtd_theme"
html_favicon = "images/tagscript-logo.ico"

# -- Options for EPUB output
epub_show_urls = "footnote"


def setup(app):
    app.add_css_file("style.css")
