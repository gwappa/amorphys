URI-based reference
===================

The classes below are used to refer to unique objects on the web based on their URIs.

The classes are supplied to fulfill our needs for the time being,
but it may be substituted later if there exists any structure general enough to be used.

Referrable
----------

.. py:class:: Referrable

    the base class being used to refer to anything "referrable" on the web.
    Both :py:attr:`name` and :py:attr:`uri` properties are required.

    .. py:attribute:: name

        a human-readable ``string`` description of this object.

    .. py:attribute:: uri

        a ``string`` representing the URI-based ID of this object.
        Can be ``null`` (but not recommended), if this ``Referrable`` does not have any ID
        (although it may sound paradoxical).



Individual
----------

.. py:class:: Individual

    a subclass of :py:class:`Referrable` being used to identify any individuals
    (people, institutions, companies etc.).

    - :py:attr:`name` field would reflect what would appear as the "full-name" on the web pages.
    - :py:attr:`uri` field may be:

        - for an institution/company: the URL for its website (starting with ``https://``)
        - for a person: the ORCID (starting with ``ORCID:``)

        Can be ``null`` (but not recommended), if this individual does not have any ID.

License
-------

.. py:class:: License

    a class being used to represent a license type of the subject being described.

    For example, a CC0-license may be represented using :py:class:`License` as follows:

    .. code-block:: JavaScript

        {
            "name":    "CC0",
            "uri":     "http://creativecommons.org/publicdomain/zero/1.0",
            "year":    "2019",
            "authors": { "$ref": "/organization/people" }
        }

    - :py:attr:`name` represents the shorthand of the license e.g. "CC0", "MIT", "GPL2".
    - :py:attr:`uri` field may be the terms and conditions representing this license.

    In addition to the properties defined in :py:class:`Referrable`,
    a ``License`` object must have properties below:

    .. py:attribute:: authors

        a set of JSON objects, or a reference to it, representing the
        holder(s) of this license.

    .. py:attribute:: year

        a ``string`` representing the year (or a range of years) when
        this license is valid from.

Citation
--------

.. py:class:: Citation

    a subclass of :py:class:`Referrable` being used to refer to a unique article on the web.

    For example, a citation may be described using :py:class:`Citation` as follows:

    .. code-block:: JavaScript

        {
            "reference-type": "is-supplement-to",
            "name": "Sehara K, Colomb J, Larkum ME (2019) Dendritic mechanisms underlying foraging behavior of human subjects.",
            "uri": "doi:10.1101/000000"
        }

    - :py:attr:`name` is used to represent the human-readable citation
    - :py:attr:`uri` represents the URI of the article, and may start either
      with ``https://`` or with ``doi:``, depending on the type of the article.

    In addition to the properties defined in :py:class:`Referrable`,
    ``Citation`` has one required property.

    .. py:attribute:: reference-type

        a ``string`` representing how this citation works.
        valid types may be found below:

        ================ ======================================================================
        type             description
        ================ ======================================================================
        is-supplement-to used when the subject being described is a supplement to the citation.
        ================ ======================================================================
