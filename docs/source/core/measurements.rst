Classes for measurements
========================

The following classes are used to represent values related to measurements.

.. contents:: Contents
    :local:

Date
----

.. py:class:: Date

    :py:class:`Date` is used for representation of dates.
    This is for extending the conventional ``date`` object of JSON.

    for example, you can represent the date in several different formats:

    .. code-block:: JavaScript
        :caption: The following objects represent the same date

        {
            "format": "%Y-%m-%d",
            "value":  "2019-01-22"
        },

        {
            "format": "%d/%m/%y",
            "value":  "22/01/19"
        }

    .. py:attribute:: format

        a required ``string`` property used for how to parse the :py:attr:`value` field.

        In principle, the field names follow the specifications in the UNIX command ``date``.
        The following fields are allowed for the moment:

        ====== =====================
        Field  Description
        ====== =====================
        ``%Y`` a 4-digit year field
        ``%y`` a 2-digit year field
        ``%m`` a 2-digit month field
        ``%d`` a 2-digit date field
        ====== =====================

        Other than the fields above, the following special characters can be used:

        - ``-`` (hyphen)
        - ``,`` (comma)
        - ``.`` (period)
        - ``/`` (slash)
        - `` `` (space)

        .. caution::

        	A warning may be raised if the format does _not_ contain all of year/month/day fields.

    .. py:attribute:: value

        the date value, in the format specified in :py:attr:`format`.
        If the value does not conform to :py:attr:`format`, an error will be generated.

Time
----

.. py:class:: Time

    :py:class:`Time` is used for representation of dates.
    This is for extending the conventional ``time`` object of JSON.

    for example, you can represent the date in several different formats:

    .. code-block:: JavaScript
        :caption: Examples of Time instances

        {
            "format": "%H-%M-%S",
            "value":  "09-25-22"
        },

        {
            "format": "%H:%M",
            "value":  "09:25"
        }

    .. py:attribute:: format

        a required ``string`` property used for how to parse the :py:attr:`value` field.

        In principle, the field names follow the specifications in the UNIX command ``date``.
        The following fields are allowed for the moment:

        ====== ========================================================
        Field  Description
        ====== ========================================================
        ``%H`` a 2-digit 24-hour field
        ``%M`` a 2-digit minute field
        ``%S`` a 2-digit second field
        ``%f`` a field representing subsecond time (up to microseconds)
        ====== ========================================================

        Other than the fields above, the following special characters can be used:

        - ``:`` (colon)
        - ``-`` (hyphen)
        - ``,`` (comma)
        - ``.`` (period)
        - ``/`` (slash)
        - `` `` (space)

        In case the finer scales are not specified (e.g. having only ``%H`` and ``%M``,
        and not the others), having zeros for them is assumed.
        For example, if you format ``"09:50"`` with the formatter ``"%H:%M"``,
        you can expect to represent either ``"09:50:00"`` or ``"09:50:00.000000"``,
        depending on the runtime.

        .. caution::

        	You cannot format a value only consisting of e.g. ``%H`` and ``%S``, and skipping ``%M``.

    .. py:attribute:: value

        the date value, in the format specified in :py:attr:`format`.
        If the value does not conform to :py:attr:`format`, an error will be generated.

Subject-related
---------------

Age
^^^

.. admonition:: TODO

    specify how to represent age of an animal, a participant, or a tissue.


Sex
^^^

.. admonition:: TODO

    specify how to represent the sex (M/F/others?) of an animal or a participant.

Death
^^^^^

.. admonition:: TODO

    specify:

    - date of death
    - cause of death
    - method of sacrifice

Space
-----

.. py:class:: Space

    :py:class:`Space` represents an N-dimensional space with
    an optional unit.

    Typically, this class is used for description of a scan strategy
    (e.g. line scan, imaging etc.), or the shape of an electrode.

    The :py:attr:`scale` property may optionally be set to describe a
    conversion from the (probably unit-less) value represented here
    to a certain "well-known" unit (e.g. to represent mm/px).

    .. py:attribute:: shape

        a required array consisting of ``integer`` elements.
        The size of the array represents the dimension of this region,
        and each element represents the length of each edge of this region.

    .. py:attribute:: description

        an optional array consisting of ``string`` elements.
        This field is supposed to hold human-readable representations of
        what each dimension of :py:attr:`shape` stands for
        (e.g. "size", "width", "pole", "shank").

    .. py:attribute:: unit

        an optional ``string`` property to represent the unit for this size.
        If not set, a default unit (such as ``pixel`` or ``voxel``) will be assumed.
        Please read :ref:`notes-on-units`.

    .. py:attribute:: scale

        an optional :py:class:`Quantity` property to represent the conversion scale
        between the size described here (as the numerator) and a more commonly used unit
        (as the demoninator).

        For the "commonly-used" unit, please refer to :ref:`notes-on-units`.

Quantity
--------

:py:class:`Quantity` is used to represent values with units.

For example, the following entry is used to describe "30.0 Hz":

.. code-block:: JavaScript

    {
        "type":      "number",
        "value":     "29.99999999999",
        "precision": 3,
        "unit":      "Hz"
    }

.. py:class:: Quantity

    .. py:attribute:: type

        a required ``string`` property specifying the type of the value.
        Normally, ``"number"`` (floating-point number) comes here.

    .. py:attribute:: value

        a required ``string`` property representing the value of this quantity.
        Note that it is not numeric itself, e.g. in ``number``.
        This field must hold a string representation of the value,
        and it is formatted later to the type specified by the :py:attr:`type` property.

    .. py:attribute:: precision

        an optional ``integer`` property specifying
        the number of decimal places that are scientifically valid.
        This field is taken into account probably only when the :py:attr:`type`
        property is ``"number"`` or ``"float"``;
        if :py:attr:`type` is ``"integer"`` or ``"string"``, this field is
        ignored even when set.

    .. py:attribute:: unit

        an optional ``string`` property indicating the unit of this quantity.
        Please read :ref:`notes-on-units`.

.. _notes-on-units:

Notes on unit usages
--------------------

.. caution::
    Although it is up to the users to use any arbitrary units in the ``"unit"`` field,
    it is recommended to use one of widely accepted and commonly used units.

    As an example, refer to `this guide by International Astronomical Union (IAU) <https://www.iau.org/publications/proceedings_rules/units/>`_.
