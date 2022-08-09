from django import template
register=template.Library()
@register.filter(name='newfilter_slice5_aliasname')
def newfilter_slice5(value):
    result = value[0:5]
    return result
def newfilter_slice_n(value,n):
    result = value[0:n]
    return result
register.filter('newfilter_slice_n_aliasname',newfilter_slice_n)
