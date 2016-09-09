from unittest import TestCase

from effortless_bootstrap_web_form_monkey_patch import patch

class TestPatch(TestCase):

  form = web.form.Form(
    web.form.Textbox('MyTextbox', description="A Text Box"),
    web.form.Textarea('MyTextarea'),
    web.form.Checkbox('MyCheckbox'), 
    web.form.Dropdown('MyDropdown', ['Option1', 'Option2', 'Option3'])) 
    web.form.Button('Submit'),
  )

  def __init__(self):
    patch()

  def test_is_patched(self):
    self.assertTrue(isinstance(s, basestring))

  def test_form_render(self): pass
  def test_input_render(self): pass
  def test_checkbox_render(self): pass
  def test_radio_render(self): pass
