Variables and expressions
=========================

Some experimental conditions (strain, virus species etc.) may vary across
individual subjects, individual sessions, runs or sweeps.

To easily express some context-dependence within experiments, you can use
variables and expressions in place of concrete objects.

.. _variable-example:

Use of variables
^^^^^^^^^^^^^^^^

A variable is a placeholder for an object that is defined on-site during an experiment.

For example, the following object describes a variable that can take either ``pairing``
or ``testing`` as its value.

.. code-block:: JavaScript

    {
        "$variable": {
            "type":  { "enum": "pairing", "testing" }
        }
    }

Another example below describes an array of values taking any number above zero:

.. code-block:: JavaScript

    {
        "$variable": {
            "type":  "array",
            "items": {
                "type":    "number",
                "minimum": 0
            }
        }
    }

.. py:class:: variable

    A :py:class:`variable` object can be identified by the existence of
    the :py:attr:`$variable` property.

    For an example, refer to :ref:`variable-example`.

    .. py:attribute:: $variable

        holds a valid schema based on `JSON Schema <https://json-schema.org/>`_,
        but it may typically be a schema for a ``string`` or a ``number``.

.. _condition-example:

Use of conditions
^^^^^^^^^^^^^^^^^

Conditions provide a way to switch the object depending on the value of a certain variable,
just like the ``switch`` statement in C, C++ and related languages.

.. code-block:: JavaScript

    {
        "$condition": { "$ref": "/variable/task-mode" },
        "switch": [
            {
                "case":  "pairing",
                "value": 2
            },
            {
                "case":  "testing",
                "value": 1
            }
        ],
        "default": 0
    }

In the above example, depending on the ``string`` variable being held at ``/variable/task-mode``,
the expression evaluates to a different value.

It evaluates to ``2`` if the task mode is ``pairing``, ``1`` if the mode is ``testing``,
and ``0`` otherwise.

.. py:class:: condition

    the existence of the :py:class:`$condition` property indicates that this is
    a :py:class:`condition` object.

    For an example, refer to :ref:`condition-example`.

    .. py:attribute:: $condition

        holds a reference to the variable.

    .. py:attribute:: switch

        a required array of :py:class:`case-expression` objects.

    .. py:attribute:: default

        an optional property holding the "default" value, when nothing in
        :py:class:`switch` applies.

    .. caution::

    	Make sure that you covered all the possible cases in :py:attr:`switch`, or that you set the :py:attr:`default`. Otherwise the expression is evaluated to ``null``, and may cause an undefined behavior.

.. _formatter-examples:

Expressions and formatters
^^^^^^^^^^^^^^^^^^^^^^^^^^

Expressions and formatters provide a simple way of calculations based on
variables.

Below is an example of a formatter:

.. code-block:: JavaScript

    {
        "$expression": "{{ x }}\*2 + 3",
        "where": {
            "x": { "$ref": "/variables/x" }
        }
    }

In the example above, if ``x`` evaluates to the number ``1``, for example,
the whole formatter is evaluated to ``5``.

Another example provides another way of expressing a condition:

.. code-block:: JavaScript

    {
        "$expression": "{{ x }} == {{ y }}",
        "where": {
            "x": { "$ref": "/variable1" },
            "y": { "$ref": "/variable2" }
        }
    }

In this case, the whole formatter is evaluated to either ``true`` or ``false``,
depending on whether the two referenced variables are equal or not.

In practice, you can define the expression elsewhere as a string, and plug
the values where you need:

.. code-block:: JavaScript

    {
        "expressions": {
            "output-calculation": "{{ start }} + {{ step }} * {{ index }}",
            ...
        },

        ...

        "pulse": {
            "amplitude": {
                "$expression": { "$ref": "/expressions/output-calculation" },
                "where": {
                    "start": 0,
                    "step":  10,
                    "index": 2
                }
            }
        }
    }

.. py:class:: formatter

    The existence of the :py:attr:`$expression` property indicates that this is
    a :py:class:`formatter` object.

    For examples, see :ref:`formatter-examples`.

    .. py:attribute:: $expression

        the expression to be evaluated.
        Each appearance of variable names must be wrapped inside doubled curly braces.

    .. py:attribute:: where

        the assignment specifications for the expression.
        The variables used within :py:attr:`$expression` must appear once
        in this section.

Use of templates
^^^^^^^^^^^^^^^^

.. admonition:: TODO

    - ``$template`` keyword

        - object representation instead of expression
        - ``$ref``-based reference

    - ``where`` property

        - used to plug values at the root scope of the template
