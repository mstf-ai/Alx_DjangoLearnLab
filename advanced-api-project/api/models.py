from django.db import models

class Author(models.Model):
    """
    نموذج المؤلف
    يحتوي على اسم المؤلف
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    نموذج الكتاب
    يحتوي على العنوان وسنة النشر ومرجع إلى المؤلف
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
