from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.utils import timezone
from .models import Task, Upload
from .serializers import TaskSerializer, UploadSerializer
import pandas as pd

class UploadExcelView(APIView):
    def post(self, request):
        file_obj = request.FILES.get('file')
        if not file_obj:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)
        upload = Upload.objects.create(file=file_obj)
        try:
            df = pd.read_excel(upload.file.path)
            for idx, row in df.iterrows():
                Task.objects.create(
                    day_of_week=row['day_of_week'],
                    time=row['time'],
                    description=row['description'],
                    completed=False
                )
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'uploaded'}, status=status.HTTP_201_CREATED)

class TodayTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        today = timezone.now().strftime('%A')
        return Task.objects.filter(day_of_week=today)

class AllTasksView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CompleteTaskView(APIView):
    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            task.completed = request.data.get('completed', True)
            task.save()
            return Response({'status': 'updated'})
        except Task.DoesNotExist:
            return Response({'error': 'Not found'}, status=404)
