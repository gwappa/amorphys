Procedures
==========

.. note::

    TODO: make a nice object diagram for "procedures" section

"procedures" section
--------------------

.. py:class:: procedures

    The ``procedures`` section of ``amorphys`` consists of the ``blocks`` and ``order`` subsections.
    It is also *recommended* to contain the ``description`` field as well in the ``procedures`` section.

    .. py:attribute:: blocks

        a mapping of :py:class:`Procedure` objects.

    .. py:attribute:: order

        an array of :py:class:`Relationship` instances representing
        the restrictions in the order between the specified :py:class:`Procedure` objects.

    .. py:attribute:: description

        a ``string`` describing that this is the ``procedures`` section of this project.

Procedure
---------

.. py:class:: Procedure

    (TODO)
