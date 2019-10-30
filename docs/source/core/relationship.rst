Relationship
============

.. contents:: Contents
    :local:

The :py:class:`Relationship` is a class for JSON objects, and represents contextual relationships
between two or more :py:class:`Entity` instances.

The notations in :py:class:`Relationship` is based on the `JSON-LD <https://json-ld.org/>`_ semantics,
and is used to set up a `semantic triple <https://en.wikipedia.org/wiki/Semantic_triple>`_.

For example, one can specify a certain contextual-spatial relationship as follows:

How Relationship works
----------------------

.. code-block:: JavaScript

    {
        "@context":    "https://.../amorphys-spatial.jsonld",
        "@id":         { "$ref": "setups/the-rig/components/LED" },
        "in-front-of": { "$ref": "setups/the-rig/components/animal" }
    }

In the example above, a semantic triple is specified:

.. code-block:: turtle

    <setups/the-rig/components/LED> <in-front-of> <setups/the-rig/components/animal> .

:py:attr:`@id` is used to specify the subject of the semantic triple.
``in-front-of`` here is one of the properties defined in the ontology ``https://.../amorphys-spatial.jsonld``,
which in turn is specified as the value for the ``@context`` property.

Note that the keys ``in-front-of`` and ``during`` are ontologically defined
elsewhere as spatial or contextual relationships.
See :ref:`pre-defined relationship keys <relationship-keys>` for what is already defined.

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
