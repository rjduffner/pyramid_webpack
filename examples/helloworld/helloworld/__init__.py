from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    config.include('pyramid_jinja2')
    config.include('pyramid_webpack')

    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
