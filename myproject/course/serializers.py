from rest_framework import serializers
from .models import Plan, Course

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['id', 'course_num', 'day_num', 'time', 'place', 'memo']

class CourseSerializer(serializers.ModelSerializer):
    # plans = PlanSerializer(read_only=True, many=True)
    # day_number = serializers.IntegerField(source='plans.day_number')
    # time = serializers.CharField(source='plans.time') #외래키로 연결된 테이블의 다른 필드가 필요할 때
    # place = serializers.CharField(source='plans.place')
    # memo = serializers.CharField(source='plans.memo')

    plans = serializers.SerializerMethodField()

    class Meta:
        model = Course
        # fields = ['id', 'title', 'plans', 'area', 'day_number', 'time', 'place', 'memo']
        fields = ['id', 'title', 'plans', 'area']

    def get_plans(self,obj):
        plans = Plan.objects.filter(course_num=obj)
        serializer = PlanSerializer(plans, many=True)
        return serializer.data
    
# class PlanDetailSerializer(serializers.ModelSerializer):
#     plans = serializers.SerializerMethodField()

#     class Meta:
#         model = Course
#         fields = ['plans']

#     def get_plans(self, obj):
#         plans = Plan.objects.filter(course_num=obj)
#         serializer = PlanSerializer(plans, many=True)
#         return serializer.data


    

# class CourseDetailSerializer(serializers.ModelSerializer):
#     class 

# class CourseSerializer(serializers.ModelSerializer):
#     planlist = serializers.SerializerMethodField()

#     class Meta:
#         model = Course
#         fields = ['id', 'title', 'plans', 'area', 'planlist']


#     def get_planlist(self, obj):
#         plan = obj.plans
#         return plan.day_number