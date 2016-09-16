import web
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import effortless_bootstrap_web_form_monkey_patch

effortless_bootstrap_web_form_monkey_patch.patch()

render = web.template.render('./')

urls = (
  '/', 'website',
)

class website:

  # create a complex form
  form = web.form.Form(
    web.form.Textbox('a-textbox', web.form.notnull, description="textbox description"),
    web.form.Password('a-password', description="password description"),
    web.form.Textarea('a-textarea', description="textarea description"),
    web.form.Checkbox('a-checkbox', description="checkbox description", checked=False),
    web.form.Checkbox('another-checkbox', description="checkbox description", checked=True),
    web.form.Dropdown('a-dropdown', description="dropdown description", args=[('first', 'first value'), ('second', 'second value'), ('third', 'third value')], value='second'),
    web.form.Radio('a-radio', description="radio description", args=[('alpha', 'alpha value'), ('beta', 'beta value'), ('gamma', 'gamma value')], value='beta'),
    web.form.File('a-file', description="file upload description"),
    web.form.Hidden('a-hidden', description="this should be hidden"),
    web.form.Button('Submit your data'),
  )

  def GET(self):
    form = self.form()
    return render.website(form)

if __name__ == '__main__':
  app = web.application(urls, globals())
  app.run()

