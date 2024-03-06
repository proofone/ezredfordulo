from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils import timezone
from palyazat.models import Kiiras


@plugin_pool.register_plugin
class KiirasokPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "palyazat/list_inner.html"

    def render(self, context, instance, placeholder):
        ctxt = super().render(context, instance, placeholder)
        ctxt['object_list'] = Kiiras.objects.filter(deadline__gt=timezone.now())
        
        return ctxt
