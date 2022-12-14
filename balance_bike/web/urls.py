from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path

from balance_bike.web.forms import PasswordChanging
from balance_bike.web.views import IndexView, UserSignUpView, UserLoginView, UserLogoutView, BikesListView, \
    UserEditView, UserDeleteView, cart, checkout, add_to_cart, plus_cart, minus_cart, orders, remove_cart, \
    profile, remove_address, order_summary, contacts, AddressView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    # User account
    path('sign-up/', UserSignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('user/<int:pk>/edit', UserEditView.as_view(), name='user edit'),
    path('user/<int:pk>/delete/', UserDeleteView.as_view(), name='user delete'),
    path('accounts/password-change/', PasswordChangeView.as_view(
        template_name='password_change.html',
        form_class=PasswordChanging,
        success_url='/accounts/password-change-done/'), name="password-change"),
    path('accounts/password-change-done/', PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'),
         name="password-change-done"),

    # Address
    path('add-address/', AddressView.as_view(), name='add address'),
    path('remove-address/<int:id>/', remove_address, name='remove address'),

    # Cart
    path('cart/', cart, name='cart'),
    path('add-to-cart/<int:product_pk>/', add_to_cart, name='add to cart'),
    path('remove-cart/<int:cart_id>/', remove_cart, name='remove-cart'),
    path('plus-cart/<int:cart_id>/', plus_cart, name="plus cart"),
    path('minus-cart/<int:cart_id>/', minus_cart, name='minus cart'),

    path('bikes-catalogue/', BikesListView.as_view(), name='catalogue'),
    path('contacts/', contacts, name='contatcts'),

    path('order-summary/', order_summary, name='order summary'),
    path('checkout/', checkout, name='checkout'),
    path('orders/', orders, name='orders'),

]
