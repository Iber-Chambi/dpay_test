from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def payment_page(request):
    if request.method == 'POST':
        # Aquí iría la lógica de procesamiento de pago
        return HttpResponse('Pago procesado correctamente')
    return render(request, 'dpay_test/payment.html')
