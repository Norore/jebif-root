# Removed #

## django.views.generic.simple ##

django.views.generic.simple was deprecated and doesn't exist beyond django 1.4. Is there a specific reason you are using a development branch of django and not the latest stable version (1.4.2)?

Source: http://stackoverflow.com/a/13442589/1866679

## render_to_template ##

I would recommend either using django 1.4.2 (which has django.views.generic.simple or use render (from django.shortcuts import render) instead of direct_to_template.

Source: http://stackoverflow.com/a/13442589/1866679
