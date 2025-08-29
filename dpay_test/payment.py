from pretix.base.payment import PaymentProvider

class DPayTestProvider(PaymentProvider):
    identifier = 'dpay_test'
    verbose_name = 'DPay Test'

    def is_enabled(self):
        return True

    def payment_form_render(self, request):
        # Renderiza tu formulario de pago aquí
        return '<form><button type="submit">Pagar con DPay Test</button></form>'

    def execute_payment(self, request):
        # Aquí iría la lógica para procesar el pago
        pass
