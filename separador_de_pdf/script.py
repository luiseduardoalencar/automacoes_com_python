import os
import shutil
import fitz  # PyMuPDF

def main():
    # Defina os caminhos para as pastas de entrada e saída
    input_folder = "COLOCA O CAMINHA DA PASTA COM TODOS OS PDFS AQUI(pasta)"
    output_folder_with_term = "COLOCA AQUI O CAMINHO DA PASTA ONDE VAI FICAR OS PDFS COM O TERMO(pastagd)"
    output_folder_without_term = "COLOCA AQUI O CAMINHO DA PASTA ONDE VAI FICAR OS PDFS SEM O TERMO(pastanogd)"
    
    # Crie as pastas de saída se elas não existirem
    os.makedirs(output_folder_with_term, exist_ok=True)
    os.makedirs(output_folder_without_term, exist_ok=True)
    
    # Percorra todos os arquivos na pasta de entrada
    for filename in os.listdir(input_folder):
        if filename.endswith(".PDF"):
            input_path = os.path.join(input_folder, filename)
            
            # Abra o PDF com PyMuPDF
            pdf_document = fitz.open(input_path)
            
            found_term = False
            # Percorra todas as páginas do PDF para verificar o termo
            for page_num in range(pdf_document.page_count):
                page = pdf_document.load_page(page_num)
                page_text = page.get_text("text")
                if "Termo_procurado" in page_text:
                    found_term = True
                    break
            
            pdf_document.close()
            
            # Determine o caminho da pasta de saída apropriada
            output_folder = output_folder_with_term if found_term else output_folder_without_term
            
            # Copie o arquivo para a pasta de saída apropriada
            output_path = os.path.join(output_folder, filename)
            shutil.copy(input_path, output_path)

if __name__ == "__main__":
    main()
