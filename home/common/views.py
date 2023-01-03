class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        ctx = super(TitleMixin, self).get_context_data(**kwargs)
        ctx['title'] = self.title
        return ctx