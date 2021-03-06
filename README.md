# Effortless Bootstrap Web/Form Monkey Patch

Bootstrap your old web/form.py forms!

## Synopsis

Just because web.py hasn't been updated since 2012 doesn't mean you have to
settle for outdated HTML layouts. Scrap that 2001-era table-based form layout,
and use this module to create shiny, new Bootstrap 4-alpha forms!

Two ways to be happy:

1. Patch the old form classes.
2. Use our backwards-compatible form classes.

Either way, *you won't have to change a bit of your program logic.* It's a
just small change at the top of the program.

## How To Patch

To update your old webforms, just import and use the `patch()` function.

    from effortless_bootstrap_web_form_monkey_patch import patch
    patch()

Now you can continue to use your old web.py forms normally.

## How to Use Backwards-Compatible Classes

To use all-new but all-backwards-compatible classes, just import this package
instead of web.form.

    import effortless_bootstrap_web_form_monkey_patch as form

Now you can continue to use your old web.py forms normally.

## Remember to Update Your Templates

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

## Installation

    pip install effortless_bootstrap_web_form_monkey_patch

## Inspiration

 - Bootstrap 4 alpha form documentation at http://v4-alpha.getbootstrap.com/components/forms/
 - Runtime patching was learned at https://tryolabs.com/blog/2013/07/05/run-time-method-patching-python/

## Author

Justin McGuire &mdash; <jm@landedstar.com> &mdash; <a href="https://twitter.com/landedstar">@landedstar.com</a> &mdash; http://landedstar.com

## License

MIT License

