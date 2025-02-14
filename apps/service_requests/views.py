from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import ServiceRequest, ServiceRequestComment
from .forms import ServiceRequestForm, ServiceRequestCommentForm

class ServiceRequestListView(LoginRequiredMixin, ListView):
    model = ServiceRequest
    template_name = 'service_requests/list.html'
    context_object_name = 'requests'
    
    def get_queryset(self):
        if hasattr(self.request.user, 'customersupport'):
            return ServiceRequest.objects.all()
        return ServiceRequest.objects.filter(customer=self.request.user)

class ServiceRequestDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRequest
    template_name = 'service_requests/detail.html'
    context_object_name = 'request'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = ServiceRequestCommentForm()
        return context

class ServiceRequestCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRequest
    form_class = ServiceRequestForm
    template_name = 'service_requests/create.html'
    success_url = reverse_lazy('service_requests:list')
    
    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)
