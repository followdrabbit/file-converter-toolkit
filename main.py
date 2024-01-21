# main.py

# Importando as bibliotecas necessárias
import argparse  # Para análise de argumentos da linha de comando
import os        # Para operações relacionadas ao sistema de arquivos
import sys       # Para acessar algumas configurações e funções específicas do sistema

# Funções individuais para cada formato de conversão
def convert_to_txt(input_file):
    """Converte um PDF para um arquivo de texto (TXT)."""
    from src.converters.pdf_to_txt import PDFToTxtConverter
    converter = PDFToTxtConverter(input_file)
    return converter.convert(), os.path.splitext(input_file)[0] + '.txt'

def convert_to_json(input_file):
    """Converte um PDF para um arquivo JSON."""
    from src.converters.pdf_to_json import PDFToJsonConverter
    converter = PDFToJsonConverter(input_file)
    return converter.convert(), os.path.splitext(input_file)[0] + '.json'

def convert_to_docx(input_file):
    """Converte um PDF para um documento do Word (DOCX)."""
    from src.converters.pdf_to_docx import PDFToDOCXConverter
    converter = PDFToDOCXConverter(input_file)
    converter.convert()
    return None, os.path.splitext(input_file)[0] + '.docx'

def convert_to_xlsx(input_file):
    """Converte um PDF para uma planilha Excel (XLSX)."""
    from src.converters.pdf_to_xlsx import PDFToXLSXConverter
    converter = PDFToXLSXConverter(input_file)
    converter.convert()
    return None, os.path.splitext(input_file)[0] + '.xlsx'

def convert_to_md(input_file):
    """Converte um PDF para um arquivo Markdown (MD)."""
    from src.converters.pdf_to_md import PDFToMDConverter
    converter = PDFToMDConverter(input_file)
    return converter.convert(), os.path.splitext(input_file)[0] + '.md'

def save_output(output, file_name):
    """Salva o conteúdo de saída em um arquivo."""
    if output:
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(output)
        print(f"Arquivo convertido e salvo como {file_name}.")
    else:
        print("Falha na conversão do arquivo.")

def convert_pdf(input_file, output_format):
    """
    Direciona a conversão do arquivo PDF para o formato especificado.
    Se 'all' for especificado, converte para todos os formatos.
    """
    # Dicionário mapeando formatos de saída para suas respectivas funções
    conversion_functions = {
        'txt': convert_to_txt,
        'json': convert_to_json,
        'docx': convert_to_docx,
        'xlsx': convert_to_xlsx,
        'md': convert_to_md
    }

    # Executa a conversão para todos os formatos, se 'all' for escolhido
    if output_format == 'all':
        for format, function in conversion_functions.items():
            output, file_name = function(input_file)
            if output is not None:
                save_output(output, file_name)
    # Executa a conversão para um formato específico
    elif output_format in conversion_functions:
        output, file_name = conversion_functions[output_format](input_file)
        if output is not None:
            save_output(output, file_name)
    else:
        print(f"Formato '{output_format}' não suportado.")
        sys.exit(1)

# Bloco principal: Executa o script como um programa independente
if __name__ == "__main__":
    # Configuração do analisador de argumentos de linha de comando
    parser = argparse.ArgumentParser(description="Converter PDF para diferentes formatos.")
    parser.add_argument("input_file", help="Caminho do arquivo PDF para ser convertido.")
    parser.add_argument("output_format", choices=['txt', 'json', 'docx', 'xlsx', 'md', 'all'], help="Formato de saída desejado.")
    
    args = parser.parse_args()  # Analisa os argumentos fornecidos
    convert_pdf(args.input_file, args.output_format)  # Chama a função de conversão
