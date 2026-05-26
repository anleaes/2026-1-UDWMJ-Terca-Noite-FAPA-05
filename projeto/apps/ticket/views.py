from django.shortcuts import render

# Create your views here.
@client_required
def ticket_list(request, client_id):
    template_name = 'ticket/ticket_list.html'

    tickets = Ticket.objects.filter(client_id=client_id)

    context = {
        'tickets': tickets,
    }

    return render(request, template_name, context)