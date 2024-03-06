from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.urls import path, re_path

from palyazat.views import KiirasDetailView, KiirasListView


urls = [
    path("", KiirasListView.as_view()),
    path("<int:pk>/", KiirasDetailView.as_view(), name="kiiras")
]


@apphook_pool.register
class PalyazatApphook(CMSApp):
    app_name = "palyazat"
    name = "Pályázat apphook-ja"

    def get_urls(self, page=None, language=None, **kwargs):
        return urls
