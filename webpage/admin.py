from django.contrib import admin
from .models import User
from .models import Question
from .models import Question_choices
from .models import Sms1
# Register your models here.

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Question_choices)
admin.site.register(Sms1)