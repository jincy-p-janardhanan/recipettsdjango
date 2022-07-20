from django.urls import path
from . import views

urlpatterns = [
    path('getrecipeinfo/',view=views.getRecipeInfo),
    path('addrecipeinfo/',view=views.addRecipeInfo),
    path('getrecipeinstruction/',view=views.getRecipeInstruction),
    path('addrecipeinstruction/',view=views.addRecipeInstruction),

]