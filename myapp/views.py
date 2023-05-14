from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .forms import UploadForm
from .models import MiesOpskrifter
from django.urls import reverse
from django.db.models import Q


def home(request):
    return render(request, 'home.html')

# views.py
tested = set(MiesOpskrifter.objects.values_list('tested', flat=True))

def opskrifter(request):
    # Retrieve non-deleted Recipe objects from the database
    recipes = MiesOpskrifter.objects.filter(deleted=False)

    # Get the available categories and kitchens from the non-deleted Recipe queryset
    categories = set(recipes.values_list('category', flat=True))
    kitchens = set(recipes.values_list('kitchen', flat=True))

    # Get the selected filter values from the request
    category_filter = request.GET.get('category')
    kitchen_filter = request.GET.get('kitchen')
    tested_filter = request.GET.get('tested')
    search_filter = request.GET.get('search')

    # Apply the selected filters to the non-deleted Recipe queryset
    if category_filter:
        recipes = recipes.filter(category=category_filter)
    if kitchen_filter:
        recipes = recipes.filter(kitchen=kitchen_filter)
    if tested_filter:
        recipes = recipes.filter(tested=tested_filter)
    if search_filter:
        # Perform a case-insensitive search on the title field using the search term
        recipes = recipes.filter(title__icontains=search_filter)

    # Render the template with the filtered non-deleted Recipe queryset and filter options
    context = {
        'recipes': recipes,
        'categories': categories,
        'kitchens': kitchens,
        'tested': tested,
    }
    return render(request, 'opskrifter.html', context)

def slettede_opskrifter(request):
    # Retrieve deleted recipes from the database
    recipes = MiesOpskrifter.objects.filter(deleted=True)

    # Pass the recipes to the template
    context = {
        'recipes': recipes
    }
    return render(request, 'slettede_opskrifter.html', context)


def ny_opskrift(request):
    if request.POST:
        form = UploadForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']

            # Check if a recipe with the same link already exists
            if MiesOpskrifter.objects.filter(link=link).exists():
                message = "Opskrift eksisterer allerede"  # Message to display
                return render(request, 'ny.html', {'form': form, 'message': message, 'existing_recipe': True})

            # If the recipe doesn't exist, save it to the database
            form.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(request, 'ny.html', {'form': form})



def update_recipe_tested(request):
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')
        is_checked = request.POST.get('is_checked')

        recipe = get_object_or_404(MiesOpskrifter, id=recipe_id)
        recipe.tested = is_checked == 'true'  # Convert the string to a boolean value
        recipe.save()

        return JsonResponse({'message': 'Recipe updated successfully'})

    # Return an error response for other HTTP methods
    return JsonResponse({'error': 'Invalid request method'})




#deleted button
def mark_recipe_deleted(request):
    if request.method == 'POST':
        recipe_id = request.POST.get('recipe_id')

        recipe = get_object_or_404(MiesOpskrifter, id=recipe_id)
        recipe.deleted = True
        recipe.save()

        return JsonResponse({'message': 'Recipe marked as deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
