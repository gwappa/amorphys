Relationship
============

The :py:class:`Relationship` is a class for JSON objects, and represents contextual relationships
between two or more :py:class:`Entity` instances.

The notations in :py:class:`Relationship` is used to set up a `semantic triple <https://en.wikipedia.org/wiki/Semantic_triple>`_
(in fact, in terms of notation, it is probably closer to `N-quads notation <https://www.w3.org/TR/n-quads/>`_)

For example, one can specify a certain contextual-spatial relationship as follows:

.. code-block:: JavaScript

    {
        "about":       { "$ref": "setups/the-rig/components/LED" },
        "predicate":   "in-front-of",
        "relative-to": { "$ref": "setups/the-rig/components/animal" }
        "restriction": {
                "predicate":   "during",
                "relative-to": { "$ref": "procedures.json#blocks/training" }
        }
    }

In the example above, a semantic triple, being nested within another, is specified:

.. code-block:: turtle

    [ <setups/the-rig/components/LED> <in-front-of> <setups/the-rig/components/animal> ]
        <during> <procedures/blocks/training> .

Or, using a notation close to N-quads, it can be written as:

.. code-block:: turtle

    <setups/the-rig/components/LED> <in-front-of> <setups/the-rig/components/animal>
        <procedures/blocks/training> .

:py:attr:`about` is used to specify the subject of the semantic triple,
whereas :py:attr:`predicate` and :py:attr:`relative-to` represent
the predicate and the object (in terms of the graph vocabulary).

the :py:class:`Restriction` object used for the :py:attr:`restriction` key
sets up the graph context where the triple is valid.

Note that the keys ``in-front-of`` and ``during`` are ontologically defined
elsewhere as spatial or contextual relationships.
See :ref:`pre-defined relationship keys <relationship-keys>` for what is already defined.

.. py:class:: Restriction

    a base class for :py:class:`Relationship`.
    This class is a partial implementation of a semantic triple;
    it only represents the predicate and the object part of a semantic triple,
    without specification of the subject part.

    Aside from being the "headless" superclass of :py:class:`Relationship`,
    it is also used to represent a :py:attr:`restriction` where a :py:class:`Relationship` is valid.

    .. py:attribute:: predicate

        a ``string`` object representing the predicate part of the corresponding semantic triple.
        See :ref:`pre-defined relationship keys <relationship-keys>` for what is already defined.

    .. py:attribute:: relative-to

        a JSON reference to an instance defined elsewhere, representing the
        object part of the semantic triple.

.. py:class:: Relationship

    a ``Relationship`` object is used to describe a full semantic triple,
    with the use of :py:attr:`about` representing its subject part.

    In addition to :py:attr:`predicate` and :py:attr:`relative-to`,
    ``Relationship`` must have the following attribute:

    .. py:attribute:: about

        a JSON reference to an instance defined elsewhere, representing the
        subject part of the semantic triple.
        It corresponds to the ``about`` XML attribute in the ``http://www.w3.org/1999/02/22-rdf-syntax-ns#`` namespace
        (cf. `RDF 1.1 XML syntax <https://www.w3.org/TR/rdf-syntax-grammar/>`_).

    Further, a ``Relationship`` object can have the following optional attribute:

    .. py:attribute:: restriction

        a :py:class:`Restriction` object that sets up the context where
        this ``Relationship`` object is valid.

        For the time being, only one :py:class:`Restriction` object is allowed
        (i.e., use of an array is not allowed) here.

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
