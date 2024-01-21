# PDF Converter Main Script

O `main.py` é um script Python centralizado para converter arquivos PDF em vários formatos, incluindo TXT, JSON, DOCX, XLSX e Markdown (MD).

## Funcionalidades

- Converte arquivos PDF em diversos formatos.
- Suporta conversão para os seguintes formatos: TXT, JSON, DOCX, XLSX, MD.
- Possibilita a conversão para todos os formatos de uma só vez com a opção `all`.
- Exibe o progresso da conversão e salva o arquivo convertido.

## Requisitos

O script requer várias bibliotecas externas, dependendo do formato de conversão desejado. Estas incluem `pdfplumber`, `openpyxl`, `python-docx` e outras. Instale as bibliotecas necessárias de acordo com os formatos de conversão desejados.


## Como usar

Para usar o `main.py`, forneça o caminho do arquivo PDF e o formato de saída desejado como argumentos da linha de comando:

```bash
python main.py caminho_do_seu_arquivo.pdf formato_desejado
```

### Exemplos de  utilização

Para converter para um formato específico

```bash
python main.py exemplo.pdf txt
python main.py exemplo.pdf json
```

Para converter para todos os formatos

```bash
python main.py exemplo.pdf all
```


## Estrutura do Código

- O script define funções individuais para cada formato de conversão (convert_to_txt, convert_to_json, etc.).
- Uma função save_output é usada para salvar os resultados da conversão em arquivos.
- A função convert_pdf é responsável por chamar a função de conversão apropriada com base no formato de saída fornecido.
- Argumentos da linha de comando são processados usando o módulo argparse.