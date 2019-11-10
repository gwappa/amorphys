"Referrable" objects
=====================

.. contents:: Contents
    :local:

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

referrable
-----------

.. py:class:: referrable

    the base class being used to refer to anything "referrable" on the web.
    Both :py:attr:`name` and :py:attr:`uri` properties are required.

    .. py:attribute:: name

        a human-readable ``string`` name of this object.

    .. py:attribute:: uri

        a ``string`` representing the URI-based ID of this object.
        Can be ``null`` (but not recommended), if this ``Referrable`` does not have any ID
        (although it may sound paradoxical).



individual
-----------

Any individuals (people, institutions, companies etc.) being referred to through the URI,
are represented by the :py:class:`individual` class.

For reference to a person, in particular, the :py:class:`person` class is used.

.. py:class:: individual

    a subclass of :py:class:`referrable` being used to identify any individuals
    (people, institutions, companies etc.).

    .. py:attribute:: name

        a required property inherited from :py:attr:`referrable.name`.
        It would typically reflect what would appear as the "full-name" on the web pages.

    .. py:attribute:: uri

        a required property inherited from :py:attr:`referrable.uri`.

        - for an institution/company: the URL for its website (starting with ``https://``)
        - for a person: the ORCID (starting with ``ORCID:``)

        Can be ``null`` (but not recommended), if this individual does not have any ID.


institution class
-----------------

.. py:class:: institution

    This is a subclass of the :py:class:`individual` class, with no additional properties.
    This class is used to e.g. represent the affiliated institution(s) of a :py:class:`contributor`.

    .. literalinclude:: /_static/referrable/institution.json
        :language: JavaScript
        :caption:  Typical "institution" object

    .. py:attribute:: name

        a required property inherited from :py:attr:`individual.name`.
        It represents the human-readable expression of this institution.

    .. py:attribute:: uri

        a required property inherited from :py:attr:`individual.uri`.
        It represents the URL (i.e. starting with ``https://``) of the institution.

person
-------

.. py:class:: person

    a subclass of :py:class:`individual` being used to refer to a person.

    .. literalinclude:: /_static/referrable/person.json
        :language: JavaScript
        :caption:  Typical "person" object

    All of the properties described below are necessary.

    .. py:attribute:: name

        inherited from :py:attr:`individual.name`.
        The full name as it would appear on the web pages.

    .. py:attribute:: uri

        inherited from :py:attr:`individual.uri`.
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

contributor
------------

.. py:class:: contributor

    It is a subclass of :py:class:`person`, and represents the contributor to a project.

    .. literalinclude:: /_static/referrable/contributor.json
        :language: JavaScript
        :caption:  Typical "contributor" object

    All the superclass properties are necessary:

    - :py:attr:`name <person.name>`
    - :py:attr:`uri <person.uri>`
    - :py:attr:`lastname <person.lastname>`
    - :py:attr:`firstnames <person.firstnames>`
    - :py:attr:`contact <person.contact>`

    In addition, all of the properties described below are necessary.

    .. py:attribute:: affiliation

        an :py:class:`institution` object, or a reference to one, or an array
        of multiple of them, corresponding to the affiliations for this contributor,
        *in relation with this dataset publication*.

    .. py:attribute:: roles

        an array of :py:class:`roles <credit>` of this contributor, specified in terms of the
        `contributor roles <https://dictionary.casrai.org/Contributor_Roles>`_
        (as it is defined in the `CRediT taxonomy <https://www.casrai.org/credit.html>`_).


license
--------

.. py:class:: license

    a class being used to represent a license type of the subject being described.

    For example, a CC0-license may be represented using :py:class:`license` as follows:

    .. literalinclude:: /_static/referrable/license.json
        :language: JavaScript
        :caption:  Typical "license" object

    a ``license`` object must have properties below:

    .. py:attribute:: name

        equivalent to :py:attr:`referrable.name`.
        It represents the shorthand of the license e.g. "CC0", "MIT", "GPL2".

    .. py:attribute:: uri

        equivalent to :py:attr:`referrable.uri`.
        It may be the terms and conditions representing this license.

    .. py:attribute:: authors

        a set of JSON objects, or a reference to it, representing the
        holder(s) of this license.

    .. py:attribute:: year

        a ``string`` representing the year (or a range of years) when
        this license is valid from.

citation
---------

.. py:class:: citation

    a subclass of :py:class:`referrable` being used to refer to a unique article on the web.

    For example, a citation may be described using :py:class:`citation` as follows:

    .. literalinclude:: /_static/referrable/citation.json
        :language: JavaScript
        :caption:  Typical "citation" object

    The following properties are required:

    .. py:attribute:: name

        equivalent to :py:attr:`referrable.name`, and is
        used to represent the human-readable citation.

    .. py:attribute:: uri

        equivalent to :py:attr:`referrable.uri`.
        It represents the URI of the article, and may start either
        with ``https://`` or with ``doi:``, depending on the type of the article.

    .. py:attribute:: reference_type

        a ``string`` representing how this citation works.
        valid types may be found below:

        ================ =======================================================================
        type             description
        ================ =======================================================================
        is-supplement-to this citation is based on the dataset being described.
        is-described-by  this citation describes how the dataset being described was generated.
        is-referenced-by this citation refers to this dataset, but neither of the above applies.
        ================ =======================================================================
