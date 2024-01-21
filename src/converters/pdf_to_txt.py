# pdf_to_txt.py

# Importando as bibliotecas necessárias
import pdfplumber  # Para manipulação de arquivos PDF
import os  # Para operações relacionadas ao sistema de arquivos

# Definindo a classe PDFToTxtConverter
class PDFToTxtConverter:
    def __init__(self, pdf_path):
        """
        Construtor da classe PDFToTxtConverter.

        :param pdf_path: Caminho para o arquivo PDF que será convertido.
        """
        self.pdf_path = pdf_path  # Armazena o caminho do arquivo PDF

    def convert(self):
        """
        Realiza a conversão do arquivo PDF para texto (TXT).

        :return: O texto extraído do arquivo PDF.
        """
        text_output = ""  # Inicializa a variável para armazenar o texto extraído
        try:
            # Abre o arquivo PDF para leitura
            with pdfplumber.open(self.pdf_path) as pdf:
                total_pages = len(pdf.pages)  # Calcula o total de páginas
                # Itera sobre cada página do PDF
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()  # Extrai o texto da página atual
                    if text:
                        text_output += text + "\n"  # Adiciona o texto ao acumulador
                    # Imprime o progresso da conversão
                    print(f"Processando página {i + 1}/{total_pages} para TXT")
            return text_output  # Retorna o texto extraído após processar todas as páginas
        except Exception as e:
            # Captura e imprime qualquer erro que ocorra durante o processamento
            print(f"Erro ao processar o arquivo PDF: {e}")
            return None  # Retorna None em caso de erro

# Este bloco de código é executado se o script for o principal executado
if __name__ == "__main__":
    import sys  # Importa a biblioteca sys para manipulação de argumentos da linha de comando

    # Verifica se um caminho de arquivo foi fornecido como argumento
    if len(sys.argv) > 1:
        pdf_file = sys.argv[1]  # Armazena o caminho do arquivo PDF fornecido
        converter = PDFToTxtConverter(pdf_file)  # Cria uma instância do conversor
        text = converter.convert()  # Executa a conversão

        # Verifica se a conversão foi bem-sucedida
        if text:
            nome_base = os.path.splitext(pdf_file)[0]  # Extrai o nome base do arquivo PDF
            txt_file = nome_base + ".txt"  # Cria o nome do arquivo de saída TXT

            # Escreve o texto extraído no arquivo TXT
            with open(txt_file, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Arquivo convertido e salvo como {txt_file}.")  # Informa o usuário sobre o sucesso da operação
        else:
            # Mensagem de erro se a conversão falhar
            print("Não foi possível converter o arquivo PDF.")
    else:
        # Mensagem de erro se nenhum arquivo for fornecido
        print("Por favor, forneça o caminho do arquivo PDF.")
