Class for scientific values
===========================

..contents:: Contents
    :local:

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
        It is recommended to use one of widely accepted and used units,
        such as those `recommended by International Astronomical Union <https://www.iau.org/publications/proceedings_rules/units/>`_.
