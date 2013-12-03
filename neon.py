# -*- coding: utf-8 -*-
"""
    pygments.styles.neon
    ~~~~~~~~~~~~~~~~~~~~

    Neon Pygments style, modified from the Sublime Text/TextMate
    `Neon Color Scheme <https://github.com/MattDMo/Neon-color-scheme>`__

    tango.py used as template, as it included all the known
    Token types, unlike most (if not all) of the styles included in the
    Pygments distribution. However, the final version of neon.py bears
    no resemblance to tango.

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
    highlight_color  = "#2d2d2d"
    default_style    = ""

    styles = {
        # token                    http://pygments.org/docs/styles/#style-rules
        Text:                      "#ffffff", # class:  ''
        Whitespace:                "#f8f8f8",      # class: 'w'
        Error:                     "#f8f8f8 bg:#800f00", # class: 'err'
        Other:                     "#ffffff",                # class 'x'

        Comment:                   "italic #7f817e", # class: 'c'
        Comment.Multiline:         "italic #7f817e", # class: 'cm'
        Comment.Preproc:           "italic #7f817e", # class: 'cp'
        Comment.Single:            "italic #7f817e", # class: 'c1'
        Comment.Special:           "italic #7f817e", # class: 'cs'

        Keyword:                   "#0b93ff",   # class: 'k'
        Keyword.Constant:          "italic #ff07a0",   # class: 'kc'
        Keyword.Declaration:       "#0b93ff",   # class: 'kd'
        Keyword.Namespace:         "#0b93ff",   # class: 'kn'
        Keyword.Pseudo:            "#0b93ff",   # class: 'kp'
        Keyword.Reserved:          "#0b93ff",   # class: 'kr'
        Keyword.Type:              "#0b93ff",   # class: 'kt'

        Operator:                  "bold #a7a3ff",   # class: 'o'
        Operator.Word:             "bold #a7a3ff",   # class: 'ow' - like keywords

        Punctuation:               "#fffef7",   # class: 'p'

        Name:                      "#08d879",        # class: 'n'
        Name.Attribute:            "#c4a000",        # class: 'na' - to be revised
        Name.Builtin:              "italic #e0a1ff",        # class: 'nb'
        Name.Builtin.Pseudo:       "italic #0aedff",        # class: 'bp'
        Name.Class:                "#cfff01",        # class: 'nc' - to be revised
        Name.Constant:             "italic #eb939a",        # class: 'no' - to be revised
        Name.Decorator:            "#b6b8fe bg:#070e48",   # class: 'nd' - to be revised
        Name.Entity:               "#ce5c00",        # class: 'ni'
        Name.Exception:            "bold #ff1e00",   # class: 'ne'
        Name.Function:             "#10ff02",        # class: 'nf'
        Name.Property:             "#b6b8fe",        # class: 'py'
        Name.Label:                "#f57900",        # class: 'nl'
        Name.Namespace:            "#11bd7c",        # class: 'nn' - to be revised
        Name.Other:                "#ff25d9",        # class: 'nx'
        Name.Tag:                  "bold #02aeff",   # class: 'nt' - like a keyword
        Name.Variable:             "#ff25d9",        # class: 'nv' - to be revised
        Name.Variable.Class:       "#cfff01",        # class: 'vc' - to be revised
        Name.Variable.Global:      "#d285cc",        # class: 'vg' - to be revised
        Name.Variable.Instance:    "#d285cc",        # class: 'vi' - to be revised

        Number:                    "#ff0604",   # class: 'm'
        Number.Float:              "#ff0604",   # class: 'mf'
        Number.Hex:                "italic #ff0604",   # class: 'mh'
        Number.Integer:            "#ff0604",   # class: 'mi'
        Number.Integer.Long:       "#ff0604",   # class: 'il'
        Number.Oct:                "italic #ff0604",   # class: 'mo'

        Literal:                   "#db1e44",        # class: 'l'
        Literal.Date:              "#14ff01",        # class: 'ld'

        String:                    "#ffdf02",        # class: 's'
        String.Backtick:           "italic #ffdf02",        # class: 'sb'
        String.Char:               "#ffdf02",        # class: 'sc'
        String.Doc:                "italic #218b97", # class: 'sd' - like a comment
        String.Double:             "#ffdf02",        # class: 's2'
        String.Escape:             "italic #ff087b",        # class: 'se'
        String.Heredoc:            "italic #3a771f",        # class: 'sh'
        String.Interpol:           "#ffdf02",        # class: 'si'
        String.Other:              "#ffdf02",        # class: 'sx'
        String.Regex:              "#ffe4a6",        # class: 'sr'
        String.Single:             "#ffdf02",        # class: 's1'
        String.Symbol:             "#ff9705",        # class: 'ss'

        Generic:                   "#ffffff",        # class: 'g'
        Generic.Deleted:           "#f8f8f8 bg:#4c0900",        # class: 'gd'
        Generic.Emph:              "bold italic #ffffff", # class: 'ge'
        Generic.Error:             "bold #ff1e00",        # class: 'gr'
        Generic.Heading:           "bold #000080",   # class: 'gh'
        Generic.Inserted:          "#f8f8f8 bg:#154f00",        # class: 'gi'
        Generic.Output:            "italic #ffffff", # class: 'go'
        Generic.Prompt:            "#22ff31",        # class: 'gp'
        Generic.Strong:            "bold #ffffff",   # class: 'gs'
        Generic.Subheading:        "bold #ff00ff",   # class: 'gu'
        Generic.Traceback:         "bold #f00bad",   # class: 'gt'
    }
