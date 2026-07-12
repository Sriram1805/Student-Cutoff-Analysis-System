from django.http import HttpResponse
from reportlab.pdfgen import canvas
from cutoff.models import CalculationHistory
from django.contrib.auth.decorators import login_required


@login_required
def download_pdf(request):

    latest = CalculationHistory.objects.filter(
        student=request.user
    ).order_by("-calculated_at").first()

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="Cutoff_Report.pdf"'

    pdf = canvas.Canvas(response)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(180, 800, "CutoffIQ Report")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(50, 750, f"Student Name : {request.user.first_name}")
    pdf.drawString(50, 725, f"Email : {request.user.email}")

    if latest:
        pdf.drawString(50, 680, f"Mathematics : {latest.mathematics}")
        pdf.drawString(50, 655, f"Physics : {latest.physics}")
        pdf.drawString(50, 630, f"Chemistry : {latest.chemistry}")
        pdf.drawString(50, 605, f"Category : {latest.category}")
        pdf.drawString(50, 580, f"TNEA Cutoff : {latest.cutoff}")
        pdf.drawString(50, 555, f"Calculated At : {latest.calculated_at}")

    pdf.save()

    return response