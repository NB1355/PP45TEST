from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Event(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)          

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    # start_time = models.TimeField()
    # end_time = models.TimeField()
    # location = models.CharField(max_length=200)
    # organizer = models.CharField(max_length=100)
    # attendees = models.ManyToManyField('Attendee', blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # Optional: If you want to add an image to the event
    # event_image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.title

# class Attendee(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name
