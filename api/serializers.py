from rest_framework import serializers
from . models import *

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'url', 'lrn', 'first_name', 'middle_name', 'last_name', 'email', 'is_active', 'is_superuser', 'profile_img', 'role', 'class_id', 'mastery')
        
        
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ('id', 'name', 'code', 'teacher', 'date_created', 'batch', 'status' )


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ('__all__')
        
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('__all__')
        