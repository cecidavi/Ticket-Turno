# app/utils/pdf_generator.py

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
import os

from app.utils.qr_generator import generate_qr

def generate_ticket_pdf(curp, nombre_completo, turno_municipio, municipio, nivel, asunto):
    # Ruta donde se guardará el PDF
    output_dir = 'app/static/pdf'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_path = f'{output_dir}/{curp}_{turno_municipio}.pdf'

    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Títulos
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2, height - 60, "Secretaría de Educación")

    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(width / 2, height - 90, "Comprobante de Turno")

    # Línea divisoria
    c.setStrokeColor(colors.grey)
    c.line(50, height - 110, width - 50, height - 110)

    # Datos del Alumno
    c.setFont("Helvetica", 12)
    start_y = height - 140
    line_height = 20

    c.drawString(80, start_y, f"Nombre completo: {nombre_completo}")
    c.drawString(80, start_y - line_height, f"CURP: {curp}")
    c.drawString(80, start_y - 2 * line_height, f"Municipio: {municipio}")
    c.drawString(80, start_y - 3 * line_height, f"Nivel educativo: {nivel}")
    c.drawString(80, start_y - 4 * line_height, f"Asunto: {asunto}")
    c.drawString(80, start_y - 5 * line_height, f"Número de turno asignado: {turno_municipio}")

    # Código QR
    qr_img = generate_qr(curp)
    qr_reader = ImageReader(qr_img)
    qr_x = width - 200
    qr_y = height - 350
    c.drawImage(qr_reader, qr_x, qr_y, 120, 120)

    # Footer
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(colors.grey)
    c.drawCentredString(width / 2, 50, "Este comprobante es válido únicamente para el trámite de asignación de turno.")

    c.save()

    return pdf_path
