# PDF to Text Converter

O `pdf_to_txt.py` é um script Python para converter arquivos PDF em documentos de texto (TXT). Ele pode ser usado tanto como um módulo importado em outros programas quanto como um script independente.


## Funcionalidades

- Converte arquivos PDF em texto.
- Mostra o progresso da conversão página por página.
- Salva o texto extraído em um arquivo TXT com o mesmo nome base do arquivo PDF.


## Requisitos

Para executar este script, você precisa ter a biblioteca `pdfplumber` instalada. Para instalá-la, execute:

```bash
pip install pdfplumber
```


## Como usar

1. Como um script independente:
   - Execute na linha de comando: `python pdf_to_txt.py caminho_do_arquivo.pdf`
   - O script lê o arquivo PDF especificado e imprime o texto extraído no terminal.

### Exemplo 1 - Como um script independente

```bash
python pdf_to_txt.py caminho/do/seu/arquivo.pdf
```

2. Como um módulo importado:
   - Importe a classe em seu script: `from pdf_to_txt import PDFToTxtConverter`
   - Crie uma instância da classe com o caminho do arquivo PDF e chame o método `convert`.

### Exemplo 2 - Como um módulo importado

```bash
from pdf_to_txt import PDFToTxtConverter

converter = PDFToTxtConverter('caminho_do_seu_arquivo.pdf')
texto = converter.convert()
print(texto)
```


## Explicação do Código

- Importações: As bibliotecas pdfplumber e os são importadas para trabalhar com arquivos PDF e o sistema de arquivos, respectivamente.
- Classe PDFToTxtConverter: Define uma classe para converter PDF para TXT.
  - Método __init__: Construtor que inicializa a classe com o caminho do arquivo PDF.
  - Método convert: Responsável pela conversão do PDF para texto, imprimindo o progresso e tratando possíveis erros.
- Bloco if __name__ == "__main__": Permite que o script seja usado como um programa autônomo.
  - Argumentos da Linha de Comando: O script aceita o caminho do arquivo PDF como um argumento da linha de comando.
  - Processo de Conversão: O texto é extraído do PDF e salvo em um arquivo TXT com o mesmo nome base.

Este código fornece uma maneira clara e eficiente de converter arquivos PDF em arquivos de texto, com feedback útil para o usuário durante a execução.