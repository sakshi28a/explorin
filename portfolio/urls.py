from django.urls import path
from .views import (portfolio,accordian,bill,flex,trial12,weekly1) 

urlpatterns = [
	path('',portfolio,name='portfolio'),
	path('accordian',accordian,name='accordian'),
	path('bill',bill,name='bill'),
	path('flex',flex,name='flex'),
	path('trial12',trial12,name='trial12'),
	path('weekly1',weekly1,name='weekly1'),
]