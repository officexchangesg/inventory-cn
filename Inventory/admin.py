from django.contrib import admin
from .models import Chair
from .models import Desk
from .models import Pedestal
from .models import Cabinet

admin.site.register(Chair)
admin.site.register(Desk)
admin.site.register(Pedestal)
admin.site.register(Cabinet)
# Register your models here.
