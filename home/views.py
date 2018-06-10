


from django.views.generic import TemplateView, ListView
from forecast.models import Forecasts
#class home_view(TemplateView):
#    template_name = "home.html"

class home_view(ListView):
    model = Forecasts
    template_name = 'home.html' 
    context_object_name = 'forecast_list'  # Default: object_list
    paginate_by = 3
    queryset = Forecasts.objects.all()  # Default: Model.objects.all()