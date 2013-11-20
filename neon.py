# -*- coding: utf-8 -*-
"""
    pygments.styles.neon
    ~~~~~~~~~~~~~~~~~~~~~

    Neon Pygments style, modified from the Sublime Text/TextMate
    "Neon Color Scheme" https://github.com/MattDMo/Neon-color-scheme

    tango.py used as template, as it included all the known
    Token types, unlike most (if not all) of the styles included in the
    Pygments distribution. However, the final version of neon.py bears
    very little resemblance to tango.

    :copyright: Copyright 2013 by Matt Morrison mattdmo@mattdmo.com
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


class NeonStyle(Style):
    """
    Neon style inspired by the Sublime Text Neon Color Scheme -
    https://github.com/MattDMo/Neon-color-scheme
    """

    # work in progress...

    background_color = "#000000"
    default_style = ""

    styles = {
        # No corresponding class for the following:
        #Text:                     "", # class:  ''
        Whitespace:                "underline #f8f8f8",      # class: 'w'
        Error:                     "#f8f8f8 bg:#800f00", # class: 'err'
        Other:                     "#ffffff",                # class 'x'

        Comment:                   "italic #7f817e", # class: 'c'
        Comment.Multiline:         "italic #7f817e", # class: 'cm'
        Comment.Preproc:           "italic #7f817e", # class: 'cp'
        Comment.Single:            "italic #7f817e", # class: 'c1'
        Comment.Special:           "italic #7f817e", # class: 'cs'

        Keyword:                   "#0b93ff",   # class: 'k'
        Keyword.Constant:          "italic #ff07a0",   # class: 'kc'
        Keyword.Declaration:       "bold #204a87",   # class: 'kd'
        Keyword.Namespace:         "bold #204a87",   # class: 'kn'
        Keyword.Pseudo:            "bold #204a87",   # class: 'kp'
        Keyword.Reserved:          "bold #204a87",   # class: 'kr'
        Keyword.Type:              "bold #204a87",   # class: 'kt'

        Operator:                  "bold #ce5c00",   # class: 'o'
        Operator.Word:             "bold #204a87",   # class: 'ow' - like keywords

        Punctuation:               "bold #ffffff",   # class: 'p'

        # because special names such as Name.Class, Name.Function, etc.
        # are not recognized as such later in the parsing, we choose them
        # to look the same as ordinary variables.
        Name:                      "#ffffff",        # class: 'n'
        Name.Attribute:            "#c4a000",        # class: 'na' - to be revised
        Name.Builtin:              "#204a87",        # class: 'nb'
        Name.Builtin.Pseudo:       "#3465a4",        # class: 'bp'
        Name.Class:                "#ffffff",        # class: 'nc' - to be revised
        Name.Constant:             "#ffffff",        # class: 'no' - to be revised
        Name.Decorator:            "bold #5c35cc",   # class: 'nd' - to be revised
        Name.Entity:               "#ce5c00",        # class: 'ni'
        Name.Exception:            "bold #cc0000",   # class: 'ne'
        Name.Function:             "#ffffff",        # class: 'nf'
        Name.Property:             "#ffffff",        # class: 'py'
        Name.Label:                "#f57900",        # class: 'nl'
        Name.Namespace:            "#ffffff",        # class: 'nn' - to be revised
        Name.Other:                "#ffffff",        # class: 'nx'
        Name.Tag:                  "bold #204a87",   # class: 'nt' - like a keyword
        Name.Variable:             "#ffffff",        # class: 'nv' - to be revised
        Name.Variable.Class:       "#ffffff",        # class: 'vc' - to be revised
        Name.Variable.Global:      "#ffffff",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "#ffffff",        # class: 'vi' - to be revised

        Number:                    "bold #0000cf",   # class: 'm'
        Number.Float:              "bold #0000cf",   # class: 'mf'
        Number.Hex:                "bold #0000cf",   # class: 'mh'
        Number.Integer:            "bold #0000cf",   # class: 'mi'
        Number.Integer.Long:       "bold #0000cf",   # class: 'il'
        Number.Oct:                "bold #0000cf",   # class: 'mo'

        Literal:                   "#ffffff",        # class: 'l'
        Literal.Date:              "#ffffff",        # class: 'ld'

        String:                    "#4e9a06",        # class: 's'
        String.Backtick:           "#4e9a06",        # class: 'sb'
        String.Char:               "#4e9a06",        # class: 'sc'
        String.Doc:                "italic #218b97", # class: 'sd' - like a comment
        String.Double:             "#4e9a06",        # class: 's2'
        String.Escape:             "#4e9a06",        # class: 'se'
        String.Heredoc:            "italic #218b97",        # class: 'sh'
        String.Interpol:           "#4e9a06",        # class: 'si'
        String.Other:              "#4e9a06",        # class: 'sx'
        String.Regex:              "#4e9a06",        # class: 'sr'
        String.Single:             "#4e9a06",        # class: 's1'
        String.Symbol:             "#4e9a06",        # class: 'ss'

        Generic:                   "#ffffff",        # class: 'g'
        Generic.Deleted:           "#a40000",        # class: 'gd'
        Generic.Emph:              "italic #ffffff", # class: 'ge'
        Generic.Error:             "#ef2929",        # class: 'gr'
        Generic.Heading:           "bold #000080",   # class: 'gh'
        Generic.Inserted:          "#00A000",        # class: 'gi'
        Generic.Output:            "italic #ffffff", # class: 'go'
        Generic.Prompt:            "#8f5902",        # class: 'gp'
        Generic.Strong:            "bold #ffffff",   # class: 'gs'
        Generic.Subheading:        "bold #800080",   # class: 'gu'
        Generic.Traceback:         "bold #a40000",   # class: 'gt'
    }
