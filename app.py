from fpdf import FPDF
class PDF(FPDF):
    def __init__(self, image_file):
        super().__init__()
        self.image_file = image_file

    def header(self):
        
        pass

    def footer(self):
        
        pass

    def add_image(self):
        self.add_page()
        self.image(self.image_file, x = 10, y = 8, w = 190)  

#Aqui é o caminho para Imagem
image_path = "C:\\Users\\Remakker\\Desktop\\image.png"
pdf = PDF(image_path)
pdf.add_image()
pdf.output("saida.pdf")
print("PDF gerado com sucesso!")
