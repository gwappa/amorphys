Project organization
====================

.. note::

    TODO: make a nice object diagram for "organization" section

.. contents:: Contents
    :local:

"organization" section
----------------------

A typical :py:class:`organization` would look like below:

.. code-block:: JavaScript
    :caption: in: "organization.json"

    {
        "$schema":      "https://.../amorphys.json#properties/organization"
        "$description": "the project organization for foraging experiment",

        "dataset": {
            "name": "HumanForagingBehavior_PostdocRoom",
            ...
        },

        "people": {
            "Keisuke": {
                "name": "Keisuke S.K. Sehara",
                ...
            },
            "Julien": {
                "name": "Julien Colomb",
                ...
            },
            ...
        },

        "affiliations": {
            "ChaosSoftware": {
                "name": "Chaos Software",
                ...
            },
            ...
        },

        "funded-by": {
            "DFG": {
                "name": "Deutliche Forschungsgesellschaft",
                ...
            },
            ...
        },

        "data-published-by": [
            { "$ref": "../people/Keisuke" },
            { "$ref": "../people/Julien" }
        ]
    }

.. py:class:: organization

    The ``organization`` section of ``amorphys`` is a subclass of :py:class:`section`,
    and describes the organization of the project group.
    It consists of several fields:

    .. py:attribute:: $description

        a recommended field that is equivalent to that in :py:class:`section`.

    .. py:attribute:: dataset

        a :py:class:`Dataset` object representing the metadata for this dataset itself.

    .. py:attribute:: people

        a mapping to :py:class:`Contributor` instances representing the people involved in
        this project.

    .. py:attribute:: affiliations

        a mapping to :py:class:`Institution` instances representing the affiliations
        of the people involved.

    .. py:attribute:: funded-by

        a mapping to :py:class:`Funding` instances representing the funding sources
        for this project.

    .. py:attribute:: data-published-by

        an array of references to an item or more in :py:attr:`people`, representing
        the people contributed to publish this dataset.

Dataset class
-------------

The instantiation of the :py:class:`Dataset` would look something like below:

.. code-block:: JavaScript

    {
        "name":        "HumanForagingBehavior_PostdocRoom",
        "description": "Tracking data of human subjects performing a foraging task inside a post-doc room",
        "keywords":    ["foraging behavior", "human", "scientists"],
        "license":     {
            "name":    "CC0",
            "uri":     "http://creativecommons.org/publicdomain/zero/1.0",
            "year":    "2019",
            "authors": { "$ref": "/organization/people" }
        },
        "references": [
            {
                "reference-type": "is-supplement-to",
                "name": "Sehara K, Colomb J, Larkum ME (2019) Dendritic mechanisms underlying foraging behavior of human subjects.",
                "uri": "doi:10.1101/000000"
            }
        ]
    }

.. py:class:: Dataset

    a class to represent the metadata for this project dataset as a whole,
    including a license information based on a :py:class:`License` object.

    .. py:attribute:: name

        a ``string`` representing the identifiable name of this dataset as a whole.

    .. py:attribute:: description

        a ``string`` representing the description of this dataset as a whole.

    .. py:attribute:: keywords

        an array of ``string`` objects representing the free keywords for this dataset.

    .. py:attribute:: license

        a :py:class:`License` object corresponding to the license clause of this dataset publication.

    .. py:attribute:: references

        an array of :py:class:`Citation` objects referring to the articles related to this dataset.

Contributor class
-----------------

The ``Contributor`` class represents the contributor to this project.

It normally looke like below:

.. code-block:: JavaScript

    {
        "name":       "Keisuke S.K. Sehara",
        "lastname":   "Sehara",
        "firstnames": "Keisuke S.K.",
        "uri":        "ORCID:0000-0000-0000-0000",
        "contact":    "kkkkkeeeeiiiissssuuuukkkkeeee@mail.chaos-software.cc",
        "affiliation": [
            { "$ref": "organization/affiliations/ChaosSoftware" },
            { "$ref": "organization/affiliations/NerdUniversityTokyo" }
        ]
        "roles": [
            "https://dictionary.casrai.org/Contributor_Roles/Data_curation",
            "https://dictionary.casrai.org/Contributor_Roles/Software"
        ]
    },

.. py:class:: Contributor

    It is a subclass of :py:class:`Person`.

    All the superclass properties are necessary:

    - :py:attr:`name <Person.name>`
    - :py:attr:`uri <Person.uri>`
    - :py:attr:`lastname <Person.lastname>`
    - :py:attr:`firstnames <Person.firstnames>`
    - :py:attr:`contact <Person.contact>`

    In addition, all of the properties described below are necessary.

    .. py:attribute:: affiliation

        an :py:class:`Institution` object, or a reference to one, or an array
        of multiple of them, corresponding to the affiliations for this contributor,
        *in relation with this dataset publication*.

    .. py:attribute:: roles

        an array of roles, specified in terms of the `contributor roles <https://dictionary.casrai.org/Contributor_Roles>`_
        (as it is defined in the `CRediT taxonomy <https://www.casrai.org/credit.html>`_).


Institution class
-----------------

The :py:class:`Institution` class is used to represent the affiliated institution(s).

Typically, it would look like below:

.. code-block:: JavaScript

    {
        "name": "Chaos Software",
        "uri":  "https://www.chaos-software.cc"
    }

.. py:class:: Institution

    This is a subclass of the :py:class:`Individual` class, with no additional properties.

    .. py:attribute:: name

        a required property inherited from :py:attr:`Individual.name`.
        It represents the human-readable expression of this institution.

    .. py:attribute:: uri

        a required property inherited from :py:attr:`Individual.uri`.
        It represents the URL (i.e. starting with ``https://``) of the institution.

Funding class
-------------

.. py:class:: Funding

    (TODO)
