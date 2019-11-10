Specification of metadata sections
===================================

.. contents:: Contents
    :local:

Each section in the ``amorphys`` metadata file(s) must have a certain specific format.

section
--------

.. py:class:: section

    Each section of ``amorphys`` has different properties of its own.
    But it can have an optional property, :py:attr:`description` to describe itself.

    .. py:attribute:: description

        a human-readable ``string`` description of the section.
        It is recommended to include this property for every section,
        for increased understandability.

project
--------

.. py:class:: project

    The ``project`` section of ``amorphys`` is a subclass of :py:class:`section`,
    and describes the organization of the project group.

    A typical :py:class:`project` would look like below:

    .. literalinclude:: /_static/sections/project.json
        :language: javascript
        :caption: in: "project.json"

    It consists of several fields:

    .. py:attribute:: description

        a recommended field that is equivalent to that in :py:class:`section`.

    .. py:attribute:: dataset

        a :py:class:`dataset` object representing the metadata for this dataset itself.

    .. py:attribute:: people

        a mapping to :py:class:`contributor` instances representing the people involved in
        this project.

    .. py:attribute:: affiliations

        a mapping to :py:class:`institution` instances representing the affiliations
        of the people involved.

    .. py:attribute:: funded_by

        a mapping to :py:class:`funding` instances representing the funding sources
        for this project.

    .. py:attribute:: data_published_by

        an array of references to an item or more in :py:attr:`people`, representing
        the people contributed to publish this dataset.
