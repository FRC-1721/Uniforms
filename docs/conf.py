import os
import sys
import subprocess
import sphinx_theme

# Revision/git information
release = (
    subprocess.check_output(
        [
            "git",
            "describe",
            "--abbrev=4",
            "--always",
            "--tags",
        ]
    )
    .strip()
    .decode("utf-8")
)


# Project Information
project = "Tidal Force Uniform and Style Guide"
copyright = "2021-2022, To Be Announced"
author = "Tidal Force, FRC Team 1721"

# Ammend any custom extensions we have
sys.path.append(os.path.abspath("uniforms/patches"))

# General Config
extensions = [
    "sphinx.ext.autosectionlabel",
    "patchbuilder",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# HTML output options
html_theme = "stanford_theme"
html_theme_path = [sphinx_theme.get_html_theme_path("stanford-theme")]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# PDF output options
latex_elements = {"extraclassoptions": "openany,oneside"}

latex_logo = "resources/banner.png"
