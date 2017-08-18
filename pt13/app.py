
from factories import (
    create_app,
    configure_error_handlers,
    configure_jinja,
    configure_blueprints,
    configure_extensions
)

app = create_app(
    DEBUG=True,
    SECRET_KEY='secret-here',
    # DEBUG_TB_PROFILER_ENABLED=True,
    # DEBUG_TB_TEMPLATE_EDITOR_ENABLED=True
)

configure_error_handlers(app)
configure_jinja(app)
configure_blueprints(app)

# blueprints can be registered here directly
from blueprints import contact
app.register_blueprint(contact.blueprint)
# NOTE: Changes in endpoints, now got blueprint.endpoint

# add extra extensions
configure_extensions(app)
