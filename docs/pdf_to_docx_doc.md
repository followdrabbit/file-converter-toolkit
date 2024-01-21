# PDF to DOCX Converter

O `pdf_to_docx.py` é um script Python projetado para converter arquivos PDF em documentos do Microsoft Word (formato DOCX).

## Funcionalidades

- Converte arquivos PDF em documentos DOCX (Microsoft Word).
- Extrai o texto de cada página do PDF e o salva em um documento DOCX.
- Exibe o progresso da conversão página por página.
- Salva o resultado em um arquivo DOCX com o mesmo nome base do arquivo PDF.

## Requisitos

Para executar este script, as seguintes bibliotecas são necessárias:
- `pdfplumber` para leitura e manipulação de arquivos PDF.
- `python-docx` para criar e manipular documentos DOCX.

Você pode instalar essas dependências executando:

```bash
pip install pdfplumber python-docx
```


## Como usar

1. Como um script independente:
   - Execute na linha de comando: `python pdf_to_docx.py caminho_do_arquivo.pdf`
   - O script lê o arquivo PDF especificado e imprime o texto extraído no terminal.

### Exemplo 1 - Como um script independente

```bash
python pdf_to_docx.py caminho_do_seu_arquivo.pdf
```

2. Como um módulo importado:
   - Importe a classe em seu script: `from pdf_to_docx import PDFToTxtConverter`
   - Crie uma instância da classe com o caminho do arquivo PDF e chame o método `convert`.

### Exemplo 2 - Como um módulo importado

```bash
from pdf_to_docx import PDFToDOCXConverter

converter = PDFToDOCXConverter('caminho_do_seu_arquivo.pdf')
docx_file = converter.convert()
print(f"Documento DOCX gerado: {docx_file}")
```


## Explicação do Código

- Importações: Explica para que servem as bibliotecas pdfplumber, docx e os.
- Classe PDFToMDConverter: Define a classe responsável pela conversão de PDF para docx.
  - __init__: Construtor que inicializa a instância com o caminho do arquivo PDF.
  - convert: Método que abre o PDF, extrai o texto de cada página, organiza os dados em formato MD e trata possíveis erros.
 - Bloco if __name__ == "__main__": Instruções para executar o script de forma independente, processando um arquivo PDF fornecido como argumento e salvando o resultado em um arquivo docx.

Este código fornece uma maneira clara e eficiente de converter arquivos PDF em arquivos de texto, com feedback útil para o usuário durante a execução.