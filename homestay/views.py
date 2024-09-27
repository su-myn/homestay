from django.shortcuts import render, redirect
from .forms import RepairFormForm, AdhocItemFormForm
from .models import RepairForm, AdhocItemForm, Tag
from django.contrib import messages
from django.core.mail import EmailMessage
from django.db.models import F, Count, Min




def index(request):
    return render(request, "index.html")

def repair(request):
    sort_by = request.GET.get('sort_by', 'date')  # Default sort by date
    order = request.GET.get('order', 'asc')  # Default ascending order

    repair_forms = RepairForm.objects.all()

    if order == 'desc':
        sort_by = F(sort_by).desc(nulls_last=True)
    else:
        sort_by = F(sort_by).asc(nulls_last=True)

    repair_forms = repair_forms.order_by(sort_by)

    context = {
        'repair_forms': repair_forms,
        'current_sort': request.GET.get('sort_by', 'date'),
        'current_order': order,
    }
    return render(request, 'repair.html', context)



def replace(request):
    return render(request, "replace.html")

def complain(request):
    return render(request, "complain.html")

def aircond_log(request):
    return render(request, "aircond_log.html")

def refill_log(request):
    return render(request, "refill_log.html")

def addAircond(request):
    return render(request, "add_aircond.html")

def addRepair(request):
    if request.method == "POST":
        form = RepairFormForm(request.POST)
        if form.is_valid():

            unit_number = form.cleaned_data["unit_number"]
            contractor = form.cleaned_data["contractor"]
            repair_issue = form.cleaned_data["repair_issue"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            price = form.cleaned_data["price"]


            message_body = f"""
A new Repair Issue was submitted.

Details:
- Unit Number: {unit_number}
- Contractor: {contractor}
- Repair Issue: {repair_issue}
            """
            email_message = EmailMessage("A New Repair Work was submitted", message_body, to=["tansumyn@gmail.com"])
            email_message.send()

            RepairForm.objects.create(unit_number=unit_number, contractor=contractor, repair_issue=repair_issue, email=email, date=date, price=price)
            messages.success(request, "Form Submitted Successfully!")
    return render(request, "add_repair.html")


def adhoc_item(request):
    adhoc_forms = AdhocItemForm.objects.all()

    # Get the sort parameter from the URL
    sort_by = request.GET.get('sort', 'adhoc_item')

    # Define valid sorting fields
    valid_sort_fields = ['adhoc_item', 'remark', 'category', 'date_created','tag']

    # Check if the sort parameter is valid
    if sort_by in valid_sort_fields:
        if sort_by == 'tag':
            # Sort by the first tag name
            adhoc_forms = adhoc_forms.annotate(
                first_tag_name=Min('tags__name')
            ).order_by(F('first_tag_name').asc(nulls_last=True))
        else:
            # Use F() to reference model fields
            adhoc_forms = adhoc_forms.order_by(F(sort_by).asc(nulls_last=True))

    return render(request, "adhoc_item.html", {'adhoc_forms': adhoc_forms, 'current_sort': sort_by})

def addItem(request):
    if request.method == "POST":
        form = AdhocItemFormForm(request.POST)
        if form.is_valid():

            tags = form.cleaned_data["tags"]
            category = form.cleaned_data["category"]
            adhoc_item = form.cleaned_data["adhoc_item"]
            remark = form.cleaned_data["remark"]
            #date_created = form.cleaned_data["date_created"]

            message_body = f"""
A new Adhoc Item was created.

Details:
- Adhoc Item: {adhoc_item}

            """
            email_message = EmailMessage("A New Adhoc Item was created", message_body, to=["tansumyn@gmail.com"])
            email_message.send()

            #oldcode (can use also)
            #AdhocItemForm.objects.create(adhoc_item=adhoc_item, remark=remark, category=category, tags=tags)

            # Create the AdhocItemForm instance without tags
            new_item = AdhocItemForm.objects.create(
                adhoc_item=adhoc_item,
                remark=remark,
                category=category
            )

            # Add tags to the new item
            new_item.tags.set(tags)

            messages.success(request, "Form Submitted Successfully!")
#    return render(request, "add_item.html")
            return redirect('/adhoc_item/')  # Replace 'some_success_url' with your actual URL name
    else:
        form = AdhocItemFormForm()

    return render(request, "add_item.html", {'form': form})