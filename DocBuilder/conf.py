#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SunshineWidgets documentation build configuration file, created by
# sphinx-quickstart on Fri Apr 21 20:15:10 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import shutil
sys.path.insert(0, os.path.abspath('../poco'))

from recommonmark.parser import CommonMarkParser


# prepare tree structure
this_dir = os.path.dirname(os.path.abspath(sys._getframe(0).f_code.co_filename))
os.chdir(this_dir)

print sys.argv
# compatible with readthedocs online builder and local builder
if sys.argv[0].endswith('sphinx-build') and ('html' in sys.argv or sys.argv[-1] == '_build/html'):
    if not os.path.exists('source'):
        os.mkdir('source')

    # gen api-doc
    os.environ['SPHINX_APIDOC_OPTIONS'] = 'members,show-inheritance'
    os.system("sphinx-apidoc -Me -o source/ ../poco ../poco/utils")

    # prepare other file
    shutil.copyfile('../README.rst', 'source/README.rst')
    if os.path.exists('source/doc'):
        shutil.rmtree('source/doc')
    shutil.copytree('../doc', 'source/doc')


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.napoleon',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
source_parsers = {
   '.md': CommonMarkParser,
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'poco'
copyright = '2017, NetEase Co, Ltd.'
author = ['lxn3032@corp.netease.com', 'gzliuxin@corp.netease.com']

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = os.environ.get('LANGUAGE') or 'zh_CN'  # language supported
locale_dirs = ['locale/']  # path is example but recommended.
gettext_compact = False  # optional.

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pocodoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'poco.tex', 'poco Documentation',
     'lxn3032', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'poco', 'poco Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'poco', 'poco Documentation',
     author, 'poco', 'A cross-engine UI automation framework.',
     'Miscellaneous'),
]

napoleon_include_special_with_doc = True
napoleon_include_init_with_doc = True
napoleon_use_param = True
napoleon_use_rtype = True

# if True:
#     class poco.sdk.AbstractDumper.IDumper
# if False:
#     class IDumper
add_module_names = False
