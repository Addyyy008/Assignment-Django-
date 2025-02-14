from django.db import models
from apps.accounts.models import Customer, CustomerSupport

class ServiceRequestCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]
    
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('URGENT', 'Urgent'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    category = models.ForeignKey(ServiceRequestCategory, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='MEDIUM')
    assigned_to = models.ForeignKey(CustomerSupport, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"#{self.id} - {self.subject}"

class ServiceRequestAttachment(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    file = models.FileField(upload_to='service_requests/attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Attachment for {self.service_request}"

class ServiceRequestComment(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author} on {self.service_request}"
