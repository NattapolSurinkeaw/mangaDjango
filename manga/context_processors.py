from .models import Category  # แก้ไขจาก model เป็น models

def categories(request):
    categories = Category.objects.filter(display=True).order_by('priority')
    return {'categories': categories}