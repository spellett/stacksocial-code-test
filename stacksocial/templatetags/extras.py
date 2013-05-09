from django import template
from django.template.defaultfilters import stringfilter

import re

register = template.Library()

@register.filter
@stringfilter
def markup_twitter_handles(text):
    handle_re = r'@[\w]+\b'

    updated_text = text

    for handle in re.findall(handle_re, text):
        markup = '<a href="../user/%s" class="twitterHandle">%s</a>' % (handle[1:], handle)
        updated_text = text.replace(handle, markup)

    return updated_text
