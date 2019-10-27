Procedures
==========

.. note::

    TODO: make a nice object diagram for "procedures" section

.. contents:: Contents
    :local:

"procedures" section
--------------------

.. py:class:: procedures

    The ``procedures`` section of ``amorphys`` is a subclass of :py:class:`section`.
    It consists of the ``blocks`` and ``order``, both of which are required properties.

    .. py:attribute:: $description

        a recommended ``string`` property inherited from :py:class:`section`.

    .. py:attribute:: blocks

        a mapping of :py:class:`Procedure` objects.

    .. py:attribute:: order

        an array of :py:class:`Relationship` instances representing
        the restrictions in the order between the specified :py:class:`Procedure` objects.

Procedure class
---------------

.. py:class:: Procedure

    (TODO)
