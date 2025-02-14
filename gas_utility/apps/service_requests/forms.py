from django import forms
from .models import ServiceRequest, ServiceRequestComment, ServiceRequestAttachment

class ServiceRequestForm(forms.ModelForm):
    attachments = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)
    
    class Meta:
        model = ServiceRequest
        fields = ['category', 'subject', 'description', 'priority']
    
    def save(self, commit=True):
        instance = super().save(commit=commit)
        for attachment in self.cleaned_data.get('attachments', []):
            ServiceRequestAttachment.objects.create(
                service_request=instance,
                file=attachment
            )
        return instance

class ServiceRequestCommentForm(forms.ModelForm):
    class Meta:
        model = ServiceRequestComment
        fields = ['content']
