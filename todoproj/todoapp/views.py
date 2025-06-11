# from django.shortcuts import render
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.viewsets import ViewSet
# from .models import TODOAPP
# from .serializers import TODOAPPSerializer
#
#
# class TODOViews(ViewSet):
#     def list(self, request):
#         todo = TODOAPP.objects.all()
#         serializer = TODOAPPSerializer(todo, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         # get the request data from user
#         name = request.data.get('name')
#
#         if not name:
#             return Response({'error': 'error to create'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # convert data into serializer
#         serializer = TODOAPPSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request,pk=None):
#         try:
#             name = TODOAPP.objects.get(pk=pk)
#         except TODOAPP.DoesNotExist:
#             return Response({'errors' : 'Not found'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # convert into readable  by serializer
#         serializer = TODOAPPSerializer(name,data=request.data)
#         # check serializer valid or not
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'successfull' : 'Updated data successfully'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     # delete user
#
#     def destroy(self, request, pk=None):
#         try:
#             name = TODOAPP.objects.get(pk=pk)
#         except TODOAPP.DoesNotExist:
#             return Response({'errors' : 'Not Found'},status=status.HTTP_400_BAD_REQUEST)
#
#         name.delete()
#         return Response({'successfull' : 'deleted successfull'},status=status.HTTP_200_OK)
from rest_framework.response import Response
# from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response
# from rest_framework import status
# from .models import TODOAPP
# from .serializers import TODOAPPSerializer
#
#
# class TODOViews(ModelViewSet):
#     def list(self, request):
#         todo = TODOAPP.objects.all()
#         return Response(todo.values())
#
#     def create(self, request):
#         id = request.data.get('id')
#         name = request.data.get('name')
#         try:
#             users = TODOAPP.objects.create(id=id, name=name)
#             return Response(request.data, status=status.HTTP_200_OK)
#         except TODOAPP.DoesNotExist:
#             return Response({'Error': 'Error while creating'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # update
#
#     def update(self, request, pk=None):
#         id = request.data.get('id')
#         name = request.data.get('name')
#
#         try:
#             users = TODOAPP.objects.get(id=id)
#             users.name = name
#             users.save()
#             return Response(request.data, status=status.HTTP_200_OK)
#         except TODOAPP.DoesNotExist:
#             return Response({'error': 'Instance not Found'}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(request.data, status=status.HTTP_200_OK)
#
#     def destroy(self, request, pk=None):
#         id = request.data.get('id')
#         name = request.data.get('name')
#
#         try:
#             # create the object of the model
#             users = TODOAPP.objects.get(id=id)
#             users.delete()
#             return Response(request.data, status=status.HTTP_200_OK)
#         except TODOAPP.DoesNotExist:
#             return Response({'error': 'Does not exist'}, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.viewsets import ModelViewSet
# from rest_framework import status, viewsets
# from rest_framework import request, response
# from .serializers import TODOAPPSerializer
# from .models import TODOAPP
#
#
# class TODOViews(viewsets.ModelViewSet):
#     # queryset = TODOAPP.objects.all()  # ✅ REQUIRED to avoid AssertionError
#
#     def list(self, request):
#         users = TODOAPP.objects.all()
#         return Response(users.values(), status=status.HTTP_200_OK)
#
#     # creare
#
#     def create(self, request):
#         id = request.query_params.get('id')
#         name = request.query_params.get('name')
#         age = request.query_params.get('age')
#
#         # if not id or not name:
#         #     return Response({'error':'error'}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             users = TODOAPP.objects.create(id=id, name=name, age=age)
#             users.save()
#             # return Response({'successfully:', users.id, users.name , users.age}, status=status.HTTP_200_OK)
#             # add new age in here
#             return Response(
#                 {'Successfully': 'Succesfully Generated', "id": users.id, "name": users.name, "age": users.age},
#                 status=status.HTTP_200_OK)
#         except TODOAPP.DoesNotExist:
#             return Response({'error': 'error'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk=None):
#         try:
#             # Fetch the instance using the primary key
#             instance = TODOAPP.objects.get(id=pk)
#
#             # Get data from URL query parameters
#             name = request.GET.get('name')
#             age = request.GET.get('age')
#
#             # Update fields if provided
#             if name is not None:
#                 instance.name = name
#             if age is not None:
#                 instance.age = age
#
#             # Save the updated instance
#             instance.save()
#
#             return Response(
#                 {
#                     "message": "Record updated successfully",
#                     "id": instance.id,
#                     "name": instance.name,
#                     "age": instance.age
#                 },
#                 status=status.HTTP_200_OK
#             )
#
#         except TODOAPP.DoesNotExist:
#             return Response({'error': 'Instance not found'}, status=status.HTTP_404_NOT_FOUND)
#     def destroy(self, request, pk=None):
#         try:
#             users = TODOAPP.objects.get(id=pk)
#             users.delete()
#             return Response(request.data, status=status.HTTP_200_OK)
#         except TODOAPP.DoesNotExist:
#             return Response({'error': 'error showing'}, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework.request import Request
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
# from .models import TODOAPP
# from .serializers import TODOAPPSerializer
#
#
# class TODOViews(APIView):
#     # list
#     def get(self, request):
#         users = TODOAPP.objects.all()
#         serializer = TODOAPPSerializer(users, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     # create
#
#     def post(self, request):
#         id = request.data.get('id')
#         name = request.data.get('name')
#         age = request.data.get('age')
#         print(id, name , age)
#         serializer = TODOAPPSerializer(data=request.data)
#         if serializer.is_valid():
#             user_detials = serializer.save()
#             return Response({"Successful": "Successfully created {}".format(user_detials.name)},
#                             status=status.HTTP_200_OK)
#         return Response({'Error': 'Not created'}, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk=None):
#         id = request.data.get('id')
#         name = request.data.get('name')
#         age = request.data.get('age')
#         print(id, name, age, pk)
#         try:
#             users = TODOAPP.objects.get(id=pk)
#         except TODOAPP.DoesNotExist:
#             return Response({'error': 'This was not working properly'}, status=status.HTTP_400_BAD_REQUEST)
#
#         # define the serializer
#         serializer = TODOAPPSerializer(data=request.data, partial=True)
#         if serializer.is_valid():
#             print("Validated Data:", serializer.validated_data)  # Debugging step
#             serializer.save()
#             return Response({'Successful': 'Successfully updated'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk=None):
#         print(pk)
#         try:
#             users = TODOAPP.objects.get(id=pk)
#         except TODOAPP.DoesNotExist:
#             return Response({
#                 'error', 'Showing error {}'.format(request.name)
#             }, status=status.HTTP_400_BAD_REQUEST)
#         users.delete()
#         return Response({'Successfull': 'Account have been updated'}, status=status.HTTP_200_OK)

#
# from rest_framework import request, response
# from rest_framework import status
# from rest_framework.viewsets import ViewSet, ModelViewSet
# from .models import TODOAPP
# from .serializers import TODOAPPSerializer
#
#
# class TODOViews(ModelViewSet):
#     def list(self, request):
#         users = TODOAPP.objects.all()
#         return Response(users.values())
#
#     def create(self, request, pk=None):
#         id = request.data.get('id')
#         name = request.data.get('name')
#         age = request.data.get('age')
#         gender = request.data.get('date')
#         place = request.data.get('place')
#         position = request.data.get('position')
#         print(id, name, age, gender, place, position)
#         # serializer = TODOAPPSerializer(data=request.data)
#         try:
#             users = TODOAPP.objects.create(id=id, name=name, age=age, gender=gender, place=place, position=position)
#             return Response({'Successfully': "The Account was create {} {}".format(users.id, users.name)},
#                             status=status.HTTP_200_OK)
#         except TODOAPP.DoesNotExist:
#             return Response({'Error': 'Not definied properly for creation'})
#
#     def update(self, request, pk=None):
#         # id = request.data.get('id')
#         # name = request.data.get('name')
#         # age = request.data.get('age')
#         # gender = request.data.get('gender')
#         # place = request.data.get('place')
#         # position = request.data.get('position')
#         # print(id, name, age, gender, place, position)
#         try:
#             users = TODOAPP.objects.get(id=pk)
#             # users.name = name
#             # users.age = age
#             # users.gender = gender
#             # users.place = place
#             # users.position = position
#             # users.name, users.age, users.gender, users.place, users.position, users.id = name, age, gender, place, position, id
#         except TODOAPP.DoesNotExist:
#             return Response({'errors': 'Error was showing in this object'}, status=status.HTTP_400_BAD_REQUEST)
#         # serializer = TODOAPPSerializer(users, data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response({'Successfully': 'Account was updated'}, status=status.HTTP_200_OK)
#         users.save()
#         return Response({'Successfully': 'Account was updated {} {}'.format(users.id,users.name)}, status=status.HTTP_200_OK)
#
#     def destroy(self, request, pk=None):
#         try:
#             users = TODOAPP.objects.get(pk=pk)
#         except TODOAPP.DoesNotExist:
#             return Response({'Error': 'Not valid'}, status=status.HTTP_400_BAD_REQUEST)
#         users.delete()
#         return Response({'Successfully': 'Data was {} user removed'.format(pk)}, status=status.HTTP_200_OK)
#

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .models import TODOAPP
from .serializers import TODOAPPSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def todoviews(request, pk=None):
    # list all users record from  the db table
    global id
    if request.method == 'GET':
        users = TODOAPP.objects.all()
        return Response(users.values(), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        id = request.data.get('id')
        name = request.data.get('name')
        age = request.data.get('age')
        gender = request.data.get('gender')
        place = request.data.get('place')
        position = request.data.get('position')
        print(id, place)
        # condition checking
        if age <= 18:
            return Response({'Error': 'Age Should be greater than 18'}, status=status.HTTP_400_BAD_REQUEST)
        elif place.lower() not in ['madurai', 'chennai', 'coimbatore']:
            return Response({'Error': 'Other place was not allowed'}, status=status.HTTP_400_BAD_REQUEST)
        elif gender not in ['men', 'female']:
            return Response({'Error': 'Other gender was not allowed'})
        elif position.lower() not in ['developer', 'tester', 'manager', 'software developer']:
            return Response({'Error showing': 'Showing the error in the registration'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            users = TODOAPP.objects.create(id=id, name=name, age=age, gender=gender, place=place, position=position)
            users.save()
            return Response({'Successfull': 'created properly'}, status=status.HTTP_200_OK)
        except TODOAPP.DoesNotExist:
            return Response({'Error': 'Showing error'}, status=status.HTTP_400_BAD_REQUEST)


    # put method

    elif request.method == 'PUT':
        id = request.data.get('id')
        name = request.data.get('name')
        age = request.data.get('age')
        gender = request.data.get('gender')
        place = request.data.get('place')
        position = request.data.get('position')
        print(id)
        try:
            users = TODOAPP.objects.get(id=id)
            users.name = name
            users.age = age
            users.gender = gender
            users.place = place
            users.position = position
            # save the updated data
            users.save()
            return Response({'Successfully': 'updated properly'}, status=status.HTTP_200_OK)
        except TODOAPP.DoesNotExist:
            return Response({'Error': 'not properly defined'}, status=status.HTTP_400_BAD_REQUEST)

    # delete method

    elif request.method == 'DELETE':
        id = request.data.get('id')
        users = TODOAPP.objects.get(id=pk)
        try:
            users.delete()
            return Response({'Successfully': 'Showing Successful Message'}, status=status.HTTP_200_OK)
        except TODOAPP.DoesNotExist:
            return Response({'Error': 'Showing error message {} '.format(users.name)},
                            status=status.HTTP_400_BAD_REQUEST)
