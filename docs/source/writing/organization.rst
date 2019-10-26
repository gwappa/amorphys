Project organization
====================

"organization" section
----------------------

.. py:class:: organization

    The ``organization`` section of ``amorphys`` describes the organization of the
    project group, and consists of several fields:

    .. py:attribute:: description

        a recommended ``string`` field describing that this is the ``organization`` section of this project.

    .. py:attribute:: dataset

        a :py:class:`Dataset` object representing the metadata for this dataset itself.

    .. py:attribute:: people

        a mapping to :py:class:`Person` instances representing the people involved in
        this project.

    .. py:attribute:: affiliations

        a mapping to :py:class:`Affiliation` instances representing the affiliations
        of the people involved.

    .. py:attribute:: funded-by

        a mapping to :py:class:`Funding` instances representing the funding sources
        for this project.

    .. py:attribute:: data-published-by

        an array of references to an item or more in :py:attr:`people`, representing
        the people contributed to publish this dataset.

Dataset
-------

.. py:class:: Dataset

    (TODO)

Person
------

.. py:class:: Person

    (TODO)

Affiliation
-----------

.. py:class:: Affiliation

    (TODO)

Funding
-------

.. py:class:: Funding

    (TODO)
