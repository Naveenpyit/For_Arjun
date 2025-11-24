from rest_framework.views import APIView
from rest_framework.response import Response
from . import models,serializer

class TaskView(APIView):
    model = models.TaskModel
    serializer = serializer.TaskSerializer

    def get(self,request,pk=None):
        try:
            if pk is None:
                data = self.model.objects.all().order_by('id')
                serial_data = self.serializer(data,many = True).data
            else:
                data = self.model.objects.filter(pk = pk).first()
                serial_data = self.serializer(data).data
            return Response({'status':1,'message':'success','data':serial_data})
        except Exception as e:
            return Response({'status':0,'message':str(e)})
    
    def post(self,request):
        try:
            payload = request.data
            serial = self.serializer(data = payload)
            if serial.is_valid():
                serial.save()
                return Response({'status':1,'message':'Data submitted successfully!'})
            return Response({'status':0,'message':'Data save failed!'})
        except Exception as e:
            return Response({'status':0,'message':str(e)})
        
    def put(self,request,pk):
        try:
            pass
        except Exception as e:
            return Response({'status':0,'message':str(e)})


