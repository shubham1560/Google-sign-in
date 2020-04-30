from snippets.models import SystemProperties


class GlideSystem:

    def getProperty(self, key):
        a = SystemProperties.objects.filter(key=key)
        return a


