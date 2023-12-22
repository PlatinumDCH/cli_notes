from cli.models.field import Title, Description, Tag


class Note:
    counter = 1

    def __init__(self, title):
        self.id = type(self).counter
        self.title = Title(title)
        self.description = None
        self.tags = []
        type(self).counter += 1

    def __iter__(self):
        yield "id", self.id
        yield "title", self.title if self.title else None
        yield "description", self.description if self.description else None
        yield "tags", [tag for tag in self.tags]

    def to_dict(self):
        return dict(self)

    def __str__(self):
        tags_str = f"Tags: {', '.join(map(str, self.tags))}" if self.tags else ""
        return f"ID: {self.id}; Title: {self.title}; Description: {self.description}; {tags_str}"

    def add_description(self, description):
        self.description = Description(description)

    def edit_description(self, new_description):
        self.description = Description(new_description)

    def edit_title(self, new_title):
        self.title = Title(new_title)

    def add_tag(self, tag):
        self.tags.append(Tag(tag))

    def delete_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
