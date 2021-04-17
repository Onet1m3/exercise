from .models import MenuItem


def list_menu_items(request):
    """Список меню"""
    return {"menu_items": MenuItem.objects.all()}