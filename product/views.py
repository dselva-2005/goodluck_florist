from typing import Any
from django.views.generic import ListView,DetailView
from .models import Product, Review, Comment
from django.views.decorators.http import require_POST
from .forms import ReviewForm, SearchForm
from django.shortcuts import render,get_object_or_404
# Create your views here.

class ProductsList(ListView):
    comments = 7
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()[:self.comments]
        return context

class ProductsDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ReviewForm()
        reviews = Review.objects.filter(product__id = self.object.pk)
        print(self.object.pk)
        context['form'] = form
        context['reviews'] = reviews

        return context

@require_POST
def add_review(request,product_id):
    form = ReviewForm(request.POST)
    product = get_object_or_404(Product,id=product_id)
    if form.is_valid():
        form = (form.cleaned_data)
        review = ReviewForm(form).save(commit=False)
        review.product = product
        review.save()
        return render(request,'product/review.html')
    else:
        return render(request, 'product/detail.html',{
            'product':product,
            'form': form})
    
def prduct_search(request):
    query = request.GET.get('query')
    form = SearchForm()
    results = []
    if query:
        results = Product.objects.filter(name__icontains=query) | Product.objects.filter \
        (description__icontains=query)
        form = SearchForm(request.GET)
        
    return render(request,'product/search.html',{
        'form':form,
        'results': results,
    })