from pathlib import Path
from django.http import FileResponse, Http404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class CompteRenduView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        filename = self.kwargs["filename"]
        file_path = (
            Path(__file__).resolve().parent
            / "documents"
            / "compte_rendu"
            / filename
        )
        try:
            return FileResponse(open(file_path, "rb"), content_type="application/pdf")
        except FileNotFoundError:
            raise Http404()
