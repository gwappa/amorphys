Procedures
==========

.. note::

    TODO: make a nice object diagram for "procedures" section

.. contents:: Contents
    :local:

.. _procedures-example:

"procedures" section
--------------------

A typical "procedures" section looks like the one below:

.. code-block:: JavaScript

    (TODO)

.. py:class:: procedures

    The ``procedures`` section of ``amorphys`` is a subclass of :py:class:`section`.
    It consists of the ``blocks`` and ``order``, both of which are required properties.

    .. py:attribute:: $description

        a recommended ``string`` property inherited from :py:class:`section`.

    .. py:attribute:: phases

        a mapping from the phase names to :py:class:`Phase` objects, or arrays of
        :py:class:`Phase` objects.

        If you perform the phase only once for each subject, the value must be
        a :py:class:`Phase` entity; if you perform it repetitively on different days
        or periods, the value must be an array of :py:class:`Phase` entity.

    .. py:attribute:: order

        an array of :py:class:`Relationship` instances representing
        the restrictions in the order between the specified :py:class:`Phase` objects.
