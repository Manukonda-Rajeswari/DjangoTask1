from django.shortcuts import render
from django.db import models
from.views import generate_summary

# Create your views here.

def generate_summary(content):
    summary="This is a sample summary"
    return summary


class Conversation(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    content=models.TextField()
    summary=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def create_conversation(request):
        if request.method == 'POST':
            user = request.user
            content = request.POST.get('content')
            conversation = Conversation(user=user, content=content)
            conversation.save()  # Call the overridden save() method
            return redirect('conversation_list')
        return render(request, 'create_conversation.html')

   def update_conversation(request, pk):
       conversation = Conversation.objects.get(pk=pk)
       if request.method == 'POST':
           conversation.content = request.POST.get('content')
           conversation.save()  # Call the overridden save() method
           return redirect('conversation_list')
      return render(request, 'update_conversation.html', {'conversation': conversation})

    def save(self, *args, **kwargs):
        self.summary=generate_summary(self.content)
        super().save(*args, **kwargs)
