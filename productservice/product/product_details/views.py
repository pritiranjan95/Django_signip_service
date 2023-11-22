from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from product_details.seriealizer import product_serializers, purchase_serializers
from .models import products, purchase


class Productcreate(APIView):
    def post(self, request):
        try:
            serializer=product_serializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(e)

class Getdata(APIView):
    def get(self, request):
        try:
            data=products.objects.all()
            serializer=product_serializers(data, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)  
        except:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
class Updatedata(APIView):
    def put(self, request, pk):
        try:
            s=products.objects.get(id=pk)
        except products.DoesNotExist:
            return Response({"details": "The given id is not there"}, status=status.HTTP_404_NOT_FOUND)
        serializer=product_serializers(s, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"details":"successfully updated"}, status=status.HTTP_201_CREATED)
class Removedata(APIView):
    def delete(self, request,pk):
        try:
            s=products.objects.get(id=pk)
        except products.DoesNotExist:
            return Response({"details":"your serched data not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=product_serializers(s)
        s.delete()
        return Response({"details":"The data has successfully deleted","data":serializer.data}, status=status.HTTP_204_NO_CONTENT)
    
#Purchase classes

class Purchasecreate(APIView):
    def post(self, request):
        try:
            print("started working")
            serializer = purchase_serializers(data=request.data)
            
            if serializer.is_valid():
                print("thhhhhhhhhhhhh")
                product_no = request.data.get("product_name")
                print(f"tttttttt{product_no}")

                try:
                    # Attempt to get the product with the specified ID
                    product_exist = products.objects.get(id=product_no)
                    print(f"The product status is {product_exist}")

                    # If the product exists, proceed with saving the serializer
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                except products.DoesNotExist:
                    # Handle the case where the product does not exist
                    print("Product does not exist in the related table")
                    return Response({"details": "Product does not exist in the related table"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                print("Serializer is not valid:", serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"The error is {e}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
class Get_purchase_data(APIView):
    def get(self, request):
        try:
            s=purchase.objects.all()
            serializer=purchase_serializers(s, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error":e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)