from django.shortcuts import render, redirect, get_object_or_404
from .models import MenuItem, Chef, Category
from .forms import MenuItemForm, ChefForm


def home(request):
    """Display home page with featured items."""
    featured_items = MenuItem.objects.filter(is_available=True)[:3]
    context = {
        'featured_items': featured_items,
    }
    return render(request, 'menu/home.html', context)


def menu_list(request):
    """Display a list of all menu items."""
    menu_items = MenuItem.objects.all()
    context = {
        'menu_items': menu_items,
    }
    return render(request, 'menu/menu_list.html', context)


def menu_detail(request):
    """Display details of a single menu item."""
    if request.method == 'POST':
        menu_item_id = request.POST.get('menu_item_id')
        if menu_item_id:
            menu_item = get_object_or_404(MenuItem, id=menu_item_id)
            context = {
                'menu_item': menu_item,
            }
            return render(request, 'menu/menu_detail.html', context)
    
    return redirect('menu-list')


def add_menu_item(request):
    """Display form to add a new menu item."""
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu-list')
    else:
        form = MenuItemForm()
    
    context = {
        'form': form,
        'form_title': 'Add New Menu Item',
    }
    return render(request, 'menu/menu_item_form.html', context)


def chef_list(request):
    """Display a list of all chefs."""
    chefs = Chef.objects.all()
    context = {
        'chefs': chefs,
    }
    return render(request, 'menu/chef_list.html', context)


def add_chef(request):
    """Display form to add a new chef."""
    if request.method == 'POST':
        form = ChefForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chef-list')
    else:
        form = ChefForm()
    
    context = {
        'form': form,
        'form_title': 'Add New Chef',
    }
    return render(request, 'menu/chef_form.html', context)


def category_list(request):
    """Display a list of all menu categories."""
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'menu/category_list.html', context)
