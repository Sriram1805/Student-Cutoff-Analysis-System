from django.shortcuts import render
from .models import CalculationHistory
from django.contrib.auth.decorators import login_required


def calculator(request):

    cutoff = None
    
    if request.method == "POST":
        
        maths = int(request.POST["maths"])
        physics = int(request.POST["physics"])
        chemistry = int(request.POST["chemistry"])
        category = request.POST["category"]

        cutoff = maths + (physics / 2) + (chemistry / 2)

        if request.user.is_authenticated:

            CalculationHistory.objects.create(
                student=request.user,
                mathematics=maths,
                physics=physics,
                chemistry=chemistry,
                cutoff=cutoff,
                category=category
            )

    return render(
        request,
        "cutoff/calculator.html",
        {"cutoff": f"{cutoff:.2f}" if cutoff else None}
    )

@login_required
def history(request):

    calculations = CalculationHistory.objects.filter(
        student=request.user
    ).order_by("-calculated_at")

    return render(
        request,
        "cutoff/history.html",
        {
            "calculations": calculations
        }
    )