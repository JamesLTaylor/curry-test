This project demonstrates an issue when certain decorators are used in conjunction
with `sphinx-docfx-yaml <https://github.com/docascode/sphinx-docfx-yaml>`_

When I run `make html`, I get:

.. code:: text

    Running Sphinx v1.5.5
    loading pickled environment... not yet created
    building [mo]: targets for 0 po files that are out of date
    building [html]: targets for 4 source files that are out of date
    updating environment: 4 added, 0 changed, 0 removed
    Can't inspect type <class 'functools._lru_cache_wrapper'>: utils.curry_and_docfx.cached_adder

    Exception occurred:
      File "c:\dev\python\curry-test\venv\lib\site-packages\docfx_yaml\extension.py", line 523, in insert_children_on_class
        insert_class = app.env.docfx_yaml_classes[datam[CLASS]]
    KeyError: 'utils.curry_and_docfx'
    The full traceback has been saved in C:\Users\James\AppData\Local\Temp\sphinx-err-vs7quk5x.log, if you want to report the issue to the de
    velopers.
    Please also report this if it was a user error, so that a better error message can be provided next time.
    A bug report can be filed in the tracker at <https://github.com/sphinx-doc/sphinx/issues>. Thanks!

This error does not appear to happen when the module is not in a sub-package