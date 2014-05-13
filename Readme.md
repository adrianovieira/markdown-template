Markdown Template
=================

Esse é um template que facilita a conversão de textos escritos em pandoc/markdown para outros formatos (PDF, ODT etc). Inicialmente está previsto e funcional a conversão apenas para PDF.

Estrutura de diretório do projeto
---------------------------------

~~~
makefile					Arquivo usado pelo comando *make* para conversão
							automatizada de arquivos fontes em pandoc/markdown
							(fontes).
template/	  				Repositório de *templates* a serem usados na conversão
							de fontes. Conforme tipo de arquivo destino.
template/latex.template 	Usado para converter para latex, PDF.
template/odt.template 		Usado para converter para ODT.
imagens/					Imagens padrão usadas pelo próprio *template*.  
bibliografia/				Arquivos de padrão de estilos (CSL) usados para formatar
							citações e referências.


Artigo-metadados-comuns.md	Arquivo contendo parâmetros de padrão geral para 
							conversão de textos

Artigo-estrutura.md			Exemplo de estrutura padrão para escrever artigos.
~~~

Forma de uso
------------

Para usar esse template é necessário possuir instalado na máquina as ferramentas:

```
- pandoc		Ferramento de conversão de e para múltiplos formatos.
- pdflatex		Utilitário para gerar PDF a partir de fonte em LaTeX.

- make			Utilitário para conversão automatiza de arquivos textos em 
				pandoc/markdown.
```

O arquivo *makefile* contem uma explicação simplificada e pode ser acessada digitando-se:

```bash
$ make
```

ou 

```bash
$ make help
```


Para utilizar o comando *make* para automatizar o processo de conversão de arquivos deve-se usar da forma descrita a seguir.


Sintaxe:

```bash
$ make <tipo_conversão> <artigo=nome_do_artigo.md>
```

Onde:

- **tipo_conversão**: tipos de conversão a ser realizada.  
- **nome_do_artigo**: nome do arquivo a ser convertido.


### Converter arquivos markdown (.md)  

Considere utilizar os comandos a seguir a partir do diretório onde estiver o fonte do arquivo a ser convertido.

```bash
$ make pdf <artigo=Nome_do_arquivo[.md]> - converter para PDF;
```

Exemplo:

```bash
  $ make pdf artigo=Artigo-estrutura
```

ou

```bash
  $ make pdf artigo=Artigo-estrutura.md
```

Também pode ser realizada a conversão a partir de diretório externo ao próprio diretório do template.

Supondo que haja uma estrutura própria para o artigo que está sendo criado a sintaxe precisará o local origem do arquivo "*makefile*" do template.

Sintaxe:

```bash
$ make -f <TEMPLATE_DIR_PATH/makefile> <tipo_conversão> <artigo=nome_do_artigo.md>
```


Onde:

 - ***TEMPLATE_DIR_PATH***: local onde estiver o arquivo *makefile* do template.

Exemplo:

Considerando a seguinte estrutura:

~~~
Meu_Primeiro_Artigo.md				Meu artigo conforme estrutura padrão.
imagens/							Imagens usadas no meu artigo somente.
	./print-screen1.jpg
	
markdown-template/
	./makefile
	./template/
	./imagens/
	./bibliografia/
	./Artigo-metadados-comuns.md
	./Artigo-estrutura.md	
~~~

Comando:

```bash
  $ make -f markdown-template/makefile pdf artigo=Meu_Primeiro_Artigo.md
```

Nesse caso será gerado o arquivo "*Meu_Primeiro_Artigo.pdf*" no diretório corrente.