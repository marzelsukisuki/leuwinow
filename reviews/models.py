from django.db import models

class CustomerReview(models.Model):
    name = models.CharField(max_length=100)
    profile_pic = models.URLField()
    rating = models.PositiveSmallIntegerField()
    review_text = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.rating} stars"
