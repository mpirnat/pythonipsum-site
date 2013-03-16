from wtforms import Form, IntegerField, validators


class LoremIpsumForm(Form):
    num_paragraphs = IntegerField('Paragraphs', [
            validators.Optional(), validators.NumberRange(1, 10)])
