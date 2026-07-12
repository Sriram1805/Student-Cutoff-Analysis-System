from django.contrib import admin
from .models import College, Branch


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = (
        "college_name",
        "district",
        "college_type",
    )

    list_filter = (
        "district",
        "college_type",
    )

    search_fields = (
        "college_name",
        "district",
    )


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        "branch_name",
    )

    search_fields = (
        "branch_name",
    )