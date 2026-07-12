from django.contrib import admin
from .models import Cutoff, CalculationHistory


@admin.register(Cutoff)
class CutoffAdmin(admin.ModelAdmin):
    list_display = (
        "college",
        "branch",
        "category",
        "year",
        "opening_cutoff",
        "closing_cutoff",
    )

    list_filter = (
        "year",
        "category",
        "college",
    )

    search_fields = (
        "college__college_name",
        "branch__branch_name",
    )


@admin.register(CalculationHistory)
class CalculationHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "cutoff",
        "category",
        "calculated_at",
    )

    list_filter = (
        "category",
        "calculated_at",
    )

    search_fields = (
        "student__username",
    )