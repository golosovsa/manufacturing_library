class LowerCaseFieldMixin:
    def get_prep_value(self, value):
        return str(value).lower()
