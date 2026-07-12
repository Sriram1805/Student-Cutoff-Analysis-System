from django.db import models


COLLEGE_TYPE_CHOICES = [
    ("GOVT", "Government"),
    ("AIDED", "Government Aided"),
    ("SELF", "Self Financing"),
]


BRANCH_CHOICES = [
    ("CSE", "Computer Science and Engineering"),
    ("IT", "Information Technology"),
    ("AIDS", "Artificial Intelligence and Data Science"),
    ("ECE", "Electronics and Communication Engineering"),
    ("EEE", "Electrical and Electronics Engineering"),
    ("MECH", "Mechanical Engineering"),
    ("CIVIL", "Civil Engineering"),
]


class College(models.Model):
    college_code = models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        null=True
    )

    college_name = models.CharField(max_length=200)
    district = models.CharField(max_length=100)

    college_type = models.CharField(
        max_length=10,
        choices=COLLEGE_TYPE_CHOICES
    )

    def __str__(self):
        return self.college_name


class Branch(models.Model):
    college = models.ForeignKey(
        College,
        on_delete=models.CASCADE
    )

    branch_name = models.CharField(
        max_length=10,
        choices=BRANCH_CHOICES
    )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["college", "branch_name"],
                name="unique_branch_per_college",
            )
        ]

    def __str__(self):
        return f"{self.college.college_name} - {self.branch_name}"