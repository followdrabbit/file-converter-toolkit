# pdf_to_docx.py

# Importando as bibliotecas necessárias
import pdfplumber  # Para manipulação de arquivos PDF
from docx import Document  # Para criar documentos do Word (DOCX)
import os  # Para operações relacionadas ao sistema de arquivos

# Definindo a classe PDFToDOCXConverter
class PDFToDOCXConverter:
    def __init__(self, pdf_path):
        """
        Construtor da classe PDFToDOCXConverter.

        :param pdf_path: Caminho para o arquivo PDF que será convertido.
        """
        self.pdf_path = pdf_path  # Armazena o caminho do arquivo PDF

    def convert(self):
        """
        Realiza a conversão do arquivo PDF para DOCX (Microsoft Word).

        :return: O caminho do arquivo DOCX gerado.
        """
        doc = Document()  # Cria um novo documento DOCX
        try:
            # Abre o arquivo PDF para leitura
            with pdfplumber.open(self.pdf_path) as pdf:
                total_pages = len(pdf.pages)  # Calcula o total de páginas
                # Itera sobre cada página do PDF
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()  # Extrai o texto da página atual
                    if text:
                        doc.add_paragraph(text)  # Adiciona o texto ao documento DOCX
                    # Imprime o progresso da conversão
                    print(f"Processando página {i + 1}/{total_pages} para DOCX")
            
            # Define o nome do arquivo DOCX baseado no nome do arquivo PDF
            docx_filename = os.path.splitext(self.pdf_path)[0] + '.docx'
            doc.save(docx_filename)  # Salva o documento DOCX
            return docx_filename  # Retorna o caminho do arquivo DOCX
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
        converter = PDFToDOCXConverter(pdf_file)  # Cria uma instância do conversor
        docx_file = converter.convert()  # Executa a conversão

        # Verifica se a conversão foi bem-sucedida
        if docx_file:
            print(f"Arquivo convertido e salvo como {docx_file}.")  # Informa o usuário sobre o sucesso da operação
        else:
            # Mensagem de erro se a conversão falhar
            print("Não foi possível converter o arquivo PDF.")
    else:
        # Mensagem de erro se nenhum arquivo for fornecido
        print("Por favor, forneça o caminho do arquivo PDF.")
