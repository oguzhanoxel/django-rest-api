from rest_framework import serializers, viewsets

from .models import Lecture

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('id', 'title', 'description', 'lecturer_name', 'date', 'slides_url', 'is_required', 'created_at', 'updated_at')

class LectureViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = LectureSerializer
