Context
=======

Context class
-------------

.. py:class:: Context

    The ``Context`` is a subclass of :py:class:`Entity`:
    it consists of (at least) the :py:attr:`type`, :py:attr:`description`,
    and optional :py:attr:`reference` properties.

    Actually, ``Context`` does not have a unique property on its own,
    but it works as a marker that tells the processor that this consists of
    a group of :py:class:`Entity` and :py:class:`Relationship` objects.

    Additional required/optional properties may be defined in subclasses of
    ``Context``.

    .. py:attribute:: type

        a required ``string`` object inherited from :py:class:`Entity`.

    .. py:attribute:: description

        a required ``string`` description inherited from :py:class:`Entity`.

    .. py:attribute:: reference
    
        an optional set of URIs, in ``string`` or ``[ string ]``, inherited from :py:class:`Entity`.

.. toctree::
   :maxdepth: 2
   :caption: Table of contents:
