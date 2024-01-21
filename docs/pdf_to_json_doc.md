# PDF to JSON Converter

O `pdf_to_json.py` é um script Python para converter arquivos PDF em formato JSON, preservando o texto de cada página.


## Funcionalidades

- Converte arquivos PDF em documentos JSON.
- Extrai o texto de cada página do PDF e o organiza em um formato JSON estruturado.
- Exibe o progresso da conversão página por página.
- Salva o resultado em um arquivo JSON com o mesmo nome base do arquivo PDF.


## Requisitos

Este script requer a biblioteca `pdfplumber`. Para instalá-la, execute:

```bash
pip install pdfplumber
```



## Como usar

1. Como um script independente:
   - Execute na linha de comando: `python pdf_to_json.py caminho_do_arquivo.pdf`
   - O script lê o arquivo PDF especificado e imprime o texto extraído no terminal.

### Exemplo 1 - Como um script independente

```bash
python pdf_to_json.py caminho_do_seu_arquivo.pdf
```

2. Como um módulo importado:
   - Importe a classe em seu script: `from pdf_to_json import PDFToTxtConverter`
   - Crie uma instância da classe com o caminho do arquivo PDF e chame o método `convert`.

### Exemplo 2 - Como um módulo importado

```bash
from pdf_to_json import PDFToJsonConverter

converter = PDFToJsonConverter('caminho_do_seu_arquivo.pdf')
json_output = converter.convert()
print(json_output)
```


## Explicação do Código

- Classe PDFToJsonConverter: Responsável pela conversão de PDF para JSON.
  - Método __init__: Inicializa a instância com o caminho do arquivo PDF.
  - Método convert: Abre o PDF, extrai o texto de cada página, e o armazena em um formato JSON. O progresso é impresso na tela. Em caso de erro, um aviso é exibido.
- Bloco if __name__ == "__main__": Permite que o script seja executado diretamente da linha de comando. Aceita o caminho do arquivo PDF como um argumento e salva o resultado em um arquivo JSON.