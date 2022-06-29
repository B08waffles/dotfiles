(TeX-add-style-hook
 "powerlake"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("report" "11pt" "letterpaper")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("sourceserifpro" "default" "regular" "black") ("fontenc" "T1") ("microtype" "final") ("geometry" "margin=1in" "headsep=\\baselineskip" "includehead" "includefoot") ("pgfornament" "object=vectorian")))
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
    "minted"
    "pgfornament"
    "hyperref")
   (TeX-add-symbols
    '("sectionlinetwo" 2)
    "ornamentbreak"))
 :latex)

