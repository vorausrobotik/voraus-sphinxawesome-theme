# -- Project information -----------------------------------------------------

project = "Sphinxawesome Theme"
copyright = "2020, Kai Welke"
author = "Kai Welke"

# -- General configuration ---------------------------------------------------

extensions = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
nitpicky = True
default_role = "literal"

rst_prolog = r'''.. |name| replace:: sphinxawesome theme'''

# -- Options for HTML output -------------------------------------------------

html_theme = "sphinxawesome_theme"
html_theme_path = ["../sphinxawesome_theme"]
html_theme_options = {"nav_include_hidden": True}
html_last_updated_fmt = "%b %d, %Y"