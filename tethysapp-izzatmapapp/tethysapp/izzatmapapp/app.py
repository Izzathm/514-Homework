from tethys_sdk.base import TethysAppBase, url_map_maker


class Izzatmapapp(TethysAppBase):
    """
    Tethys app class for Izzats Map App.
    """

    name = 'Izzats Map App'
    index = 'izzatmapapp:home'
    icon = 'izzatmapapp/images/icon.gif'
    package = 'izzatmapapp'
    root_url = 'izzatmapapp'
    color = '#27AE60'
    description = 'This is the coolest Map App EVER'
    tags = '&quot;Geospatial&quot;,&quot;ArcGIS&quot;'
    enable_feedback = True
    feedback_emails = ["izzatmukattash11@hotmail.com"]

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='izzatmapapp',
                controller='izzatmapapp.controllers.home'
            ),

            UrlMap(
                name='map',
                url='izzatmapapp/map',
                controller='izzatmapapp.controllers.map'
            ),

            UrlMap(
                name='data',
                url='izzatmapapp/data',
                controller='izzatmapapp.controllers.data'
            ),

            UrlMap(
                name='about',
                url='izzatmapapp/about',
                controller='izzatmapapp.controllers.about'
            ),
            UrlMap(
                name='proposal',
                url='izzatmapapp/proposal',
                controller='izzatmapapp.controllers.proposal'
            ),
            UrlMap(
                name='diagrams',
                url='izzatmapapp/diagrams',
                controller='izzatmapapp.controllers.diagrams'
            ),
        )

        return url_maps
