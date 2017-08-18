from flask import Markup, url_for, request


def build_menu_item(endpoint, name):
    is_active = "active" if request.endpoint == endpoint else ""
    return Markup(
        f'<li class="nav-item {is_active}">'
        f'<a class="nav-link" href="{url_for(endpoint)}">{name}</a>'
        f'</li>'
    )


def build_menu_item_as_filter(endpoint):
    is_active = "active" if request.endpoint == endpoint else ""
    return Markup(
        f'<li class="nav-item {is_active}">'
        f'<a class="nav-link" href="{url_for(endpoint)}">{endpoint.upper()}</a>'
        f'</li>'
    )
