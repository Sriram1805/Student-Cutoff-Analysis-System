from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cutoff.models import CalculationHistory

@login_required
def dashboard(request):
    calculations = CalculationHistory.objects.filter(
        student=request.user
    ).order_by("-calculated_at")

    total_calculations = calculations.count()

    latest_cutoff = None

    if calculations.exists():
        latest_cutoff = calculations.first().cutoff

    return render(
        request,
        "user_dashboard/dashboard.html",
        {
            "calculations": calculations[:5],
            "total_calculations": total_calculations,
            "latest_cutoff": latest_cutoff,
        },
    )
    