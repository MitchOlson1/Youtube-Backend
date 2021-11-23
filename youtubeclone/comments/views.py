from django.http import response
from .models import Comment
from rest_framework.response import Response
from .serializers import VideoSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class Comment(APIView):
    
    def get (self, request):
        comment = Comment.objects.all()
        serializer = VideoSerializer(comment, many = True)
        return Response (serializer.data)

    def post(self, request, pk):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.data, status = status.HTTP_400_Bad_REQUEST)
    
    




class VideoDescription(APIView):
    pass

