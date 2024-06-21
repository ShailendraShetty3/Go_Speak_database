from rest_framework import status, generics, parsers
from rest_framework.response import Response
from .models import Groups, Cfps, Events, Proposals
from .serializers import GroupsSerializer, CfpsSerializer, EventsSerializer, ProposalsSerializer
from django.shortcuts import get_object_or_404

class GroupsListCreateView(generics.ListCreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    parser_classes = [parsers.MultiPartParser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupsDetail(generics.GenericAPIView):
    serializer_class = GroupsSerializer
    parser_classes = [parsers.MultiPartParser]
    def get_object(self, id):
        try:
            return Groups.objects.get(pk=id)
        except Groups.DoesNotExist:
            return None
    
    def get(self, request, id, format=None):
        groups = self.get_object(id)
        if groups:
            serializer = GroupsSerializer(groups)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, format=None):
        groups = get_object_or_404(Groups, pk=id)
        serializer = GroupsSerializer(groups, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id, format=None):
        groups = self.get_object(id)
        if groups:
            groups.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # def patch(self, request, id, format=None):
    #     groups = self.get_object(id)
    #     if groups:
    #         serializer = GroupsSerializer(groups, data=request.data, partial=True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    
    # from django.shortcuts import get_object_or_404

    def patch(self, request, id, format=None):
        groups = get_object_or_404(Groups, pk=id)
        serializer = GroupsSerializer(groups, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




#CFPS

class CfpsListCreateView(generics.ListCreateAPIView):
    queryset = Cfps.objects.all()
    serializer_class = CfpsSerializer
    parser_classes = [parsers.MultiPartParser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Events

class EventsListCreateView(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    parser_classes = [parsers.MultiPartParser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



#Proposals

class ProposalsListCreateView(generics.ListCreateAPIView):
    queryset = Proposals.objects.all()
    serializer_class = ProposalsSerializer
    parser_classes = [parsers.MultiPartParser]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)