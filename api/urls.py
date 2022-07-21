from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('getrecipeinfo/', view=views.getRecipeInfo),
    path('addrecipeinfo/', view=views.addRecipeInfo),
    path('getrecipeinstruction/', view=views.getRecipeInstruction),
    path('addrecipeinstruction/', view=views.addRecipeInstruction),
    path('playrecipe/', view=views.play),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
