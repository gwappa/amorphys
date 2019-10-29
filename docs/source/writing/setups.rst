Setups
======

.. note::

    TODO: make a nice object diagram for "setups" section

.. contents:: Contents
    :local:

"setups" section
----------------

A typical :py:class:`setups` section would look like below:

.. code-block:: JavaScript
    :caption: in: "setups.json"

    {
        "$description": "experimental setups for the foraging-behavior project",

        "postdoc-room": {
            "type": "Setup",
            "description": "the setup for investigation of human foraging behavior.",

            "components": {
                "subject": { "$ref": "variables.json#participants/subject" },
                "KeisukesDesk": {
                    ...
                },
                "fridge": {
                    ...
                },
                ...
            },

            "layout": [
                {
                    "about":       { "$ref": "../components/fridge" },
                    "predicate":   "left-side-of",
                    "relative-to": { "$ref": "../components/KeisukesDesk" }
                },
                ...
            ]
        }
    }

(refer to ``variables`` for what ``participants/subject`` refers to)

.. py:class:: setups

    The ``setups`` section of ``amorphys`` is a subclass of :py:class:`section`,
    and consists of a mapping of :py:class:`Setup` objects.

    Multiple :py:class:`Setup` objects may be included inside this section,
    and each of them can be referred to from elsewhere by its key
    (i.e. ``"setups/postdoc-room"`` in the above example).

    .. py:attribute:: $description

        a recommended ``string`` field inherited from the :py:class:`section` class.

Setup class
-----------

.. py:class:: Setup

    ``Setup`` is a subclass of :py:class:`Context`.
    A ``Setup`` object consists of the following parts, in addition to
    the standard properties defined in :py:class:`Context`:

    .. py:attribute:: type

        a required ``string`` object inherited from :py:class:`Entity`.
        Unless you define any subclasses, this property must be ``"Setup"``.

    .. py:attribute:: description

        a required ``string`` description inherited from :py:class:`Entity`.

    .. py:attribute:: components

        a mapping to physical objects (subjects and apparatuses) that comprise the setup.
        The value part can be either a :py:class:`Spatial` instance, or a JSON reference to it.

        Note that **only** :py:class:`Spatial` **objects** can become the value part of this mapping.

    .. py:attribute:: layout

        an array of spatial relationships between those defined in the ``components`` section.

        Each :py:class:`Relationship` instance must have one and only one spatial restriction in it,
        but can optionally have the other types of relationship keys.

    .. py:attribute:: reference

        an optional set of URIs, in ``string`` or ``[ string ]``, inherited from :py:class:`Entity`.

.. toctree::
   :maxdepth: 2
   :caption: Table of contents:
