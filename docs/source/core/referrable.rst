URI-based reference
===================

The classes below are used to refer to unique objects on the web based on their URIs.

The classes are supplied to fulfill our needs for the time being,
but it may be substituted later if there exists any structure general enough to be used.

.. code-block::

    [Referrable] <-- [Individual] <-- [Person] <-- [organization:Contributor]
                                  <-- [organization:Institution]
                 <-- [License]
                 <-- [Citation]

.. note::

    TODO: make a nice class diagram

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

Any individuals (people, institutions, companies etc.) being referred to through the URI,
are represented by the :py:class:`Individual` class.

For reference to a person, in particular, the :py:class:`Person` class is used.

.. py:class:: Individual

    a subclass of :py:class:`Referrable` being used to identify any individuals
    (people, institutions, companies etc.).

    .. py:attribute:: name

        a required property inherited from :py:attr:`Referrable.name`.
        It would typically reflect what would appear as the "full-name" on the web pages.

    .. py:attribute:: uri

        a required property inherited from :py:attr:`Referrable.uri`.

        - for an institution/company: the URL for its website (starting with ``https://``)
        - for a person: the ORCID (starting with ``ORCID:``)

        Can be ``null`` (but not recommended), if this individual does not have any ID.

.. py:class:: Person

    a subclass of :py:class:`Individual` being used to refer to a person.
    All of the properties described below are necessary.

    .. py:attribute:: name

        inherited from :py:attr:`Individual.name`.
        The full name as it would appear on the web pages.

    .. py:attribute:: uri

        inherited from :py:attr:`Individual.uri`.
        The ORCID (a ``string`` starting with ``ORCID:``) of this person.

    .. py:attribute:: lastname

        a ``string`` representing the last name of this person.
        This is used to identify the person across the database, especially
        if the :py:attr:`uri` property is set to be ``null``.

    .. py:attribute:: firstnames

        a ``string`` representing the first names (i.e. other than the last name) of this person.
        This is used to identify the person across the database, especially
        if the :py:attr:`uri` property is set to be ``null``.

    .. py:attribute:: contact

        a ``string`` representing the contact information of this person.

        It is recommended to contain the e-mail address of the person here,
        but it can be the mailing address, too.

        This field can well be ``null`` if this person does not have, or is not
        willing to share, a contact.

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

    a ``License`` object must have properties below:

    .. py:attribute:: name

        equivalent to :py:attr:`Referrable.name`.
        It represents the shorthand of the license e.g. "CC0", "MIT", "GPL2".

    .. py:attribute:: uri

        equivalent to :py:attr:`Referrable.uri`.
        It may be the terms and conditions representing this license.

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

    The following properties are required:

    .. py:attribute:: name

        equivalent to :py:attr:`Referrable.name`, and is
        used to represent the human-readable citation.

    .. py:attribute:: uri

        equivalent to :py:attr:`Referrable.uri`.
        It represents the URI of the article, and may start either
        with ``https://`` or with ``doi:``, depending on the type of the article.

    .. py:attribute:: reference-type

        a ``string`` representing how this citation works.
        valid types may be found below:

        ================ ======================================================================
        type             description
        ================ ======================================================================
        is-supplement-to used when the subject being described is a supplement to the citation.
        ================ ======================================================================
