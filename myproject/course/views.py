from django.shortcuts import render
from .models import Course, Plan
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import generics

from .serializers import CourseSerializer, PlanSerializer

# Create your views here.

# class PlanDetail(APIView):
#     def get(self, request):
#         plans = Plan.objects.()


# class CourseList(APIView):
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = [IsAuthenticatedOrReadOnly]

#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         # for c in Course.objects.all():
#         #     plans = Plan.objects.filter(pk=)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         planlist = self.request.plans
#         serializer.save(planlist=planlist)



class CourseDetail(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def get_object(self, pk):
        course = get_object_or_404(Course, pk=pk)
        return course
    
    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PlanList(generics.ListCreateAPIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']
        queryset = Plan.objects.filter(course_num = course_id)
        return queryset 
    
# class PlanDetail(APIView):
#     def get_object(self, pk):
#         course = get_object_or_404(Course, pk=pk)
#         return course
    
#     def get(self, request, pk):
#         course = self.get_object(pk)
#         serializer = CourseSerializer(course)
#         queryset = 

# class PlanDetail(generics.RetrieveAPIView):
#     queryset = Course.objects.filter(pk=pk)
#     serializer_class = PlanSerializer

#     #{id: , t:, p:, m: , daynum: ,...}

#     def get_queryset(self):
#         # day_number = self.request.GET.get('day')
#         queryset = Plan.objects.filter(day_num = self.kwargs['day'])
#         return queryset
    
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = [IsAuthenticatedOrReadOnly]

# @api_view(['GET'])
# def plan_detail(request, pk, day):
#     try:
#         # course_number = request.GET['pk']
#         # day_number = request.GET['day']
        
#         detail_plans = Plan.objects
#         # if course_number:
#         detail_plans = detail_plans.filter(course_num = pk)
#         # if day_number:
#         detail_plans = detail_plans.filter(day_num = day)
        
#         serializer = PlanSerializer(detail_plans)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     except Plan.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

class PlanDetail(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    def get_list(self, pk):
        plan = get_list_or_404(Plan, course_num=pk)
        return plan
    
    def get(self, request, pk, day):
        plan = self.get_list(pk)
        plan_detail = []
        for p in plan:
            if p.day_num == day:
                plan_detail.append(p)
        serializer = PlanSerializer(plan_detail, many=True)
        return Response(serializer.data)