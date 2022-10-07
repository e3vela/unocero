from wagtail.admin.views.account import BaseSettingsPanel
from wagtail.core import hooks
from .forms import CustomSettingsForm


@hooks.register("register_account_settings_panel")
class CustomSettingsPanel(BaseSettingsPanel):
    name = "custom"
    title = "social accounts"
    order = 500
    form_class = CustomSettingsForm
    form_object = "user"
