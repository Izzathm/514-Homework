from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import DatePicker
from tethys_sdk.gizmos import RangeSlider
@login_required()
def home(request):

    # Date Picker Options
    date_picker = DatePicker(name='date1',
                             display_text='Date',
                             autoclose=True,
                             format='MM d, yyyy',
                             start_date='2/15/2014',
                             start_view='decade',
                             today_button=True,
                             initial='February 15, 2014')

    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'

        }
    )


    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button,
        'date_picker': date_picker,


    }

    return render(request, 'izzatmapapp/home.html', context)

def map(request):

    context = {

    }

    return render(request, 'izzatmapapp/map.html', context)

def data(request):
    slider1 = RangeSlider(display_text='Slider 1',
                          name='slider1',
                          min=0,
                          max=100,
                          initial=50,
                          step=1)

    slider2 = RangeSlider(display_text='Slider 2',
                          name='slider2',
                          min=0,
                          max=1,
                          initial=0.5,
                          step=0.1,
                          disabled=True,
                          error='Incorrect, please choose another value.')

    context = {
        'slider1': slider1,
        'slider2': slider2,

    }

    return render(request, 'izzatmapapp/data.html', context)

def about(request):
    context = {

    }

    return render(request, 'izzatmapapp/about.html', context)
def proposal(request):
    context = {

    }

    return render(request, 'izzatmapapp/proposal.html', context)
def diagrams(request):
    save_button = Button(
        display_text='Home Page',
        name='Home Page',
        icon='home page',
        style='success',
        attributes={
            'data-toggle': 'tooltip',
            'data-placement': 'top',
            'title': 'Home Page'
        }
    )
    context = {'save_button': save_button,

    }

    return render(request, 'izzatmapapp/diagrams.html', context)
