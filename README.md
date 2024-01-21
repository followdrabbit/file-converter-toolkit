# File-Converter-Toolkit

Este projeto fornece um conjunto de ferramentas para converter arquivos PDF em vários formatos, incluindo TXT, JSON, DOCX, XLSX e Markdown (MD). É ideal para automatizar a conversão de documentos e facilitar o processamento de arquivos PDF em diferentes formatos.

## Características

- Conversão de PDF para:
  - Texto (TXT)
  - JSON
  - Microsoft Word (DOCX)
  - Microsoft Excel (XLSX)
  - Markdown (MD)
- Conversão de um arquivo para múltiplos formatos simultaneamente
- Interface de linha de comando fácil de usar

## Pré-requisitos

Antes de iniciar, certifique-se de que você tenha o Python instalado em sua máquina. Este projeto foi testado com Python 3.8. Além disso, algumas bibliotecas externas são necessárias, que podem ser instaladas via pip:

```bash
pip install pdfplumber openpyxl python-docx
```

## Instalação

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://link-para-seu-repositorio.git
cd nome-do-seu-repositorio
```

Instale todas as dependências necessárias executando:

```bash
pip install -r requirements.txt
```

## Instruções de uso

Para converter um arquivo PDF para um formato específico, use o script main.py com o seguinte comando:

```bash
python main.py caminho_do_seu_arquivo.pdf formato_desejado
```

Por exemplo, para converter para TXT:

```bash
python main.py exemplo.pdf txt
```

Para converter para todos os formatos disponíveis:

```bash
python main.py exemplo.pdf all
```


## Estrutura do Projeto

```bash
pdf-txt-converter/
│
├── docs/
│   ├── main_doc.md  # Documentação adicional sobre o main.py
│   ├── pdf_to_docx_doc.md # Documentação adicional sobre o pdf_to_docx.py
│   ├── pdf_to_json_doc.md # Documentação adicional sobre o pdf_to_json.py
│   ├── pdf_to_md_doc.md # Documentação adicional sobre o pdf_to_md.py
│   ├── pdf_to_txt_doc.md # Documentação adicional sobre o pdf_to_txt.py
│   ├── pdf_to_xlsx_doc.md # Documentação adicional sobre o pdf_to_xlsx.py
│   ├── pdf_to_yaml_doc.md # Documentação adicional sobre o pdf_to_yaml.py
├── src/
│   ├── converters/
│   │   ├── pdf_to_docx.py
│   │   ├── pdf_to_json.py
│   │   ├── pdf_to_md.py
│   │   ├── pdf_to_txt.py
│   │   ├── pdf_to_xlsx.py
│   │   ├── pdf_to_yaml.py
├── main.py  # Script principal para interagir com os conversores
├── README.md             # Documentação do projeto
├── requirements.txt      # Dependências do projeto
├── venv/                 # Ambiente virtual
└── .gitignore            # Arquivo para ignorar certos arquivos no git
```