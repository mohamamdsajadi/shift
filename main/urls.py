from django.urls import path

from .views import *


urlpatterns = [
    path('login/', LogInView.as_view(), name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('thankyou/', SignedView.as_view(), name="signed"),
    path('files/', FilesView.as_view(), name="files"),
    path('bankinfo/', BankInfoView.as_view(), name="bankinfo"),
    path('password/', change_password, name="change_password"),
    path('sendcode/', send_code, name="sendcode"),
    path('next_month_shift/', next_month_shift_view, name="nms"),
    path('current_month_shift/', current_month_shift_view, name="cms"),
    path('shift/', shift_portal, name="shift"),
    path('discount/', discount, name="discount"),
    path('reqedit/', request_edit, name="request_edit"),
    path('', ProfileView.as_view(), name="profile"),
]
