from django.db import models
from colleges.models import College, Branch
from django.contrib.auth.models import User


CATEGORY_CHOICES = [
    ("OC", "Open Competition"),
    ("BC", "Backward Class"),
    ("BCM", "Backward Class Muslim"),
    ("MBC", "Most Backward Class"),
    ("SC", "Scheduled Caste"),
    ("SCA", "Scheduled Caste Arunthathiyar"),
    ("ST", "Scheduled Tribe"),
]


class Cutoff(models.Model):
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE
    )

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE
    )

    year = models.PositiveIntegerField()

    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES
    )

    opening_cutoff = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    closing_cutoff = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "college",
                    "branch",
                    "year",
                    "category",
                ],
                name="unique_cutoff_record",
            )
        ]

    def __str__(self):
        return f"{self.college.college_name} - {self.branch.branch_name} ({self.category})"
    
class CalculationHistory(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    mathematics = models.PositiveIntegerField()

    physics = models.PositiveIntegerField()

    chemistry = models.PositiveIntegerField()

    cutoff = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    category = models.CharField(
        max_length=3,
        choices=CATEGORY_CHOICES
    )

    calculated_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.username} - {self.cutoff}"