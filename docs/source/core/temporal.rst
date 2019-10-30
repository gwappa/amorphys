List of subclasses for Temporal
===============================

Representative classes of the :py:class:`Temporal` class are described below.
An example can be found :ref:`here <procedures-example>`.

.. contents:: Contents
    :local:

Procedure
---------

:py:class:`Procedure` is an abstract class representing an experimental procedure.

- For an atomic, unitary procedure, use :py:class:`Action`.
- For a group of procedures, use :py:class:`Block`.

.. py:class:: Procedure

    :py:class:`Procedure` is a subclass of :py:class:`Temporal`,
    and represents any type of experimental procedure.

    .. note::

    	TODO:

        - type: required
        - date: required (but nullable), date format (inherits from parent)
        - start-time, stop-time: optional, time format
        - description: required

Action and Block
----------------

Both :py:class:`Action` and :py:class:`Block` derive from the :py:class:`Procedure`
abstract class.

- For an atomic, unitary procedure, use :py:class:`Action`.
- For a group of procedures, use :py:class:`Block`.

.. py:class:: Action

    :py:class:`Action` is a subclass of :py:class:`Procedure`,
    and represents an elemental procedural action.

    .. note::

        TODO: inherits attributes from :py:class:`Procedure`:

.. py:class:: Block

    :py:class:`Block` is a subclass of :py:class:`Procedure`,
    and consists of a group of Procedures.

    .. note::

        TODO: in addition to that of :py:class:`Procedure`:

        - items
        - order
        - procedures:  array of Procedures, required
        - order:       array of relationships between elemental procedures, required

Phase
-----

For an example, refer to :ref:`this section <procedures-example>`.

.. py:class:: Phase

    :py:class:`Phase` is a subclass of :py:class:`Block` (i.e. a group of procedures),
    and represents a operational phase, or an experimental session
    consisting of one experimental procedure or more.

    .. note::

    	TODO: attributes are inherited
        warning occurs if "date" is null

Acquisition
-----------

For an example, refer to :ref:`this section <procedures-example>`.

Acquisition allows to link an :py:class:`Action` entity (i.e. an atomic procedure)
with specific acquisition/setup configurations.

.. py:class:: Acquisition

    a subclass of :py:class:`Action`.

    .. note::

    	TODO: in addition to attributes in :py:class:`Action`:

        - setup: reference to a :py:class:`Setup` entity
        - task:  reference to a :py:class:`Task` entity
