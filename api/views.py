from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import InstructionSerializer, RecipeSerializer
from base.models import Recipe
from base.models import RecipeInstruction


@api_view(['GET'])
def getRecipeInfo(request):
    recipes  = Recipe.objects.all()
    serializer = RecipeSerializer(recipes,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addRecipeInfo(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def getRecipeInstruction(request):
    instructions  = RecipeInstruction.objects.all()
    serializer = InstructionSerializer(instructions,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def addRecipeInstruction(request):
    serializer =InstructionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
