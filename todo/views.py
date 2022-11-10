
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

class AllPlansAPIView(APIView):
   permission_classes = [IsAuthenticated]
   def get(self, request):
        plans=Plan.objects.all()
        serializer=PlanSerializer(plans, many=True)
        return Response(serializer.data)

   def post(self, request):
        plan=request.data
        serializer=PlanSerializer(data=plan)
        if serializer.is_valid():
           serializer.save(user=request.user)
           natija = {"xabar": "Saqlandi!",
                     "qoshilgan malumot": serializer.data}
           return Response(natija)
        return Response({"xabar": "Ma'lumotda xatolik bor!"})

class PlanAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        plan=Plan.objects.get(id=pk)
        serializer=PlanSerializer(plan)
        return Response(serializer.data)
    def delete(self, request, pk):
        plan=Plan.objects.get(id=pk)
        if plan.user==request.user:
            plan.delete()
            return Response({"Success": "True"})
        return Response({"Success": "False"})
    def put(self, request, pk):
        plan=Plan.objects.get(id=pk)
        if plan.user==request.user:
            serializer=PlanSerializer(plan, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response({"Success": "True"})
            return Response(serializer.errors)
        return Response({"xabar": "Bu plan bu userga tegishli emas!"})