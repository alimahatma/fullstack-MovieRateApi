from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()

    #! kode "no_of_ratings" adalah method yang mengembalikan jumlah raings yg diberikan pada movie
    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)
    
    #!kode ini berufngsi menghitung rating rata-rata movie yang diberikan oleh user 
    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars
            
        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0
        
    def __str__(self):
        return self.title


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    #! class Meta adalah kelas internal untuk memberikan meta data ke model
    #! membrikan informasi tambahan pada mode, tanpa harus menambah field atau metode baru ke model
    class Meta:
        unique_together = ('user','movie')
        index_together = ['user','movie']
        
