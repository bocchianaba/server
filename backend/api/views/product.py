from rest_framework import viewsets
from ..serializers.ProductSerializer import ProductSerializer
from ..models import Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

class ProductDetailView(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        product = Product.objects.filter(available=True)
        serializer = ProductSerializer(product, context={"request": request}, many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)

class MyProductDetailView(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        product = Product.objects.filter(created_by=request.user.id)
        serializer = ProductSerializer(product, context={"request": request}, many=True)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            #we must return the url of the image of the product
            serializer2 = ProductSerializer(self.get_object(pk), context={"request": request})
            return Response(serializer2.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            status_code = status.HTTP_201_CREATED
            return Response(serializer.data, status=status_code)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ProductPostLikePushView(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        like=request.data.pop('image')
        print(request.data)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductPostLikePopView(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        like=request.data.pop('image')
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductPostDisLikePushView(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        like=request.data.pop('image')
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductPostDislikePopView(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        like=request.data.pop('image')
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductPostLovePushView(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        like=request.data.pop('image')
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductPostLovePopView(APIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        like=request.data.pop('image')
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
