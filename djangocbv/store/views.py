from django.shortcuts import render,redirect
from django.views.generic import *
from store.models import Category,Customer,Order,OrderItem,Product
from django.urls import reverse_lazy,reverse
from store.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Sum

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    success_url = reverse_lazy('store:home')

    def get_success_url(self):
        return self.success_url
    
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['name'] = "Ebrahim"
        return context
    

def toggleTheme(request):
    theme = Setting.objects.get(key='theme')
    if theme.value == "dark":
        theme.value = "light"
    else:
        theme.value = "dark"
    theme.save()
    referer = request.META.get('HTTP_REFERER', '/')
    return redirect(referer)

class ProductListView(PermissionRequiredMixin,ListView):
    permission_required = 'store.view_product'
    model = Product
    template_name = 'store/product/product_list.html'

class ProductCreateView(PermissionRequiredMixin,CreateView):
    permission_required = 'store.add_product'
    form_class = ProductForm 
    template_name = 'store/product/product_form.html'
    success_url = reverse_lazy('store:products')

class ProductDetailView(PermissionRequiredMixin,DetailView):
    permission_required = 'store.view_product'
    model = Product
    template_name = 'store/product/product_detail.html'

class ProductUpdateView(PermissionRequiredMixin,UpdateView):
    permission_required = 'store.change_product'
    model = Product
    form_class = ProductForm 
    template_name = 'store/product/product_form.html'
    success_url = reverse_lazy('store:products')

class ProductDeleteView(PermissionRequiredMixin,DeleteView):
    permission_required = 'store.delete_product'
    model = Product
    template_name = 'store/product/product_confirm_delete.html'
    success_url = reverse_lazy('store:products')


class CategoryListView(LoginRequiredMixin,ListView):
    model = Category
    template_name = "store/category/category_list.html"

class CategoryCreateView(CreateView):
    # model = Category
    # fields = ['name',]
    form_class = CategoryForm
    template_name = "store/category/category_form.html"
    success_url = reverse_lazy('store:categories')

class CategoryDetailView(DetailView):
    model = Category
    template_name = "store/category/category_detail.html"

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm 
    template_name = 'store/category/category_form.html'
    success_url = reverse_lazy('store:categories')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'store/category/category_confirm_delete.html'
    success_url = reverse_lazy('store:categories')

class OrderCreateView(View):
    def get(self, request, id, *args, **kwargs):
        product = Product.objects.get(id=id)
        customer = Customer.objects.get(user=request.user)
        order = Order.objects.filter(customer=customer).last()
        if order.is_confirmed:
            order = Order.objects.create(customer=customer, total_price=product.price, is_confirmed=False)
        else:
            order.total_price += product.price
            order.save()

        order_item = order.orderitem_set.filter(product=product).first()
        if order_item:
            order_item.quantity += 1
            order_item.save()
        else:
            OrderItem.objects.create(order=order, product=product, quantity=1)
        return redirect(reverse_lazy('store:products'))


class CartView(LoginRequiredMixin,ListView):
    model = OrderItem
    template_name = "store/cart/order_list.html"
    context_object_name = "orders"
    
    def get_queryset(self):
        customer = Customer.objects.get(user=self.request.user)
        order = Order.objects.filter(customer=customer, is_confirmed=False).last()
        orderitem  = order.orderitem_set.all()
        return orderitem
    
    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        customer = Customer.objects.get(user=self.request.user)
        order = Order.objects.filter(customer=customer, is_confirmed=False).last()

        orders = order.orderitem_set.all()
        total_orders = orders.aggregate(Sum('quantity'))

        context['order'] = order
        context['total_orders'] = total_orders['quantity__sum']
        return context


class OrderConfirmView(View):
    def get(self,request):
        customer = Customer.objects.get(user=request.user)
        order = Order.objects.filter(customer=customer,is_confirmed=False).last()
        order.is_confirmed = True
        order.save()
        return redirect(reverse_lazy("store:products"))
# from django.shortcuts import render_to_response
# from django.template import RequestContext

# def e_handler404(request):
#     context = RequestContext(request)
#     response = render_to_response('error404.html', context)
#     response.status_code = 404
#     return response

# def e_handler500(request):
#     context = RequestContext(request)
#     response = render_to_response('error500.html', context)
#     response.status_code = 500
#     return response
