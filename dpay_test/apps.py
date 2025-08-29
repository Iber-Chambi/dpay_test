from django.utils.translation import gettext_lazy

from . import __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    default = True
    name = "dpay_test"
    verbose_name = "dpay_test"

    class PretixPluginMeta:
        name = gettext_lazy("dpay_test")
        author = "ichambi"
        description = gettext_lazy("dpay_test")
        visible = True
        version = __version__
        category = "PAYMENT"
        compatibility = "pretix>=0.0.1"
        settings_links = []
        navigation_links = []

    def ready(self):
        from . import signals  # NOQA

        def get_payment_providers(self, *args, **kwargs):
            from .payment import DPayTestProvider
            return [DPayTestProvider]
