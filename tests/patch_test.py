import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from web import form

from effortless_bootstrap_web_form_monkey_patch import patch

def remove_optional_whitespace(s):
  """a lot of web.py includes newlines and tabs, these aren't necessary for HTML testing"""
  if s:
    return s.translate({ord(c): None for c in "\n\t"})
  else:
    return s

class TestPatch(unittest.TestCase):

  def setUp(self):
    patch()

  def test_textbox_render(self):
    result = form.Textbox(name='foo', description='bar').render()
    correct = '<input class="form-control" type="text" id="foo" name="foo">'
    self.assertEqual(result, correct)

  def test_textarea_render(self):
    result = form.Textarea(name='foo').render()
    correct = '<textarea class="form-control" id="foo" name="foo"></textarea>'
    self.assertEqual(result, correct)

  def test_checkbox_render(self):
    result = form.Checkbox(name='foo', value='bar').render()
    correct = '<input class="form-check-input" type="checkbox" id="foo" value="bar" name="foo"> foo'
    self.assertEqual(result, correct)

  def test_dropdown_render(self):
    result1 = remove_optional_whitespace(form.Dropdown(name='foo', args=['a', 'b', 'c'], value='b').render())
    correct1 = '<select class="form-control" id="foo" name="foo"><option value="a">a</option><option selected="selected" value="b">b</option><option value="c">c</option></select>'
    self.assertEqual(result1, correct1)

    result2 = remove_optional_whitespace(form.Dropdown(name='foo', args=[('a', 'aa'), ('b', 'bb'), ('c', 'cc')], value='b').render())
    correct2 = '<select class="form-control" id="foo" name="foo"><option value="a">aa</option><option selected="selected" value="b">bb</option><option value="c">cc</option></select>'
    self.assertEqual(result2, correct2)

  def test_radio_render(self):
    result1 = remove_optional_whitespace(form.Radio(name='foo', args=['a', 'b'], value='b').render())
    correct1 = '<div class="form-check"><label class="form-check-label"><input class="form-check-input" type="radio" id="foo" value="a" name="foo"> a</label></div><div class="form-check"><label class="form-check-label"><input checked="checked" name="foo" value="b" id="foo" type="radio" class="form-check-input"> b</label></div>'
    self.assertEqual(result1, correct1)

    result2 = remove_optional_whitespace(form.Radio(name='foo', args=[('a', 'aa'), ('b', 'bb'), ('c', 'cc')], value='b').render())
    correct2 = '<div class="form-check"><label class="form-check-label"><input class="form-check-input" type="radio" id="foo" value="a" name="foo"> aa</label></div><div class="form-check"><label class="form-check-label"><input checked="checked" name="foo" value="b" id="foo" type="radio" class="form-check-input"> bb</label></div><div class="form-check"><label class="form-check-label"><input class="form-check-input" type="radio" id="foo" value="c" name="foo"> cc</label></div>'
    self.assertEqual(result2, correct2)

  def test_button_render(self):
    result = form.Button(name='foo').render()
    correct = '<button class="btn btn-primary" type="submit" id="foo" name="foo">foo</button>'
    self.assertEqual(result, correct)

  def test_form_render(self):
    result = remove_optional_whitespace(form.Form(form.Textbox("x")).render())
    correct = '<div class="form-group"><label id="x">x</label><input class="form-control" type="text" id="x" name="x"></div>'
    self.assertEqual(result, correct)

  def test_form_with_error_render(self):
    input_field = form.Textbox("x")
    input_field.note = "ERROR"
    result = remove_optional_whitespace(form.Form(input_field).render())
    correct = '<div class="form-group has-danger"><label id="x">x</label><input class="form-control form-control-danger" type="text" id="x" name="x"><div class="form-control-feedback">ERROR</div></div>'
    self.assertEqual(result, correct)


if __name__ == '__main__':
    unittest.main()

