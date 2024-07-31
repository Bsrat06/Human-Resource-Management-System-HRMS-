from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def user_in_groups(context, *group_names):
    user = context['request'].user
    return user.groups.filter(name__in=group_names).exists()
