# Makefile
# adaptado da fonte: https://gist.github.com/kristopherjohnson/7466917 
# Converts Markdown to other formats (HTML, PDF, DOCX, RTF, ODT, EPUB) using Pandoc
# <http://johnmacfarlane.net/pandoc/>
#
# Run "make" (or "make all") to convert to all other formats
#
# Run "make clean" to delete converted files

# Dados básicos
SOURCE_DOC := $(artigo:.md=)
PANDOC_METADATA_COMMON=Artigo-metadados-comuns.md
PANDOC_TEMPLATE_LATEX=template/latex.template
 
# nome do arquivo com .md
SOURCE_DOC_MD=$(SOURCE_DOC).md

RM=/bin/rm
 
PANDOC=/usr/local/bin/pandoc
 
PANDOC_OPTIONS=--smart --standalone
 
PANDOC_HTML_OPTIONS=--to html5
PANDOC_PDF_OPTIONS=--template=$(PANDOC_TEMPLATE_LATEX)
PANDOC_DOCX_OPTIONS=
PANDOC_RTF_OPTIONS=
PANDOC_ODT_OPTIONS=
PANDOC_EPUB_OPTIONS=--to epub3
 
#.DEFAULT:
#    echo Teste
 
pdf : $(SOURCE_DOC_MD)
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_PDF_OPTIONS) -o $(SOURCE_DOC).pdf $(PANDOC_METADATA_COMMON) $<
	
odt : $(SOURCE_DOC_MD)
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_ODT_OPTIONS) -o $(SOURCE_DOC).odt $(PANDOC_METADATA_COMMON) $<
 
# Targets and dependencies
 
.PHONY: all clean
 
all : 
 
clean:
	- $(RM) *.pdf *.odt
