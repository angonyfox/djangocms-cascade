===============
Release History
===============

0.17.10
=======
* Fix problem of missing referer, required to determine the current page when accessing an **IconFontPlugin**
  from inside the CKEditor.

0.17.9
======
* Catch IconFont exceptions, if CKEditor is used outside of CMS pages.
* Fix: Supress AttributeError in `BootstrapCardPlugin.get_identifier`.

0.17.8
======
* For better reusability of ``IconFont``-s: Refactor method ``unzip_archive`` into external
  utility function.

0.17.7
======
* Fix: Restore-to-Clipboard with data from differently configured instances of Cascade
  may cause an Internal Server Error. Now such an import shows an error message importing
  whatever is parsable.
* Add ``role="button"`` to the **ButtonPlugin**.
* Optionally add CSS class ``stretched-link`` introduced in Bootstrap-4.3 to ``<a href="...">``.
* Fix: We can not see the SVG file, if the image file existed and was not found, specifically 
  when copying a Persisted clipboard.
* Fix: If jsonfield is serialized as string, convert and reload as JSON.
* Fix: **ImagePlugin** / **PicturePlugin** can't be copied by clipboard CMS.
* Fix: Strides Plugin Element object has no attribute ``placeholder``.


0.17.6
======
* Fix: Tabset support for Bootstrap-4 using jQuery.


0.17.5
======
* Fix: Limit the number of results to 16 while searchung for a link.


0.17.4
======
* Fix: TextIconPlugin does not raise an exception if no IconFont was selected for the current page.


0.17.3
======
* Use ``HeavySelect2Widget`` to choose the CMS page if **django-select2** is available.
* For **ButtonPlugin**, make IconFont optional.
* Fix: Limit number of decimal places in breakpoint selection to one.
* Increase width of select2 widget to 400px.
* Add feature: if a plugin use ImageFormMixin and that the source of the media is missing,
  instead it uses a svg with old witdh and heigth who use srcset.

0.17.2
======
* Fix  problem with lazy evaluation during initialization by lazy formating translated strings
  in ``BootstrapUtilities``.
* Fix font-size icon don't work without text_align.
* In ``HeadingPlugin`` set width of content field to 100%.
* Add nicer ColorPicker widget for fields containing a color.

0.17.1
======
* User margin classes for HeadingPlugin as provided by Bootstrap-4.
* In SectionMixin, fix problem if no cascadepage is associated with CMS page.
* Fix: Can add BootstrapColumn with interface +.
* Fix: Add missing file carsousel template file.
* Render a nicer warning box if plugin template not found.
* Fix problem with missing placeholderreference.
* Adopted examples to support Bootstrap-3 as well as Bootstrap-4.
* Add filter function to find font-icon by name.

0.17
====
* Add support for django-CMS 3.5.
* Add support for Bootstrap-4.
* Drop support for Django-1.9.
* Remove deprectated function ``cmsplugin_cascade.utils.resolve_dependencies``.
* Replace function ``cmsplugin_cascade.utils.format_lazy`` by Django's internal function.
* Font Icons now must be chosen per page, rather than for each Icon plugin. This prevents the
  problem of rendering unwanted symbols in case more than one Icon Font was selected on a given CMS
  page. Therefore, after migrating to this version of **djangocms-cascade**, check on all CMS
  pages if the selected icon font is the desired one. Use the django-CMS toolbar, and click onto
  ``Page > Choose Icon Font…``.
* Fix: Prevent double registration of proxy models.
* Append fields to plugins, which are missing in list ``glossary_fields_order``.


0.16.3
======
* Fix **CarouselPlugin**, if used with newer versions of the **angular-ui-bootstrap** NPM library.
* Fix corner-case of dysfunctional **elif** evaluation in **SegmentPlugin**.


0.16.2
======
* Fix Markdown while uploading to PyPI.


0.16.1
======
* Fix: Compute link of ``Page`` object holding documentation menu.
* Fix regression in sharable glossary caused by upgrade to Django-1.11.
* Adopt child plugin editing for django-CMS 3.5 to behave as earlier versions.
* Icons in the Text field may have a foreground color.


0.16
====
* Drop support for **Django-CMS CKEditor** version 3.4 in favor of version 3.5 and later. In ``CKEDITOR_SETTINGS``
  change the ``skin`` setting to ``moono-lisa``.
* Remove monkey patch required for django-CMS 3.4. This has been fixed by applying
  this pull request: https://github.com/divio/django-cms/pull/5809
* Icons inside the ``TextPlugin`` can have an optional link.
* Simplify JavaScript plugins to extend alternative link types.
* Added ``TextImagePlugin`` allowing to add simple images inside the CKEditor.
* Move common image functionality into utility class ``cmsplugin_cascade/image.py``.
* Optional checkbox to hide plugin is moved at the end of the editor window.


0.15.5
======
* Fix: ImagePlugin should not have duplicate css_classes and inline_styles if there is a link.
* Fix regression: Cascade Clipboard did not work anymore with Django<=1.10.
* Fix: If ``USE_THOUSAND_SEPARATOR`` was set to ```True``, some templates where not unlocalized
  properly.


0.15.4
======
* Fix: In ``FramedIconPlugin``, use ``ColorWidget`` for glossary attribute ``color`` instead of
  using a text field. This allows to inherit the foreground color from the given CSS settings.
  This fix required to run migration ``0018_iconfont_color``.
* Fix: A Bootstrap Row now can be the child of a Jumbotron Plugin.
* Added a CMSAppHook named "Sphinx Documentation" which routes a documentaion tree directly onto
  the ``SphinxDocsView``. Therefore the documentation tree can be handled directly by the CMS and
  doesn't require any special routes in the project's URL config.

0.15.3
======
* Bugfix: If more than one CheckboxInput in plugin only the first seem work correctly.
* Bugfix: Cascade works properly if ``'cmsplugin_cascade.icon'`` is missing in ``INSTALLED_APPS``.

0.15.1 and 0.15.2
=================
* Fixed one failing occurrence of ``settings.SPHINX_DOCS_ROOT``.

0.15
====
* Posibility to integrate documentation pages generated by Sphinx, manged by the CMS menu tree.

0.14.4
======
* Adopted button- and container selection widget rendering to work with Django-1.11.
* Fixed clipboard issued regarding Django-1.11.

0.14.3
======
* Fix: If plugin is missing, now templatetag ``render_plugin`` renders empty string, instead
  of raising a TemplateSyntaxError.
* Fix: Method ``RenderTemplateMixin.get_render_template()`` now properly expands templates with
  placeholders.

0.14.2
======
* In Leaflet Map Plugin:
  * For unset markers, place the position into the center of the current map.
  * Fix positioning of the markers anchor.
* When using templatetag ``render_cascade``, the HTML content is cached to improve performance.

0.14.1
======
* Restored deleted font files.
* Fix template for rendering a Google map.
* Add fields ``offset`` and ``limit`` to **SecondaryMenuPlugin**, to segment the menus.
* Fix bug in HeadingPlugin: Can not be used in static_placeholder tag.
* Fix bug in HeadingPlugin: HTML entities, such as ampersand can be used as content.
* Fix in Panel Plugin: Show identifier in Placeholder tree.
* Fix in Section Plugin: Can now be used in ``static_placeholder``.

0.14
====
* Added static rendering of a serialized representation of plugins copied from a ``placeholder``
  to the clipboard. For details, please read on how to :doc:`strides`.

0.13.1
======
* Prepare for Django-1.11 compatibility: Replace renderer classes by specialized widgets
  overriding its ``render()`` method.

0.13
====
* Added Leaflet Plugin which allows to integrate interactive maps from Google, Mapbox and
  OpenStreetMap. The editor can add any number of markers using arbitrary logos with an optional
  popup box.
* Refactored the app's settings modules to use an ``AppSettings`` class, rather than merging
  application specific settings on the fly.

0.12.5
======
* Fixed: Wrapper for transparent plugins did not find all children which declared
  these kind of plugins as their parents.

0.12.4
======
* Fixed: Initial Image is reseted after reopening Image plugin editor.
* Changed order of fields in Accordion plugin editor.
* Moved directory ``workdir`` for demo project from root folder into examples.

0.12.3
======
* Fixed: When using an Element ID while adding a Heading Plugin, under certain circumstances
  the validation ran into an infinite loop.

0.12.2
======
* Fixed: Allow transparent instances as root objects.

0.12.1
======
* Fixed: Do not invoke ``{% addtoblock "css" %}...`` for empty values of ``stylesheet_url``.
* Renamed buttons in clipboard admin to "Insert Data" (instead of "Save") and "Restore Data"
  (instead of "restore").

0.12.0
======
* Added compatibility for Django version 1.10.
* Added compatibility for django-CMS version 3.4.
* Added monkey patch to resolve issues handled by PR https://github.com/divio/django-cms/pull/5809
* Added compatibility for djangocms-text-ckeditor-3.4.
* **Important for AngularJS users**: Please upgrade to angular-ui-bootstrap version 0.14.3. All
  versions later than 0.13 use the prefix ``uib-`` on all AngularJS directives, hence this upgrade
  is required.
* In the ``CarouselSlide`` plugin, caption is added as a child ``TextPlugin`` instead of using the
  glossary. Currently the migration of ``TextLinkPlugins`` inside this caption field does not work
  properly. Please create an issue, if you really need it.
* Added method ``value_omitted_from_data`` to ``JSONMultiWidget`` to override the Django method
  implemented in ``django.forms.widgets.MultiWidget``.
* In ``cmsplugin_cascade.models.CascadeElement`` the foreign key ``shared_glossary`` now is marked
  as editable. Instead to plugins without sharable glossary, the attribute
  ``exclude = ['shared_glossary']`` is added.
* Instead of handling ring.js plugin inheritance through ``get_ring_bases()``, Cascade plugins
  just have to add ``ring_plugin = '...'`` to their class declaration.
* Function ``cmsplugin_cascade.utils.resolve_dependencies`` is deprecated, since Javascript
  dependencies now are handled via their natural inheritance relation.
* The configuration option ``settings.CMSPLUGIN_CASCADE['dependencies']`` has been removed.
* Added method ``save()`` to model ``SharedGlossary``, which filters the glossary to be stored to
  only those fields marked as sharable.
* Accessing the CMS page via ``plugin_instance.page`` is deprecated and has been replaced by
  invocations to ``plugin_instance.placeholder.page``.
* Removed directory ``static/cascade/css/fonts/glyphicons-halflings``, since they are available
  through the Bootstrap npm packages.
* All Javascript files accessing a property ``disabled``, now use the proper jQuery function
  intended for it.
* Added interface to upload fonts and use them as framed icons, text icons or button decorators.
* The permission system now is fine grained. Administrators can give their staff users
  add/change/delete permissions to each of the many Cascade plugins. When adding new plugins, this
  does not even require a database migration.
* Fixed: On saving a **CarouselPlugin**, the glossary of it's children, ie. **CarouselSlidePlugin**,
  is sanitized.
* Handle the high resolution of the **PicturePlugin** through ``srcset`` rather than a ``@media``
  query.
* Handle the high resolution background of the **JumbotronPlugin** through ``image-set`` rather than
  a ``@media`` query.
* Use default configurations from provides Cascade settings rathern than from the Django project.

0.11.1
======
* Added preconfigured ``FilePathField`` to prevent the creation of useless migration files.
* SegmentPlugin.get_form OrderedDict value lookups now compatible with python3.
* Fixed database migration failing on multiple database setup.

0.11.0
======
* Instead of adding a list of ``PartialFormField``s named ``glossary_fields``, we now can add these
  fields to the plugin class, as we would in a Django ``forms.Form`` or ``models.Model``, for
  instance: ``fieldname = GlossaryField(widget, label="A Label", initial=some_value)`` instead of
  ``glossary_fields = <list-or-tuple-of PartialFormField s>``. This is only important for third
  party apps inheriting from ``CascadePluginBase``.

  **Remember**: In some field names, the ``-`` (dash) has been replaced against an ``_``
  (underscore). Therefore please run ``./manage.py migrate cmsplugin_cascade`` which modifies the
  plugin's payloads.

0.10.2
======
* Fix #188: Using shared settings does not remember it's value.

0.10.1
======
* Fix #185: Undefined variables in case of uncaught exception.

0.10.0
======
* Added **BootstrapJumbotronPlugin**. This for instance can be used to place background images
  extending over the full width of a page using a parallax effect.
* *Experimental*: Utility to manage font icons, so that symbol icons can be used anywhere in any
  size.
* ``CMSPLUGIN_CASCADE['plugins_with_extra_fields']`` is a dict instead of a tuple. This allows
  the site administrator to enable extra styles globally and without adding them using the
  administration backend.
* Tuples in ``CMSPLUGIN_CASCADE['bootstrap3']['breakpoints']`` now accepts five parameters instead
  of four. The 5th parameter specifies the image width for fluid containers and the Jumbotron
  plugin.
* The plugin's change form now can add an introduction and a footnote HTML. This is useful to add
  some explanation text.

0.9.4
=====
* Added function ``.utils.validate_link`` to check if submitted link information is valid.

0.9.3
=====
* Fixed: enabled subject_location did not work properly for **ImagePlugin** and **PicturePlugin**.
* Fixed indention in admin interface for extra fields model.
* Moved template 'testing.html' -> 'cascade/testing.html'.
* Added German translations.

0.9.2
=====
* Restore global jQuery object (required by the Select2 widget) in explicit file instead of doing
  it implicitly in ``linkpluginbase.js``

0.9.1
=====
* Prepared for django-1.10
* Upgrade ring.js to version 2.1.0
* In LinkPlugin, forgive if sub-dict ``link`` was missing in ``glossary``
* Fixed HTML escaping problem in Bootstrap Carousel
* Increase height of Select2 fields

0.9.0
=====
* Compatible with django-cms version 3.3.0
* Converted ``SharableCascadeElement`` into a proxy model, sharing the same data as model
  ``CascadeElement``. This allows adding plugins to ``CMSPLUGIN_CASCADE['plugins_with_sharables']``
  without requiring a data-migration. (**Note:** A migration merges the former two models, so
  please backup your database before upgrading!)
* Add support for Section Bookmarks.
* Fixed: Do not set width/height on <img>-element inside a <picture>, if wrapping container is fluid.
* Replaced configuration settings ``CMSPLUGIN_CASCADE_LINKPLUGIN_CLASSES`` against
  ``CMSPLUGIN_CASCADE['link_plugin_classes']`` for better consistency.

**Note:** If you want to continue using django-CMS 3.2 please use djangocms-cascade 0.8.5.

0.8.5
=====
* Dropped support for Python-2.6.

0.8.4
=====
* Fixed a regression in "Restore from clipboard".
* Fixed TextLinkPlugin to work again as child of TextPlugin.
* ContainerPlugin can only be added below a placeholder.
* Prepared demo to work with Django-1.10.
* Plugins marked as "transparent" are only allowed as parents,
  if they allow children.

0.8.3
=====
* Added ``CustomSnippetPlugin``. It allows to add arbitrary custom templates to the project.
* Fixed #160: Error copying Carousel plugin
* Plugins marked as "transparent" can be parents of everybody.
* BootstrapPanelPlugin now accepts inline CSS styles.

0.8.2
=====
* Cascade does not create migrations for proxy models anymore. This created major problems if
  Cascade components have been switched on and off. All existing migrations of proxy models have
  been removed from the migration files.
* Fixed: Response of more than one entry on non unique clipboards.
* Added :class:`cmsplugin_cascade.models.SortableInlineCascadeElement` which can be used for
  keeping sorted inline elements.
* :class:`cmsplugin_cascade.bootstrap3.gallery.BootstrapGalleryPlugin` can sort its images.

0.8.1
=====
* Hotfix: removed invalid dependency in migration 0007.

0.8.0
=====
* Compatible with Django-1.9
* Fixed #133: BootstrapPanelPlugin now supports custom CSS classes.
* Fixed #132: Carousel Slide plugin with different form.
* Fixed migration problems for proxy models outside Cascade.
* Replaced SelectMultiple against CheckboxSelectMultiple in admin for extra fields.
* Removed SegmentationAdmin from admin backend.
* Disallow whitespace in CSS attributes.
* Require django-reversion 1.10.1 or newer.
* Require django-polymorphic 0.9.1 or newer.
* Require django-filer 1.1.1 or newer.
* Require django-treebeard 4.0 or newer.
* Require django-sekizai 0.9.0 or newer.


0.7.3
=====
* Use the outer width for fluid containers. This allows us to add images and carousels which extend
  the browser's edges.
* Fixed #132: Carousel Slide plugin different form.
* Fixed #133: BootstrapPanelPlugin does not support custom CSS classes.
* Fixed #134: More plugins can be children of the ``SimpleWrapperPlugin``. This allows us to be more
  flexible when building the DOM tree.
* ``BootstrapContainerPlugin`` now by default accepts extra inline styles and CSS classes.

0.7.2
=====
* Add a possibility to prefix Cascade plugins with a symbol of your choice, to avoid confusion
  if the same name has been used by another plugin.
* All Bootstrap plugins can override their templates globally though a configuration settings
  variable. Usefule to switch between jQuery and AngularJS versions of a widget.
* Added TabSet and TabPanel plugins.
* It is possible to persist the content of the clipboard in the database, retrieve and export
  it as JSON to be reimported on an unrelated site.

0.7.1
=====
* Added a **HeadingPlugin** to add single text headings independently of the HTML TextEditorPlugin.

0.7.0
=====
Cleanup release, removing a lot of legacy code. This adds some incompatibilities to previous
versions:

* Instead of half o dozen of configuration directives, now one Python dict is used. Therefore
  check your ``settings.py`` for configurations starting with ``CMSPLUGIN_CASCADE_...``.
* Tested with **Django-1.8**. Support for version 1.7 and lower has been dropped.
* Tested with **djangoCMS** version 3.2. Support for version 3.0 and lower has been dropped.
* Tested with **django-select2** version 5.2. Support for version 4 has been dropped.
* The demo project now uses SASS instead of plain CSS, but SASS is not a requirement during normal
  development.

0.6.2
=====
* In Segment: A condition raising a TemplateSyntaxError now renders that error inside a HTML
  comment. This is useful for debugging non working conditions.
* In Segment: An alternative AdminModel to UserAdmin, using a callable instead of a model field,
  now works.
* In Segment: It is possible to use ``segmentation_list_display = (list-of-fields)`` in an
  alternative AdminModel, to override the list view, when emulating a user.

0.6.1
=====
* Added a panel plugin to support the Bootstrap Panel.
* Added experimental support for secondary menus.
* Renamed ``AccordionPlugin`` to ``BootstrapAccordionPlugin`` for consistency and to avoid future
  naming conflicts.

0.6.0
=====
* Fixed #79: The column width is not reduced in width, if a smaller column precedes a column for a
  smaller displays.
* Fixed: Added extra space before left prefix in buttons.
* Enhanced: Access the link content through the glossary's ``link_content``.
* New: Plugins now can be rendered using an alternative template, choosable through the plugin
  editor.
* Fixed in SegmentationPlugin: When overriding the context, this updated context was only used for
  the immediate child of segment. Now the overridden context is applied to all children and
  grandchildren.
* Changed in SegmentationPlugin: When searching for siblings, use a list index instead of
  ``get_children().get(position=...)``.
* Added unit tests for SegmentationPlugin.
* Added support for **django-reversion**.
* By using the setting ``CMSPLUGIN_CASCADE_LINKPLUGIN_CLASSES``, one can replace the class
  ``LinkPluginBase`` by an alternative implementation.
* When using *Extra Styles* distances now can have negative values.
* In caption field of ``CarouselSlidePlugin`` it now is possible to set links onto arbitrary pages.

**Possible backwards incompatibility**:

* For consistency with naming conventions on other plugins, renamed ``cascade/plugins/link.html``
  -> ``cascade/link/link-base.html``. **Check your templates**!
* The setting ``CMSPLUGIN_CASCADE_SEGMENTATION_MIXINS`` now is a list of two-tuples, where the first
  declares the plugin's model mixin, while the second declares the model admin mixin.
* Removed from setting: ``CMSPLUGIN_CASCADE_BOOTSTRAP3_TEMPLATE_DIR``. The rendering template now
  can be specified during runtime.
* Refactored and moved ``SimpleWrapperPlugin`` and ``HorizontalRulePlugin`` from
  ``cmsplugin_cascade/bootstrap3/`` into ``cmsplugin_cascade/generic/``. The glossary field
  ``element_tag`` has been renamed to ``tag_type``.
* Refactored ``LinkPluginBase`` so that external implementations can create their own version,
  which then is used as base for TextLinkPlugin, ImagePlugin and PicturePlugin.
* Renamed: ``PanelGroupPlugin`` -> ``Accordion``, ``PanelPlugin`` -> ``AccordionPanelPlugin``,
  because the Bootstrap project renamed them back to their well known names.

0.5.0
=====
* Added SegmentationPlugin. This allows to conditionally render parts of the DOM, depending on
  the status of various ``request`` object members, such as ``user``.
* Setting ``CASCADE_LEAF_PLUGINS`` has been replaced by ``CMSPLUGIN_CASCADE_ALIEN_PLUGINS``. This simplifies
  the programming of third party plugins, since the author of a plugin now only must set the member
  ``alien_child_classes = True``.

0.4.5
=====
* Fixed: If no breakpoints are set, don't delete widths and offsets from the glossary, as otherwise
  this information is lost.
* Fixed broken import for ``PageSelectFormField`` when not using **django_select2**.
* Admin form for ``PluginExtraFields`` now is created on the fly. This fixes a rare circular
  dependency issue, when accessing ``plugin_pool.get_all_plugins()``.

0.4.4
=====
* Removed hard coded input fields for styling margins from **BootstrapButtonPlugin**, since
  it is possible to add them through the **Extra Fields** dialog box.
* [Column ordering](http://getbootstrap.com/css/#grid-column-ordering) using ``col-xx-push-n``
  and ``col-xx-pull-n`` has been added.
* Fixed: Media file ``linkplugin.js`` was missing for **BootstrapButtonPlugin**.
* Hard coded configuration option ``EXTRA_INLINE_STYLES`` can now be overridden by the projects
  settings


0.4.3
=====
* The templatetag ``bootstrap3_tags`` and the templates to build Boostrap3 styled menus,
  breadcrumbs and paginator, have been moved into their own repository
  at https://github.com/jrief/djangocms-bootstrap3.
* `Column ordering`_ using ``col-xx-push-n`` and ``col-xx-pull-n`` has been added.

.. _Column ordering: http://getbootstrap.com/css/#grid-column-ordering

0.4.2
=====
* Fixed: Allow empty setting for CMSPLUGIN_CASCADE_PLUGINS
* Fixed: Use str(..) instead of b'' in combination with from __future__ import unicode_literals

0.4.1
=====
* Fixed: Exception when saving a ContainerPlugin with only one breakpoint.
* The ``required`` flag on a field for an inherited LinkPlugin is set to False for shared settings.
* Fixed: Client side code for disabling shared settings did not work.

0.4.0
=====
* Renamed ``context`` from model ``CascadeElement`` to ``glossary`. The identifier ``context`` lead
  to too much confusion, since it is used all way long in other CMS plugins, where it has a
  complete different meaning.
* Renamed ``partial_fields`` in all plugins to ``glossary_fields``, since that's the model field
  where they keep their information.
* Huge refactoring of the code base, allowing a lot of more features.

0.3.2
=====
* Fixed: Missing unicode conversion for method ``get_identifier()``
* Fixed: Exception handler for form validation used ``getattr`` incorrectly.

0.3.1
=====
* Added compatibility layer for Python-3.3.

0.3.0
=====
* Complete rewrite. Now offers elements for Bootstrap 3 and other CSS frameworks.

0.2.0
=====
* Added carousel.

0.1.2
=====
* Fixed: Added missign migration.

0.1.1
=====
* Added unit tests.

0.1.0
=====
* First published revision.

Thanks
======

This DjangoCMS plugin originally was derived from https://github.com/divio/djangocms-style, so the
honor for the idea of this software goes to Divio and specially to Patrick Lauber, aka digi604.

However, since my use case is different, I removed all the existing code and replaced it against
something more generic suitable to add a collection of highly configurable plugins.
