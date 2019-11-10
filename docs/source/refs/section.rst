Specification of metadata sections
===================================

.. contents:: Contents
    :local:

Each section in the ``amorphys`` metadata file(s) must have a certain specific format.

section
--------

.. py:class:: section

    Each section of ``amorphys`` has different properties of its own.
    But it can have an optional property, :py:attr:`_description` to describe itself.

    .. py:attribute:: _description

        a human-readable ``string`` description of the section.
        It is recommended to include this property for every section,
        for increased understandability.
