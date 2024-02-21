from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Item
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.
def index(request):
    return render(request, "items/index.html")

@swagger_auto_schema(method="get",
                     operation_description="Search for items by name",
                     manual_parameters=[
                         openapi.Parameter(
                             "q",
                             openapi.IN_QUERY,
                             description="Search query",
                             type=openapi.TYPE_STRING,
                         )
                     ])
@api_view(["GET"])
@csrf_exempt
def search(request):
    query = request.GET.get("q")

    if request.headers.get("Accept") == "application/json":
        if query:
            items = Item.objects.filter(name__icontains=query)
        else:
            items = []
        return Response([{"id": item.id, "name": item.name} for item in items])

    if query:
        items = Item.objects.filter(name__icontains=query).order_by("name")
        paginator = Paginator(items, 15)
        page_number = request.GET.get("page")
        items = paginator.get_page(page_number)
    else:
        items = []

    return render(request, "items/search.html", {"query": query, "items": items})

@swagger_auto_schema(method="get", operation_description="Get an item by ID")
@api_view(["GET"])
@csrf_exempt
def show(request, item_id):
    item = get_object_or_404(Item, pk=item_id)

    item_data = {
        "name": item.name,
        "description": item.description,
        "tags": [
            {"name": tag.name, "description": tag.description}
              for tag in item.tags.all()
            ],
    }

    if request.headers.get("Accept") == "application/json":
        return Response(item_data)

    return render(request, "items/show.html", {"item": item_data})