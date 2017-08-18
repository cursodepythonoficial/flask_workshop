# Now using factory pattern <-- RECOMMENDED!!

from factories import (
    create_app,
    configure_error_handlers,
    configure_jinja,
    configure_views
)

app = create_app(DEBUG=True)
configure_error_handlers(app)
configure_jinja(app)
configure_views(app)

app.run(use_reloader=True)
