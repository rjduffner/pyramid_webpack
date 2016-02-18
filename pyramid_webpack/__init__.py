import json
import logging

logger = logging.getLogger(__name__)


def get_stylesheet_bundle(request, *args):
    """
    Convenience tag to output 1 or more stylesheet tags.

    :param args: 1 or more stylesheet file names
    :return: Link tag(s) containing the asset
    """
    tags = []

    for arg in args:
        asset_path = request.assets_get_asset_url('{0}.css'.format(arg))
        if asset_path:
            tags.append(
                '<link rel="stylesheet" href="{0}">'.format(asset_path))

    return '\n'.join(tags)


def get_javascript_bundle(request, *args):
    """
    Convenience tag to output 1 or more javascript tags.

    :param args: 1 or more javascript file names
    :return: Script tag(s) containing the asset
    """
    tags = []

    for arg in args:
        asset_path = request.assets_get_asset_url('{0}.js'.format(arg))
        if asset_path:
            tags.append('<script src="{0}"></script>'.format(asset_path))

    return '\n'.join(tags)


def get_asset_url(request, asset):
    if '//' in asset:
        return asset

    if asset not in request.registry.settings['webpack_assets']:
        return None

    return '{0}{1}'.format(request.registry.settings['webpack_assets_url'],
                           request.registry.settings['webpack_assets'][asset])


def includeme(config):
    webpack_stats = config.registry.settings.get('webpack_manifest_path')
    webpack_assets_url = config.registry.settings.get('webpack_assets_url')

    webpack_local_assets_dir = config.registry.settings.get('webpack_local_assets_dir')

    try:
        with open(webpack_stats, 'r') as stats_json:
            stats = json.load(stats_json)

            if webpack_assets_url:
                assets_url = webpack_assets_url
            else:
                assets_url = stats['publicPath']

            if webpack_local_assets_dir:
                config.add_static_view(name='static',
                                       path=webpack_local_assets_dir)

            config.registry.settings['webpack_assets'] = stats['assets']
            config.registry.settings['webpack_assets_url'] = assets_url


    except IOError:
        logger.exception("Failed to read asset manifest")
        raise RuntimeError(
            "Pyramid-Webpack requires 'webpack_manifest_path' to be set and "
            "it must point to a valid json file.")

    config.add_request_method(get_stylesheet_bundle, 'assets_get_stylesheet_bundle')
    config.add_request_method(get_javascript_bundle, 'assets_get_javascript_bundle')
    config.add_request_method(get_asset_url, 'assets_get_asset_url')
