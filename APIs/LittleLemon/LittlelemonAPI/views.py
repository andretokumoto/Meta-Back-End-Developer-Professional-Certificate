from django.shortcuts import get_object_or_404
#from django.http import JsonResponse
#from django.views import View
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.decorators import api_view, throttle_classes ,permission_classes
from .models import Menuitem, Category , ItemOfDay
from .serializers import MenuItemSerializar,CategorySerializer,UserSerializer
from django.core.paginator import Paginator, EmptyPage
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import TenCallPerMinute
from django.contrib.auth.models import User,Group

@api_view(['GET','POST'])
def menu_itens(request):
    if request.method == 'GET':
        itens = Menuitem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering') 
        perpage = request.query_params.get('perpage',default=2)
        page = request.query_params.get('page',default=1)
        
        if category_name:
            itens = itens.filter(category__title=category_name)
        if to_price:
             itens = itens.filter(price__lte=to_price)
        if search:
             itens = itens.filter(title__startswich=search)
        if ordering:
            ordering_fields = ordering.split(',')
            itens = itens.order_by(*ordering_fields)
        
        paginator = Paginator(itens,per_page=perpage)
        try:
            itens = paginator.page(number=page)
        except EmptyPage:
            itens = []
        
        
        serialized_item = MenuItemSerializar(itens, many = True)
        return Response(serialized_item.data) 
    
    if request.method == 'POST':
        
        if request.user.groups.filter(name='Administrador').exists():
            serialized_item = MenuItemSerializar(data=request.data)
            serialized_item.is_valid(raise_exception=True)
            serialized_item.save()
            return Response(serialized_item.data, status.HTTP_201_CREATED)
        
        return Response({'message':'Only Admin'},status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','POST'])
def single_item(request, id):
    item = get_object_or_404(Menuitem, pk=id)
    serialized_item = MenuItemSerializar(item)
    return Response(serialized_item.data)

@api_view(['GET','POST'])
def item_of_day(request,id):
    if request.method == 'GET':
        item = get_object_or_404(ItemOfDay)
        serialized_item = MenuItemSerializar(item)
        return Response(serialized_item.data,status.HTTP_200_OK)


     
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({'message':'sucesso'})

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallPerMinute])
def throttle_check_auth(request):
    return Response({'message':'só para usuarios'})

@api_view()
@permission_classes([IsAuthenticated])
def me(request):
    return Response({request.user.email})

@api_view(['GET','POST','DELETE'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name='Manager')
        if request.method == 'POST':
            managers.user_set.add(user)
        elif request.method == 'DELETE':
            managers.user_set.remove(user)
        return Response({'message':'ok'})
    
    return Response({'message':'Erro'}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
@permission_classes([IsAdminUser])
def delivery_crew(request):
    if request.method == 'GET':
        crew = Group.objects.get(name='Delivery')
        return Response(crew.data)
    else:
        username = request.data['username']
        if username:
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name='Delivery')
            if request.method == 'POST':
                managers.user_set.add(user)
            elif request.method == 'DELETE':
                managers.user_set.remove(user)
            return Response({'message':'ok'})
        
        
    return Response({'message':'Erro'}, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
@permission_classes([IsAdminUser])
def category_ctl(request,id):
    
    if request.method == 'GET':
        categories = Category.objects.all()
        serialized_category = CategorySerializer(categories, many = True)
        return Response(serialized_category.data) 
    
    if request.method == 'POST':
        serialized_Category = CategorySerializer(data=request.data)
        serialized_Category.is_valid(raise_exception=True)
        serialized_Category.save()
        return Response(serialized_Category.data, status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        
        if id:
                
            category = get_object_or_404(Category, id=id)
            category.delete()
            return Response({'message':'Category deleted'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message': 'Category ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
    
@api_view(['POST'])
def user_register(request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response({'User created'},status.HTTP_201_CREATED)
    return Response({'message':"Error"},status.HTTP_400_BAD_REQUEST)
