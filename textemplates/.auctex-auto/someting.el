(TeX-add-style-hook
 "someting"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("report" "11pt" "letterpaper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("sourceserifpro" "default" "regular" "black") ("fontenc" "T1") ("microtype" "final") ("geometry" "margin=1in" "headsep=\\baselineskip" "includehead" "includefoot") ("pgfornament" "object=vectorian")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "report"
    "rep11"
    "inputenc"
    "sourceserifpro"
    "fontenc"
    "amsmath"
    "lastpage"
    "multicol"
    "fancyhdr"
    "amssymb"
    "sectsty"
    "titlesec"
    "csquotes"
    "etoolbox"
    "lipsum"
    "tikz"
    "microtype"
    "graphicx"
    "geometry"
    "xcolor"
    "pgfornament"
    "hyperref"
    "minted")
   (TeX-add-symbols
    '("sectionlinetwo" 2)
    "ornamentbreak")
   (LaTeX-add-xcolor-definecolors
    "draculabg"
    "draculacl"
    "draculafg"
    "draculacomment"
    "draculacyan"
    "draculagreen"
    "draculaorange"
    "draculapink"
    "draculapurple"
    "draculared"
    "draculayellow"))
 :latex)

