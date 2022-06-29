(TeX-add-style-hook
 "teacher"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("sourceserifpro" "default" "regular" "black") ("fontenc" "T1") ("microtype" "final") ("nowidow" "all") ("footmisc" "hang" "flushmargin" "stable" "multiple") ("geometry" "margin=1.25in") ("tcolorbox" "most")))
   (TeX-run-style-hooks
    "titling"
    "bookmark"
    "titletoc"
    "inputenc"
    "sourceserifpro"
    "fontenc"
    "xcolor"
    "microtype"
    "fancyhdr"
    "lastpage"
    "float"
    "nowidow"
    "xparse"
    "parskip"
    "sectsty"
    "footmisc"
    "manyfoot"
    "relsize"
    "breakcites"
    "geometry"
    "setspace"
    "tcolorbox")
   (TeX-add-symbols
    "oldsection"
    "oldparagraph"
    "oldsubparagraph"))
 :latex)

