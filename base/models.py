from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)

class RecipeInstruction(models.Model):
    r_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    time_stamp = models.CharField(max_length=8)
    seq_no = models.IntegerField()
    instruction = models.CharField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['r_id', 'seq_no'], name='unique_r_id_seq_no'
            )
        ]
