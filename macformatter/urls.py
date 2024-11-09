from django.urls import path

from macformatter.views import TextFormatView, format_text_view

urlpatterns = [
    path('', format_text_view, name='format-text'),
    path('format', TextFormatView.as_view(), name='format'),
]
