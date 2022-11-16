from django.urls import path

from balance_bike.web.views import IndexView, UserSignUpView, UserLoginView, UserLogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sign-up/', UserSignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('user-edit/', UserEditView.as_view(), name='user edit'),

]
