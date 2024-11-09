from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TextFormatSerializer
from django.http import JsonResponse
import re


class TextFormatView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TextFormatSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']

            # Remove colons and hyphens from the text
            cleaned_text = re.sub(r'[:\-]', '', text)

            # Add a period after every four characters
            transformed_text = '.'.join(cleaned_text[i:i + 4] for i in range(0, len(cleaned_text), 4))
            return Response({"original_text": text, "transformed_text": transformed_text.lower()},
                            status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def format_text_view(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        text = request.POST.get('text', '')

        # Remove colons and hyphens from the text
        cleaned_text = re.sub(r'[:\-]', '', text)

        # Add a period after every four characters
        transformed_text = '.'.join(cleaned_text[i:i + 4] for i in range(0, len(cleaned_text), 4))

        return JsonResponse({"transformed_text": transformed_text.lower()}, )

    # Render HTML template for GET request
    return render(request, 'format_text.html')
