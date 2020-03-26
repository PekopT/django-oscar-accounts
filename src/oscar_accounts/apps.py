from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig

class AccountsConfig(AppConfig):

    name = 'oscar_accounts'
    verbose_name = _('Accounts')
    namespace = 'oscar_accounts'
