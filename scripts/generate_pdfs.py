from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        # Cabeçalho decorativo simples
        self.set_draw_color(180, 180, 180)
        self.line(10, 8, 200, 8)
        self.ln(5)

    def footer(self):
        # Rodapé simples com número da página
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        page_text = f'Página {self.page_no()}'
        clean_page_text = page_text.encode('latin-1', 'replace').decode('latin-1')
        self.cell(0, 10, clean_page_text, 0, 0, 'C')

def create_pdf(filename, title, content_sections):
    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Título do Documento
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(33, 33, 33)
    clean_title = title.encode('latin-1', 'replace').decode('latin-1')
    pdf.cell(0, 15, clean_title, ln=True, align='C')
    pdf.ln(5)
    
    # Conteúdo por seções
    for heading, paragraph in content_sections:
        # Título da Seção
        pdf.set_font("Arial", 'B', 12)
        pdf.set_text_color(60, 60, 60)
        clean_heading = heading.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(0, 8, clean_heading, ln=True)
        pdf.ln(1)
        
        # Parágrafo de Conteúdo
        pdf.set_font("Arial", size=10)
        pdf.set_text_color(80, 80, 80)
        clean_paragraph = paragraph.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 5, clean_paragraph)
        pdf.ln(4)
        
    pdf.output(filename)
    print(f"PDF '{filename}' gerado com sucesso!")

# Dados para o PDF das Políticas da Empresa
empresa_content = [
    ("1. Missão, Visão e Valores", 
     "Nossa missão é oferecer soluções de alta qualidade, garantindo a satisfação e o sucesso de nossos clientes. Buscamos ser referência em inovação e tecnologia, atuando sempre com integridade, transparência e respeito socioambiental."),
    ("2. Código de Conduta", 
     "Todos os colaboradores devem agir com profissionalismo, ética e honestidade. É proibido qualquer tipo de discriminação, assédio ou comportamento hostil no ambiente de trabalho. Prezamos pelo respeito mútuo em todas as relações."),
    ("3. Uso de Equipamentos e Segurança da Informação", 
     "Os equipamentos fornecidos pela empresa (computadores, celulares, etc.) são para uso estritamente profissional. Toda informação interna é confidencial e não deve ser compartilhada com terceiros sem autorização prévia por escrito."),
    ("4. Política de Trabalho Híbrido", 
     "Nossa empresa adota o modelo de trabalho híbrido. Os dias presenciais devem ser alinhados diretamente com a liderança da equipe, visando a colaboração presencial e a integração do time.")
]

# Dados para o PDF de Políticas do RH
rh_content = [
    ("1. Recrutamento e Seleção", 
     "Nosso processo seletivo é baseado em mérito, competência e potencial de crescimento do candidato. Buscamos promover a diversidade e a inclusão em todas as nossas vagas, garantindo igualdade de oportunidades a todos."),
    ("2. Benefícios e Remuneração", 
     "Oferecemos uma remuneração competitiva e compatível com o mercado de atuação, além de benefícios corporativos como vale-refeição, assistência médica, seguro de vida e incentivos ao desenvolvimento educacional."),
    ("3. Férias e Licenças", 
     "O agendamento de férias deve ser acordado com o gestor direto com pelo menos 30 dias de antecedência. Respeitamos todas as licenças previstas pela legislação vigente (maternidade, paternidade, licença médica, etc.)."),
    ("4. Desenvolvimento e Avaliação de Desempenho", 
     "Realizamos avaliações periódicas de desempenho para acompanhar a evolução profissional de nossos colaboradores, identificando oportunidades de treinamento, plano de carreira, promoções e novos desafios.")
]

if __name__ == "__main__":
    # Gerando os PDFs com nomes exatos solicitados pelo usuário
    create_pdf("politicas da empresa.pdf", "Políticas da Empresa", empresa_content)
    create_pdf("politicas do rh.pdf", "Políticas de Recursos Humanos (RH)", rh_content)
