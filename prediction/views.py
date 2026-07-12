from django.shortcuts import render
from colleges.models import College, Branch
from cutoff.models import Cutoff


def prediction(request):

    districts = College.objects.values_list(
        "district",
        flat=True
    ).distinct()

    branches = Branch.objects.all()

    predictions = None
    chance = None

    if request.GET:

        cutoff = request.GET.get("cutoff")
        category = request.GET.get("category")
        branch = request.GET.get("branch")
        district = request.GET.get("district")

        predictions = Cutoff.objects.all()

        if district:
            predictions = predictions.filter(
                college__district=district
            )

        if branch:
            predictions = predictions.filter(
                branch_id=branch
            )

        if category:
            predictions = predictions.filter(
                category=category
            )

        if cutoff:
            cutoff = float(cutoff)

            predictions = predictions.filter(
                closing_cutoff__lte=cutoff
            ).order_by("-closing_cutoff")

            # Admission Chance
            if predictions.exists():

                college_cutoff = float(predictions.first().closing_cutoff)

                if cutoff >= college_cutoff + 2:
                    chance = "HIGH"

                elif cutoff >= college_cutoff:
                    chance = "MODERATE"

                else:
                    chance = "LOW"

    return render(
        request,
        "prediction/prediction.html",
        {
            "districts": districts,
            "branches": branches,
            "predictions": predictions,
            "chance": chance,
        }
    )