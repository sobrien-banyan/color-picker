from django.urls import path
from paint_app.views import ColorPickerView



urlpatterns = [
    path('', ColorPickerView.as_view(), name='paint')
]







# # from sandwich_app.views import SandwichappView, IngredientsView
# from sandwich_app.views import SandwichappView, IngredientsView

# urlpatterns = [
#     path('', SandwichappView.as_view(), name='sandwich'),
#     path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name='ingredient_type'),
# ]

