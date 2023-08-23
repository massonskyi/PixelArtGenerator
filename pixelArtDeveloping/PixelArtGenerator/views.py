from django.shortcuts import render
from django.http import JsonResponse


def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        # Здесь вы можете выполнить обработку изображения
        # Например, сохранить его на сервере или обработать его с помощью сторонней библиотеки
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})


def index(request):
    return render(request, 'index.html')