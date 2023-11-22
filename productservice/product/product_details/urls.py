from django.urls import path
from product_details import views

urlpatterns=[
    path("create",view=views.Productcreate.as_view()),
    path("get", view=views.Getdata.as_view()),
    path("update/<int:pk>", view=views.Updatedata.as_view()),
    path("delete/<int:pk>", view=views.Removedata.as_view()),
    path("create/purchase",view=views.Purchasecreate.as_view()),
    path("get_all_puchasedata", view=views.Get_purchase_data.as_view())
]