class StringFromFieldsMixin:
    string_fields = ()

    def __str__(self):
        return ' '.join(
            f"{getattr(self, str_field, None)}" for str_field in self.string_fields
        )
