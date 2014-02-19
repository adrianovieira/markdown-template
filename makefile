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

SHELL = bash

RM=/bin/rm
 
PANDOC=/usr/local/bin/pandoc
 
PANDOC_OPTIONS=--smart --standalone
 
PANDOC_HTML_OPTIONS=--to html5
PANDOC_PDF_OPTIONS=--template=$(PANDOC_TEMPLATE_LATEX)
PANDOC_DOCX_OPTIONS=
PANDOC_RTF_OPTIONS=
PANDOC_ODT_OPTIONS=
PANDOC_EPUB_OPTIONS=--to epub3
 
default: help
 
pdf : $(SOURCE_DOC_MD)
	@echo -n "Gerando $(SOURCE_DOC).pdf ... "
	@$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_PDF_OPTIONS) -o $(SOURCE_DOC).pdf $(PANDOC_METADATA_COMMON) $<
	@echo "[ OK ]"
	
odt : $(SOURCE_DOC_MD)
	@echo -n "Gerando $(SOURCE_DOC).odt ... "
	@$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_ODT_OPTIONS) -o $(SOURCE_DOC).odt $(PANDOC_METADATA_COMMON) $<
	@echo "[ OK ]"
 
# Targets and dependencies
 
.PHONY: all clean help
 
all : 
 
clean:
	- $(RM) *.pdf *.odt

help:
	@echo "  "
	@echo "Esse makefile automatiza a conversão de arquivos com conteúdo"
	@echo "padrão Pandoc/Markdown (.md), segundo metadados e estrutura"
	@echo "padrão definidos em 'Artigo-estrutura.md'."
	@echo "  "
	@echo "Makefile sintaxe: "
	@echo "- para mostrar esse help"
	@echo "  $$ make "
	@echo "     ou"
	@echo "  $$ make help"
	@echo "  "
	@echo "- para converter arquivos markdown (.md)"
	@echo '  o arquivo convertido será gerado na mesma pasta do arquivo .md'
	@echo "  "
	@echo '  $$ make pdf <artigo=Nome_do_arquivo[.md]> - converter para PDF;' 
	@echo '  $$ make odt <artigo=Nome_do_arquivo[.md]> - converter para ODT (TODO)' 
	@echo "  "
	@echo "  exemplo:"
	@echo '  $$ make pdf artigo=Artigo-estrutura' 
	@echo "     ou"
	@echo '  $$ make pdf artigo=Artigo-estrutura.md' 
	@echo "  "
