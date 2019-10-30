List of subclasses for Quality
==============================

Representative classes of the :py:class:`Quality` class are described below.

.. contents:: Contents
    :local:

Signal entity
-------------

.. py:class:: Signal

    for quality that is continuously sampled

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This property must hold ``"Signal"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: role

        a required ``string`` property referring to what role it plays in the context
        of this physiology experiment, as it is inherited from :py:class:`Quality`.

    .. py:attribute:: dimension

        a required ``string`` property describing the physical dimension that
        this signal is supposed to reflect, as it is inherited from :py:class:`Quality`.

    .. py:attribute:: generated-by

        a required property indicating what spatial existence generates/emits this signal,
        as it is inherited from :py:class:`Quality`.

    .. py:attribute:: monitored-by

        a required property indicating what spatial existence monitors/reads this signal,
        as it is inherited from :py:class:`Quality`.

    .. py:attribute:: values

        a required ``object`` property to describe what algebraic values
        this signal must hold, as it is inherited from :py:class:`Quality`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

    .. note::

        TODO: add an example, and describe subclasses

        - Line:   line scan: needs line rate and line length
        - Video:  video acquisition: needs frame rate and size
        - Volume: volume acquisition: needs volume rate and size
        - Scan:   any other types of scanning method. needs loop rate.

Event entity
------------

.. py:class:: Event

    for quality that "occurs" discretely from time to time.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This property must hold ``"Event"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: role

        a required ``string`` property referring to what role it plays in the context
        of this physiology experiment, as it is inherited from :py:class:`Quality`.

    .. py:attribute:: dimension

        a required ``string`` property describing the physical dimension that
        this event type is supposed to reflect, as it is inherited from :py:class:`Quality`.

    .. py:attribute:: generated-by

        a required property indicating what spatial existence generates/emits this event type,
        as it is inherited from :py:class:`Quality`.

    .. py:attribute:: monitored-by

        a required property indicating what spatial existence monitors/reads this event type,
        as it is inherited from :py:class:`Quality`.

    .. py:attribute:: values

        a required ``object`` property to describe what algebraic values
        this event type must hold, as it is inherited from :py:class:`Quality`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

    .. note::

        TODO: add an example, and describe subclasses

        Image: image acquisition: needs size

State entity
------------

.. py:class:: State

    an abstract, discrete and instantaneous representation of a context,
    such as a state of a machine or a subject.

    Note that, this property can hold some additional experiment-wise properties
    via the :py:attr:`properties` property.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This property must hold ``"State"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: role

        a required ``string`` property referring to what role it plays in the context
        of this physiology experiment, as it is inherited from :py:class:`Quality`.

    .. py:attribute:: dimension

        a required ``string`` property describing the physical dimension that
        this state type is supposed to reflect, as it is inherited from :py:class:`Quality`.

    .. py:attribute:: generated-by

        a required property indicating what spatial existence generates/emits this state type,
        as it is inherited from :py:class:`Quality`.

    .. py:attribute:: monitored-by

        a required property indicating what spatial existence monitors/reads this state type,
        as it is inherited from :py:class:`Quality`.

    .. py:attribute:: values

        a required ``object`` property to describe what algebraic values
        this state type must hold, as it is inherited from :py:class:`Quality`.

    .. py:attribute:: properties

        an optional property that holds schematic descriptions of additional properties.
        The semantics follows that of JSON Schema.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

    .. note::

        TODO: add an example
