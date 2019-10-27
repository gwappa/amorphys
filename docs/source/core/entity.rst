Entity
======

Entity class
------------

.. py:class:: Entity

    The ``Entity`` is a class for JSON objects representing physical existences.
    It has two required properties, ``type`` and ``description``.

    .. py:attribute:: type

        a ``string`` object representing the type of this Entity instance.

    .. py:attribute:: description

        a ``string`` description of this Entity instance.

    In addition to the above required properties, an Entity instance can have
    the following optional property:

    .. py:attribute:: reference

        a ``string`` or ``[ string ]`` that contains the URL(s) related to this Entity instance.


.. toctree::
   :maxdepth: 2
   :caption: Table of contents:
