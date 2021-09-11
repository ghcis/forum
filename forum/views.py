from django.shortcuts import get_object_or_404, render

from .models import Thread


def index(request):
    return render(
        request,
        "forum/index.html",
        {"threads": Thread.objects.order_by("-pub_date")},
    )


def detail(request, thread_id):
    return render(
        request,
        "forum/detail.html",
        {"thread": get_object_or_404(Thread, pk=thread_id)},
    )
