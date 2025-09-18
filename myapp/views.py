import io
from myapp.serializers import Student
from myapp.models import Studentt
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

# two ways to share your zip file of your computer to others and they can run it
# requirement.txt file
# pyvenv.cfg file's path
# pip upgrade to update the path of django file within our computer.....


# Create your views here.
# @csrf_exempt
# def stu_list(req):  
#     if req.method=='POST':
#         data=req.body
#         stream=io.BytesIO(data)
#         p_data=JSONParser().parse(stream)
#         serializer=Student(data=p_data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse({'msg':'data created'})
#         return JsonResponse({"error":serializer.errors})
#     elif req.method=='GET':
#         all_stu=Studentt.objects.all()
#         serializer=Student(all_stu,many=True) # if api handles multiple data then many= true
#         return JsonResponse(serializer.data,safe=False)
    

# @csrf_exempt
# def stu_detail(req,pk):
#     data=Studentt.objects.filter(id=pk)
#     if data:
#         if req.method=='GET':
#             data=Studentt.objects.get(id=pk)
#             serializer=Student(data)
#             return JsonResponse(serializer.data)
        
#         elif req.method=='PUT':
#             old_data=Studentt.objects.get(id=pk)
#             data=req.body
#             stream=io.BytesIO(data)
#             new_p_data=JSONParser().parse(stream)
#             serializer=Student(old_data,data=new_p_data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse({'msg':'Data updated'})
#             return JsonResponse({'error':serializer.errors})
        
#         elif req.method=='PATCH':
#             old_data=Studentt.objects.get(id=pk)
#             data=req.body
#             stream=io.BytesIO(data)
#             new_p_data=JSONParser().parse(stream)
#             serializer=Student(old_data,data=new_p_data,parsial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 return JsonResponse({'msg':'Data updated'})
#             return JsonResponse({'error':serializer.errors})
        
#         elif req.method=='DELETE':
#             data=Studentt.objects.get(id=pk)
#             data.delete()
#             return JsonResponse({'msg':'Data Deleted'})
        
@api_view(["GET","POST"])
def stu_list(req):
    if req.method == "GET":
        snippets = Student.objects.all()
        serializer = Student(snippets, many=True)
        return Response(serializer.data)
    elif req.method == "POST":
        serializer = Student(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","PATCH","DELETE"])
def stu_detail(req,pk):
    if req.method=="GET":
        snippet = Student.objects.get(id=pk)
        serializer = Student(snippet)
        return Response(serializer.data)

    elif req.method=="PUT":
        snippet = Student.objects.get(id=pk)
        serializer = Student(snippet, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method=="PATCH":
        snippet = Student.objects.get(id=pk)
        serializer = Student(snippet, data=req.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif req.method=="DELETE":
        snippet = Student.objects.get(id=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        



class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Studentt.objects.all()
    serializer_class = Student



# class based DRF API

# from myapp.models import Studentt
# from myapp.serializers import Student
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Studentt.objects.all()
#         serializer = Student(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = Student(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Studentt.objects.get(pk=pk)
#         except Studentt.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = Student(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = Student(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Mixins

# from myapp.models import Studentt
# from myapp.serializers import Student
# from rest_framework import mixins
# from rest_framework import generics

# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Studentt.objects.all()
#     serializer_class = Student

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Studentt.objects.all()
#     serializer_class = Student

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

from myapp.models import Studentt
from myapp.serializers import Student
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Studentt.objects.all()
    serializer_class = Student


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Studentt.objects.all()
    serializer_class = Student