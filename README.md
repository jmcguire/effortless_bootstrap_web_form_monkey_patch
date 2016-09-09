# Synopsis

Patch the old Form classes in web.py to create Bootstrap-compatible forms

Just because web.py hasn't been updated since 2012 doesn't mean you have to
settle for outdated HTML layouts. Scrap that 2001-era table-based form layout,
and use this module to create shiny, new Bootstrap 4-alpha forms!

# Example

To update your old webforms, just import and use the `patch()` function.

    from effortless_bootstrap_web_form_monkey_patch import patch
    patch()

Now you can continue to use your old web.py forms normally.

Oh yeah, make sure you update the templates to use Bootstrap. The most
important piece to remember is to wrap all Bootstrap items with a `.container`
div.

    <div class="container">
      <form>
        $:form.render()
      </form>
    </div>

And of course you need the CSS. If you don't want to host it locally, use their
CDN by adding this piece to the header.

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.4/css/bootstrap.min.css" integrity="2hfp1SzUoho7/TsGGGDaFdsuuDL0LX2hnUp6VkX3CUQ2K4K+xjboZdsXyp4oUHZj" crossorigin="anonymous">

For more information on using Bootstrap 4-alpha, check out http://v4-alpha.getbootstrap.com/ .

# Installation

Eventually, this will be a full fledged package, and you will be able to do this.

    pip install effortless_bootstrap_web_form_monkey_patch

# Author

Justin McGuire &mdash; <jm@landedstar.com> &mdash; <a href="https://twitter.com/landedstar">@landedstar.com</a> &mdash; http://landedstar.com

# License

MIT License

