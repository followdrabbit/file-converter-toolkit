# PDF to YAML Converter

O `pdf_to_yaml.py` é um script Python projetado para converter arquivos PDF em documentos no formato YAML.


## Funcionalidades

- Converte arquivos PDF para o formato YAML.
- Extrai o texto de cada página do PDF e o organiza em um formato YAML estruturado.
- Exibe o progresso da conversão página por página.
- Salva o resultado em um arquivo YAML com o mesmo nome base do arquivo PDF.


## Requisitos

Para executar este script, as seguintes bibliotecas são necessárias:
- `pdfplumber` para leitura e manipulação de arquivos PDF.
- `PyYAML` para converter dados em YAML.

Você pode instalar essas dependências executando:

```bash
pip install pdfplumber PyYAML
```


## Como usar

1. Como um script independente:
   - Execute na linha de comando: `python pdf_to_yaml.py caminho_do_arquivo.pdf`
   - O script lê o arquivo PDF especificado e imprime o texto extraído no terminal.

### Exemplo 1 - Como um script independente

```bash
python pdf_to_yaml.py caminho_do_seu_arquivo.pdf
```

2. Como um módulo importado:
   - Importe a classe em seu script: `from pdf_to_yaml import PDFToTxtConverter`
   - Crie uma instância da classe com o caminho do arquivo PDF e chame o método `convert`.

### Exemplo 2 - Como um módulo importado

```bash
from pdf_to_yaml import PDFToYAMLConverter

converter = PDFToYAMLConverter('caminho_do_seu_arquivo.pdf')
yaml_output = converter.convert()
print(yaml_output)
```


## Explicação do Código

- Importações: Explica para que servem as bibliotecas pdfplumber, yaml e os.
- Classe PDFToYAMLConverter: Define a classe responsável pela conversão de PDF para YAML.
  - __init__: Construtor que inicializa a instância com o caminho do arquivo PDF.
  - convert: Método que abre o PDF, extrai o texto de cada página, organiza os dados em formato YAML e trata possíveis erros.
 - Bloco if __name__ == "__main__": Instruções para executar o script de forma independente, processando um arquivo PDF fornecido como argumento e salvando o resultado em um arquivo YAML.

Este código fornece uma maneira clara e eficiente de converter arquivos PDF em arquivos de texto, com feedback útil para o usuário durante a execução.