Entities, Relationships and Contexts
====================================

The three key concepts in ``amorphys`` are:

1. **Entity**: represents a physical existence.
2. **Relationship**: represents a relationship between two Entity instances.
3. **Context**: represents a group of Entities and Relationships.

Entity
------

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

Relationship
------------

.. py:class:: Relationship

    The ``Relationship`` is a class for JSON objects, and represents relationships between
    two or more ``Entity`` instances.

    For example, one can specify a certain contextual-spatial relationship as follows:

    .. code-block:: JavaScript

        {
            "object": { "$ref": "components/LED" },
            "in-front-of": { "$ref": "components/subject" },
            "during": { "$ref": "procedures.json#blocks/training" }
        }

    Note that the keys ``in-front-of`` and ``during`` are ontologically defined
    elsewhere as spatial or contextual relationships.

    **At most one relationship is allowed** for each of spatial, temporal or contextual keys.

    See :ref:`pre-defined relationship keys <relationship-keys>` for what is already defined.

    .. py:attribute:: object

        a JSON reference to an instance defined elsewhere.

Context
-------

.. py:class:: Context

    The ``Context`` is a subclass of :py:class:`Entity`:
    it consists of (at least) the :py:attr:`type`, :py:attr:`description`,
    and optional :py:attr:`reference` properties.

    Actually, ``Context`` does not have a unique property on its own,
    but it works as a marker that tells the processor that this consists of
    a group of :py:class:`Entity` and :py:class:`Relationship` objects.

    Additional required/optional properties may be defined in subclasses of
    ``Context``.

.. _relationship-keys:

Pre-defined relationship keys
-----------------------------

Each of the following pre-defined relationship keys work to restrict the relationship
between the two object being specified.

Spatial specifications
^^^^^^^^^^^^^^^^^^^^^^

(TODO)

Temporal specifications
^^^^^^^^^^^^^^^^^^^^^^^

(TODO)

Cross-modal specifications
^^^^^^^^^^^^^^^^^^^^^^^^^^

(TODO)

Defining your own relationship key(s)
-------------------------------------

(TODO)

.. toctree::
   :maxdepth: 2
   :caption: Table of contents:
