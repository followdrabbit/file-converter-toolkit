# pdf_to_yaml.py

# Importando as bibliotecas necessárias
import pdfplumber  # Para manipulação de arquivos PDF
import yaml        # Para criar e manipular dados no formato YAML
import os          # Para operações relacionadas ao sistema de arquivos

# Definindo a classe PDFToYAMLConverter
class PDFToYAMLConverter:
    def __init__(self, pdf_path):
        """
        Construtor da classe PDFToYAMLConverter.

        :param pdf_path: Caminho para o arquivo PDF que será convertido.
        """
        self.pdf_path = pdf_path  # Armazena o caminho do arquivo PDF

    def convert(self):
        """
        Realiza a conversão do arquivo PDF para YAML.

        :return: Uma string contendo o conteúdo do PDF no formato YAML.
        """
        data = {"páginas": []}  # Inicializa um dicionário para armazenar os dados do PDF
        try:
            # Abre o arquivo PDF para leitura
            with pdfplumber.open(self.pdf_path) as pdf:
                total_pages = len(pdf.pages)  # Calcula o total de páginas
                # Itera sobre cada página do PDF
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()  # Extrai o texto da página atual
                    if text:
                        # Adiciona o texto extraído ao dicionário
                        data["páginas"].append({"número_da_página": i + 1, "texto": text})
                    # Imprime o progresso da conversão
                    print(f"Processando página {i + 1}/{total_pages} para YAML")
            # Converte o dicionário para uma string YAML
            return yaml.dump(data, allow_unicode=True)
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
        converter = PDFToYAMLConverter(pdf_file)  # Cria uma instância do conversor
        yaml_output = converter.convert()  # Executa a conversão

        # Verifica se a conversão foi bem-sucedida
        if yaml_output:
            nome_base = os.path.splitext(pdf_file)[0]  # Extrai o nome base do arquivo PDF
            yaml_file = nome_base + ".yaml"  # Cria o nome do arquivo de saída YAML

            # Escreve o conteúdo YAML no arquivo
            with open(yaml_file, 'w', encoding='utf-8') as f:
                f.write(yaml_output)
            print(f"Arquivo convertido e salvo como {yaml_file}.")  # Informa o usuário sobre o sucesso da operação
        else:
            # Mensagem de erro se a conversão falhar
            print("Não foi possível converter o arquivo PDF.")
    else:
        # Mensagem de erro se nenhum arquivo for fornecido
        print("Por favor, forneça o caminho do arquivo PDF.")