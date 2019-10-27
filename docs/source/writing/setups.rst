Setups
======

.. note::

    TODO: make a nice object diagram for "setups" section

"setups" section
----------------

.. py:class:: setups

    The ``setups`` section of ``amorphys`` consists of a mapping of ``Setup`` objects.
    It is also *recommended* to contain the ``description`` field as well in the ``setups`` section.

    .. py:attribute:: description

        a recommended ``string`` field describing that this is the ``setups`` section of this project.

Setup
-----

.. py:class:: Setup

    ``Setup`` is a subclass of :py:class:`Context`.
    A ``Setup`` object consists of the following parts, in addition to
    the standard properties defined in :py:class:`Context`:

    .. py:attribute:: components

        a mapping to physical objects (subjects and apparatuses) that comprise the setup.
        The value part can be either a :py:class:`Spatial` instance, or a JSON reference to it.

        Note that **only** :py:class:`Spatial` **objects** can become the value part of this mapping.

    .. py:attribute:: layout

        an array of spatial relationships between those defined in the ``components`` section.

        Each :py:class:`Relationship` instance must have one and only one spatial restriction in it,
        but can optionally have the other types of relationship keys.

.. toctree::
   :maxdepth: 2
   :caption: Table of contents:
