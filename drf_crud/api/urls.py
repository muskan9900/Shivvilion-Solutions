from django.urls import path,include
from expense import views

urlpatterns = [
    path('get-transaction/',views.get_transaction),
    path('transaction/', views.TransactionAPI.as_view())
]

# as_view() makes the method of class declared in view to behave like functions 