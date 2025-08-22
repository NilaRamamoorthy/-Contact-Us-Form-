

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
# from .forms import ContactForm  # Uncomment when using ModelForm
from .models import ContactSubmission

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        errors = {}
        if not name:
            errors['name'] = "Name is required."
        if not email:
            errors['email'] = "Email is required."
        if not message:
            errors['message'] = "Message is required."

        if errors:
            return render(request, "contact/contact.html", {"errors": errors, "name": name, "email": email, "message": message})

        # Save to database (later optional)
        ContactSubmission.objects.create(name=name, email=email, message=message)

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")

    return render(request, "contact/contact.html")
