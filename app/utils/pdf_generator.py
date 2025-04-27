from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os

from app.utils.qr_generator import generate_qr

def generate_ticket_pdf(curp, nombre_completo, turno_municipio, municipio, nivel, asunto):
    # Ruta donde se guardará el PDF
    if not os.path.exists('app/static/pdf'):
        os.makedirs('app/static/pdf')

    pdf_path = f'app/static/pdf/{curp}_{turno_municipio}.pdf'

    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 100, "Comprobante de Turno")

    c.setFont("Helvetica", 12)
    c.drawString(100, height - 150, f"Nombre completo: {nombre_completo}")
    c.drawString(100, height - 170, f"CURP: {curp}")
    c.drawString(100, height - 190, f"Municipio: {municipio}")
    c.drawString(100, height - 210, f"Nivel educativo: {nivel}")
    c.drawString(100, height - 230, f"Asunto: {asunto}")
    c.drawString(100, height - 250, f"Número de turno: {turno_municipio}")

    # Generar código QR con el CURP
    qr_img = generate_qr(curp)
    qr_reader = ImageReader(qr_img)
    c.drawImage(qr_reader, width - 200, height - 300, 150, 150)

    c.save()

    return pdf_path
