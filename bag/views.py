from django.shortcuts import render


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/shopping_bag.html')
