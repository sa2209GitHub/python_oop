# Nested Classes

class Women:
    title = "class object for the 'title' field"
    photo = "class object for the 'photo' field"
    ordering = "class object for the 'ordering' field"

    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.meta = self.Meta(user + '@' + password)

    class Meta:
        ordering = ['id']

        def __init__(self, access) -> None:
            self._access = access


w = Women(user='root', password='12345')
print(w.ordering)
print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)
