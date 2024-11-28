from django.urls import path
from .views import Register, GetSlots

urlpatterns = [
    path('',Register.as_view(), name='Register'),
    path('getslots/<int:candidate_id>/<int:interviewer_id>/', GetSlots.as_view(), name='getslots'),
]
