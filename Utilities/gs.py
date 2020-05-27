from snippets.models import SystemProperties


class GlideSystem:

    def __init__(self):
        pass

    def getProperty(self, key):
        a = SystemProperties.objects.filter(key=key)
        return a


a = GlideSystem()
a.getProperty('name')


