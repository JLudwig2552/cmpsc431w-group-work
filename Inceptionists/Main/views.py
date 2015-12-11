from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from Main.models import Page, Categories, Items
from Main.forms import UsersForm

import itertools
import MySQLdb as mdb
import sys

'''
def category(request, category_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        category = Categories.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Categories.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        pass

    # Go render the response and return it to the client.
    return render(request, 'Main/index.html', context_dict)

'''

def add_user(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = UsersForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = UsersForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'Main/add_user.html', {'form': form})

def category(request, category_name):
    try:
        con = mdb.connect('localhost', 'Admin1', 'Admin1', 'Inceptionists');

        cur = con.cursor()
        #cur.execute("SELECT name FROM items")
        cur.execute("SELECT name FROM items WHERE category = %s", [category_name])

        itemss = list(itertools.chain.from_iterable(cur))

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()

    template = loader.get_template('Main/category.html')
    context = RequestContext(request, {
        'itemss': itemss,
    })
    return HttpResponse(template.render(context))
    #return HttpResponse("Category name : %s " % category_name)

def index(request):
    try:
        con = mdb.connect('localhost', 'Admin1', 'Admin1', 'Inceptionists');

        cur = con.cursor()
        cur.execute("SELECT name FROM categories")

        #categories = cur.fetchall()
        categoriess = list(itertools.chain.from_iterable(cur))  #no longer being used

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:

        if con:
            con.close()

    category_list = Categories.objects.all()
    context_dict = {'categories': category_list}

    template = loader.get_template('Main/index.html')
    context = RequestContext(request, {
        'categoriess': categoriess,
    })
    #return render(request, 'Main/index.html')
    #return HttpResponse("Database version : %s " % ver)
    #return HttpResponse(template.render(context))    <---previous working version
    return HttpResponse(template.render(context_dict))


def about(request):
    return HttpResponse("Programmed by Fliu and Rcamp")

