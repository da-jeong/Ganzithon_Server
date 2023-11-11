from rest_framework import serializers
from .models import Plan, Course

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'course_num', 'day_num', 'time', 'place', 'memo']

class CourseSerializer(serializers.ModelSerializer):
    plans = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'plans', 'area']

    def get_plans(self,obj):
        plans = Plan.objects.filter(course_num=obj)
        serializer = PlanSerializer(plans, many=True)
        return serializer.data