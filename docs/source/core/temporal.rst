Predefined subclasses for Temporal
==================================

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

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This field must hold ``"Proedure"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: date

        an optional (but recommended) :py:class:`Date` property
        specifying the date of this procedure.

        Usually, the value for this property holds a reference to a variable, as the date
        of the procedure varies across subjects and/or sessions.

    .. py:attribute:: start-time

        an optional :py:class:`Time` property specifying the starting time of this procedure.

    .. py:attribute:: end-time

        an optional :py:class:`Time` property specifying the ending time of this procedure.

    .. py:attribute:: setup

        an optional (but recommended) :py:class:`Setup` property representing
        what setup is used for this procedure.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

Action and Block
----------------

Both :py:class:`Action` and :py:class:`Block` derive from the :py:class:`Procedure`
abstract class.

- For an atomic, unitary procedure, use :py:class:`Action`.
- For a group of procedures, use :py:class:`Block`.

.. py:class:: Action

    :py:class:`Action` is a subclass of :py:class:`Procedure`,
    and represents an elemental procedural action.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This field must hold ``"Action"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: date

        a required :py:class:`Date` property specifying the date of this action,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: start-time

        an optional :py:class:`Time` property specifying the starting time of this action,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: end-time

        an optional :py:class:`Time` property specifying the ending time of this action,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: setup

        an optional (but recommended) :py:class:`Setup` property representing
        what setup is used for this action, as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

.. py:class:: Block

    :py:class:`Block` is a subclass of :py:class:`Procedure`,
    and consists of a group of Procedures.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This field must hold ``"Block"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: date

        a required :py:class:`Date` property specifying the date of this block of procedures,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: procedures

        a required array consisting of :py:class:`Procedure` objects (can contain none),
        specifying the list of sub-procedures in this block of procedures.

    .. py:attribute:: order

        an optional array consisting of temporal :py:class:`Relationship` objects,
        specifying the order of individual sub-procedures in this block.

    .. py:attribute:: start-time

        an optional :py:class:`Time` property specifying the starting time of this block of procedures,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: end-time

        an optional :py:class:`Time` property specifying the ending time of this block of procedures,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: setup

        an optional (but recommended) :py:class:`Setup` property representing
        what setup is used for this block, as it is inherited from :py:class:`Procedure`.

        If the setup differs between individual child procedures in this block,
        the :py:attr:`setup` property may be better described there.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

Phase
-----

For an example, refer to :ref:`this section <procedures-example>`.

.. py:class:: Phase

    :py:class:`Phase` is a subclass of :py:class:`Block` (i.e. a group of procedures),
    and represents a operational phase, or an experimental session
    consisting of one experimental procedure or more..

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This field must hold ``"Phase"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: date

        a required :py:class:`Date` property specifying the date of this block of procedures,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: procedures

        a required array consisting of :py:class:`Procedure` objects (can contain none),
        specifying the list of sub-procedures in this block of procedures.
        This is a property inherited from :py:class:`Block`.

    .. py:attribute:: order

        an optional array consisting of temporal :py:class:`Relationship` objects,
        specifying the order of individual sub-procedures in this block.
        This is a property inherited from :py:class:`Block`.

    .. py:attribute:: start-time

        an optional :py:class:`Time` property specifying the starting time of this block of procedures,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: end-time

        an optional :py:class:`Time` property specifying the ending time of this block of procedures,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: setup

        an optional (but recommended) :py:class:`Setup` property representing
        what setup is used during this phase, as it is inherited from :py:class:`Procedure`.

        If the setup differs between individual child procedures in this block,
        the :py:attr:`setup` property may be better described there.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

Specific types of actions
-------------------------

Anesthesia
^^^^^^^^^^

.. admonition:: TODO

    describe what this is:

    - content: material used, probably with concentration
    - route: i.p., s.c., etc.


Acquisition
^^^^^^^^^^^

For an example, refer to :ref:`this section <procedures-example>`.

Acquisition allows to link an :py:class:`Action` entity (i.e. an atomic procedure)
with specific acquisition configurations.

.. py:class:: Acquisition

    a subclass of :py:class:`Action`.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This field must hold ``"Acquisition"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: date

        a required :py:class:`Date` property specifying the date of this action,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: sequencer

        an optional :py:class:`Sequencer` property for better describing
        what task/protocol/sequence is used during this acquisition.

    .. py:attribute:: start-time

        an optional :py:class:`Time` property specifying the starting time of this action,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: end-time

        an optional :py:class:`Time` property specifying the ending time of this action,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: setup

        an optional (but recommended) :py:class:`Setup` property representing
        what setup is used for this action, as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

ChronicPreparation
^^^^^^^^^^^^^^^^^^

Introduction or removal of some component from the subject.

.. py:class:: ChronicPreparation

    a subclass of :py:class:`Action`.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This field must hold ``"ChronicPreparation"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: date

        a required :py:class:`Date` property specifying the date of this action,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: manipulations

        a required array with manipulation-related :py:class:`Relationship`
        describing what material is introduced to / removed from the subject,
        with what parameters / coordinates.

    .. py:attribute:: start-time

        an optional :py:class:`Time` property specifying the starting time of this action,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: end-time

        an optional :py:class:`Time` property specifying the ending time of this action,
        as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: setup

        an optional (but recommended) :py:class:`Setup` property representing
        what setup is used for this action, as it is inherited from :py:class:`Procedure`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.
