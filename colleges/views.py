from django.shortcuts import render
from .models import College, Branch
from cutoff.models import Cutoff


def colleges(request):

    districts = College.objects.values_list(
        "district",
        flat=True
    ).distinct()

    branches = Branch.objects.all()

    cutoffs = Cutoff.objects.all()

    district = request.GET.get("district")
    branch = request.GET.get("branch")
    category = request.GET.get("category")

    if district:
        cutoffs = cutoffs.filter(
            college__district=district
        )

    if branch:
        cutoffs = cutoffs.filter(
            branch_id=branch
        )

    if category:
        cutoffs = cutoffs.filter(
            category=category
        )

    return render(
        request,
        "colleges/colleges.html",
        {
            "districts": districts,
            "branches": branches,
            "cutoffs": cutoffs,
        }
    )