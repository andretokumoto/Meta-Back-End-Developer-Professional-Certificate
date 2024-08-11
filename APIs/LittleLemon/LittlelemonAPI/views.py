from django.shortcuts import get_object_or_404
import datetime
from rest_framework.response import Response
from rest_framework import status,viewsets
from rest_framework.decorators import api_view, throttle_classes ,permission_classes
from .models import Menuitem, Category , ItemOfDay , Cart, Order
from .serializers import MenuItemSerializar,CategorySerializer,UserSerializer, CartSerializer, OrderSerializer, OrderItem
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
        item = ItemOfDay.objects.first()
        serialized_item = MenuItemSerializar(item.item)
        return Response(serialized_item.data,status.HTTP_200_OK)
    
    if request.method == 'POST':
        if request.user.groups.filter(name='managers').exists():
            item_id = request.data.get('item_id')
            item = get_object_or_404(Menuitem, pk=item_id)
            item_of_day = ItemOfDay.objects.get_or_create(id=1, defaults={'item': item})
            item_of_day.item = item
            item_of_day.save()
            serialized_item = MenuItemSerializar(item_of_day.item)
            return Response({'Item created',status.HTTP_201_CREATED}) 

    return Response({'message':'Error'},status.HTTP_400_BAD_REQUEST)

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

@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def cart_control(request):

    if request.method == 'GET':
        cart_items = Cart.objects.filter(user=request.user)
        serialized_cart_items = CartSerializer(cart_items, many=True)
        return Response(serialized_cart_items.data, status=status.HTTP_200_OK)       

    if request.method == 'POST':

        menuitem_id = request.data.get('menuitem_id')
        quant = request.data.get('quant')
        menuitem = get_object_or_404(Menuitem, id=menuitem_id)
        unit_price = menuitem.price
        total_price = unit_price * quant

        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            menuitem=menuitem,
            defaults={'quant': quant, 'unit_price': unit_price, 'price': total_price}
        )
        
        if not created:
            cart_item.quant += quant
            cart_item.price += total_price
            cart_item.save()

        return Response({'message':'Cart created'},status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        Cart.objects.filter(user=request.user).delete()
        return Response({'message':'Cart Deleted'},status.HTTP_200_OK)
    
@api_view(['GET','POST','DELETE'])
@permission_classes([IsAuthenticated])
def order_control(request,id):
    
    if request.method == 'GET':

        if request.user.groups.filter(name='Manager').exists():

            orders = Order.objects.all()
            serialized_orders = OrderSerializer(orders, many=True)
            return Response(serialized_orders.data, status=status.HTTP_200_OK)

        elif request.user.groups.filter(name='Delivery').exists():
            ...
        else:  #client
            if id:
                orders = Order.objects.get(id=id, user=request.user)
            else:
                orders = Order.objects.filter(user=request.user)

            serialized_orders = OrderSerializer(orders, many=True)
            return Response(serialized_orders.data,status.HTTP_200_OK)
        

    if request.method == 'POST':

        if request.user.groups.filter(name='Manager').exists():
            ...
        elif request.user.groups.filter(name='Delivery').exists():
            ...
        else:  #client
            user = request.user
            cart_items = Cart.objects.filter(user=user)
            total = sum(item.price for item in cart_items)
            order = Order.objects.create(user=user, total=total, status=False, date= datetime.date.today())

            order_items = []
            for cart_item in cart_items:
                order_item = OrderItem(
                    order=order,
                    menuitem=cart_item.menuitem,
                    quant=cart_item.quant,
                    unit_price=cart_item.unit_price,
                    price=cart_item.price
                )
                order_items.append(order_item)

                OrderItem.objects.bulk_create(order_items)

                cart_items.delete()

                serialized_order = OrderSerializer(order)
                return Response(serialized_order.data, status=status.HTTP_201_CREATED)
