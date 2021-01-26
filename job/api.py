from .models import Job
from .serializers import JobSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def job_list_api(request):
    all_jobs = Job.objects.all()
    data = JobSerializers(all_jobs, many=True).data 
    return Response({'data':data})


@api_view(['GET'])
def job_detail_api(request, id):
    job_detail = Job.objects.get(id=id)
    data = JobSerializers(job_detail).data 
    return Response({'data':data})



class JobListApi(generics.ListCreateAPIView):
    queryset = Job.objects.all()    
    serializer_class = JobSerializers


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializers   
    queryset = Job.objects.all()
    lookup_field = 'id'   
