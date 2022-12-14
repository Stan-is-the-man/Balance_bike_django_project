from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from balance_bike.web.forms import UserCreateForm, UserLoginForm, UserEditForm, AddressForm
from balance_bike.web.models import BalanceBike, Customer, Cart, Address, Order

UserModel = get_user_model()


class UserSignUpView(CreateView):
    template_name = 'user-signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('catalogue')

    # login the user automatically after registration :)
    def form_valid(self, form):
        # If the form is valid, save the associated model and log in the user
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class UserLoginView(LoginView):
    template_name = 'user-login.html'
    form_class = UserLoginForm
    next_page = reverse_lazy('catalogue')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class UserEditView(UpdateView):
    model = UserModel
    template_name = 'user-edit.html'
    form_class = UserEditForm
    success_url = reverse_lazy('profile')

    # def get_success_url(self):
    #     return reverse_lazy('profile')


class UserDeleteView(DeleteView):
    template_name = 'user-delete.html'
    model = Customer
    success_url = reverse_lazy('index')


class BikesListView(ListView):
    model = BalanceBike
    template_name = 'catalogue.html'
    context_object_name = 'bikes'

    ordering = ['color']


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class AddressView(View):
    def get(self, request):
        form = AddressForm()
        context = {
            'form': form,
        }
        return render(request, 'add_address.html', context)

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            user = request.user
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            name_for_engraving = form.cleaned_data['name_for_engraving']
            phone = form.cleaned_data['phone']

            delivery_info = Address(
                user=user,
                city=city,
                street=street,
                first_name=first_name,
                last_name=last_name,
                name_for_engraving=name_for_engraving,
                phone=phone,
            )
            delivery_info.save()

        return redirect('order summary')


@login_required
def profile(request):
    addresses = Address.objects.filter(user=request.user)
    orders = Order.objects.filter(user=request.user)
    context = {
        'addresses': addresses,
        'orders': orders,
    }

    return render(request, 'profile.html', context)


@login_required
def remove_address(request, id):
    the_address = get_object_or_404(Address, user=request.user, id=id)
    the_address.delete()
    return redirect('profile')


@login_required
def add_to_cart(request, product_pk):
    user = get_object_or_404(UserModel, pk=request.user.pk)
    product = get_object_or_404(BalanceBike, pk=product_pk)

    item_already_in_cart = Cart.objects.filter(product=product_pk, user=user)
    # if the bike with same color is already in cart:
    if item_already_in_cart:
        current_product_in_cart = get_object_or_404(Cart, user=user, product=product_pk)
        current_product_in_cart.quantity += 1
        current_product_in_cart.save()
    else:
        Cart(user=user, product=product).save()
    return redirect('cart')


@login_required
def cart(request):
    user = request.user
    cart_products = Cart.objects.filter(user=user).order_by('created_at')
    amount = 0
    shipping_amount = 0
    # using list comprehension to calculate total amount based on quantity and shipping
    cp = [p for p in Cart.objects.all() if p.user == user]
    if cp:
        for p in cp:
            temp_amount = (p.quantity * p.product.price)
            amount += temp_amount

    address = Address.objects.filter(user=user)
    context = {
        'cart_products': cart_products,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': amount + shipping_amount,
        'addresses': address,
    }
    return render(request, 'cart.html', context)


@login_required
def checkout(request):
    user = request.user
    address = Address.objects.all()[0]

    # get all the products of user in the cart
    products_in_the_cart = Cart.objects.filter(user=user).all()

    for item in products_in_the_cart:
        # moving all the products from Cart to Order and save them in order
        Order(user=user, address=address, product=item.product, quantity=item.quantity).save()

        # the available quantity (IN STOCK) decreasing !
        item.product.quantity_available -= item.quantity
        item.product.save()

        # and then deleting from the cart
        item.delete()

    return redirect('orders')


@login_required
def remove_cart(request, cart_id):
    if request.method == 'GET':
        my_cart = get_object_or_404(Cart, id=cart_id)
        my_cart.delete()
    return redirect('cart')


@login_required
def plus_cart(request, cart_id):
    if request.method == 'GET':
        product_in_cart = get_object_or_404(Cart, id=cart_id)

        # making sure selected QTY doesn't exceed available quantity at the storage
        if product_in_cart.quantity < product_in_cart.product.quantity_available:
            product_in_cart.quantity += 1
            product_in_cart.save()
    return redirect('cart')


@login_required
def minus_cart(request, cart_id):
    if request.method == 'GET':
        product_in_cart = get_object_or_404(Cart, id=cart_id)

        # remove the bike if the quantity now is 1
        if product_in_cart.quantity == 1:
            product_in_cart.delete()
        else:
            product_in_cart.quantity -= 1
            product_in_cart.save()
    return redirect('cart')


@login_required
def orders(request):
    all_orders = Order.objects.filter(user=request.user).order_by('-ordered_date')
    context = {
        'orders': all_orders
    }
    return render(request, 'orders.html', context)


@login_required
def order_summary(request):
    product_amount = 0
    shipping_amount = 0

    user = request.user
    cart_products = Cart.objects.filter(user=user)

    if cart_products:
        for product in cart_products:
            current_amount = (product.quantity * product.product.price)
            product_amount += current_amount

    addresses = Address.objects.filter(user=user)
    total_to_be_payed = product_amount + shipping_amount

    context = {
        'cart_products': cart_products,
        'amount': product_amount,
        'shipping_amount': shipping_amount,
        'total_amount': total_to_be_payed,
        'addresses': addresses,
    }

    return render(request, 'order_summary.html', context)


def contacts(request):
    return render(request, 'contacts.html')
