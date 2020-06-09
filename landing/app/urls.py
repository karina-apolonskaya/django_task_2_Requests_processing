from django.urls import path, reverse

from app.views import landing, stats, index


urlpatterns = [
    path('', index, name='index'),
    path('landing/', landing, name='landing'),
    path('stats/', stats, name='stats'),
]
print(reverse('landing'))