
# PDF to Markdown Converter

O `pdf_to_md.py` é um script Python para converter arquivos PDF em documentos no formato Markdown (MD).

## Funcionalidades

- Converte arquivos PDF em documentos Markdown (MD).
- Extrai o texto de cada página do PDF e o salva em formato Markdown.
- Exibe o progresso da conversão página por página.
- Salva o resultado em um arquivo Markdown com o mesmo nome base do arquivo PDF.

## Requisitos

Este script requer a biblioteca `pdfplumber`. Para instalá-la, execute:

```bash
pip install pdfplumber
```


## Como usar

1. Como um script independente:
   - Execute na linha de comando: `python pdf_to_md.py caminho_do_arquivo.pdf`
   - O script lê o arquivo PDF especificado e imprime o texto extraído no terminal.

### Exemplo 1 - Como um script independente

```bash
python pdf_to_md.py caminho_do_seu_arquivo.pdf
```

2. Como um módulo importado:
   - Importe a classe em seu script: `from pdf_to_md import PDFToTxtConverter`
   - Crie uma instância da classe com o caminho do arquivo PDF e chame o método `convert`.

### Exemplo 2 - Como um módulo importado

```bash
from pdf_to_md import PDFToMDConverter

converter = PDFToMDConverter('caminho_do_seu_arquivo.pdf')
md_output = converter.convert()
print(md_output)
```


## Explicação do Código

- Importações: Explica para que servem as bibliotecas pdfplumber e os.
- Classe PDFToMDConverter: Define a classe responsável pela conversão de PDF para MD.
  - __init__: Construtor que inicializa a instância com o caminho do arquivo PDF.
  - convert: Método que abre o PDF, extrai o texto de cada página, organiza os dados em formato MD e trata possíveis erros.
 - Bloco if __name__ == "__main__": Instruções para executar o script de forma independente, processando um arquivo PDF fornecido como argumento e salvando o resultado em um arquivo MD.

Este código fornece uma maneira clara e eficiente de converter arquivos PDF em arquivos de texto, com feedback útil para o usuário durante a execução.