import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InstructionSerializer, RecipeSerializer
from base.models import Recipe
from base.models import RecipeInstruction
from services import tts_service
from django.http import HttpResponse

@api_view(['GET'])
def getRecipeInfo(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addRecipeInfo(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getRecipeInstruction(request):
    instructions = RecipeInstruction.objects.all()
    serializer = InstructionSerializer(instructions, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addRecipeInstruction(request):
    serializer = InstructionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['get'])
def play(request):
    r_id = request.GET.get('r_id', None)
    recipe_instructions = RecipeInstruction.objects.filter(r_id=r_id)
    filename = tts_service.getRecipeAudio(recipe_instructions)
    file =  open(filename, "rb").read()
    response = HttpResponse(file, content_type='audio/mpeg')
    # response['Content-Disposition'] = 'attachment; filename='+filename
    try:
            os.remove(filename)
    except:
        print(filename + 'not deleted.')

    return response
    