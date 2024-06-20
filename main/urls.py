from django.urls import path
from .views import (
    home, about, faq,
    feature, contact, service,
    project, team, testimonial, not_found
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
    path('feature/', feature, name='feature'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('project/', project, name='project'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial)'),
    path('not_found/', not_found, name='not_found)'),
]