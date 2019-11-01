Predefined subclasses for Signal
================================

Representative classes of the :py:class:`Signal` class are described below.

.. contents:: Contents
    :local:

Sampled and its subclasses
--------------------------

Sampled
^^^^^^^

.. py:class:: Sampled

    for signal that is continuously sampled.
    An example of :py:class:`Sampled` may be found :ref:`here <signal-example>`.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This property must hold ``"Sampled"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: role

        a required ``string`` property referring to what role it plays in the context
        of this physiology experiment, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: quality

        a required ``string`` property describing the physical quality that
        this signal is supposed to reflect, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: range

        a required ``object`` property to describe what algebraic values
        this signal must hold, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: sampling-rate

        a required :py:class:`Quantity` property to specify the sampling rate
        of this signal.

    .. py:attribute:: generated-by

        a required property indicating what spatial existence generates/emits this signal,
        as it is inherited from :py:class:`Signal`.

    .. py:attribute:: monitored-by

        a required property indicating what spatial existence monitors/reads this signal,
        as it is inherited from :py:class:`Signal`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

There are several pre-defined subclasses.
Although most physiology experiments (except for brain-imaging studies) can
be described using the ones below, it is going to be possible at some point
to define your own subclasses, too.

Scan
^^^^

:py:class:`Scan` is a subclass that represents loops of scans.

This class is the base class for "scanning"-type sampling methods as a whole.
There are more common, usage-dependent sub-classes such as :py:class:`LineScan`,
:py:class:`Video`, and :py:class:`Volume`, so it is recommended to use them
if your use case falls into one of them.

.. py:class:: Scan

    represents any type of scanning method.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This property must hold ``"Scan"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: role

        a required ``string`` property referring to what role it plays in the context
        of this physiology experiment, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: quality

        a required ``string`` property describing the physical quality that
        this signal is supposed to reflect, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: range

        a required ``object`` property to describe what algebraic values
        this signal must hold, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: sampling-rate

        a required (pixel-)sampling rate of this signal, as it is inherited
        from :py:class:`Sampled`.

    .. py:attribute:: size

        a required :py:class:`Space` property representing the number of pixels/voxels
        for each single scan.

        For a :py:class:`Scan` entity, this property probably holds a single-dimensional
        :py:class:`Space` instance.

        .. caution::

        	The current specification assumes that the number of pixels or voxels does not change dynamically during acquisition. If it changes from run to run, or during individual runs, consider holding this value as a variable.

    .. py:attribute:: generated-by

        a required property indicating what spatial existence generates/emits this signal,
        as it is inherited from :py:class:`Signal`.

    .. py:attribute:: monitored-by

        a required property indicating what spatial existence monitors/reads this signal,
        as it is inherited from :py:class:`Signal`.

    .. py:attribute:: scan-rate

        an optional (but recommended) :py:class:`Quantity` property representing
        the number of scans (i.e. sampling for :py:attr:`size` times) being run
        per unit time.

        In most cases, the number is the inverse of the time taken to obtain :py:attr:`size`
        number of samples, but it may be exactly the same quantity as :py:attr:`sampling-rate`
        if e.g. sampling occurs simultaneously from multiple electrodes.

        The unit is normally based on ``Hz``.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

Predefined subclasses of Scan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the following subclasses, the defined properties are exactly the same
as what :py:class:`Scan` has, but a certain meaning is added in terms of ontology.

.. py:class:: LineScan

    a subclass of :py:class:`Scan` used to represent a line scan-based sampling.
    For properties, refer to :py:class:`Scan`.

.. py:class:: MEA

    a subclass of :py:class:`Scan` used to represent a multi-electrode array.
    For properties, refer to :py:class:`Scan`.

    Note that, in this case, :py:attr:`sampling-rate` must be the same as
    :py:attr:`scan-rate`.

    .. caution::

    	This class may be too specific to be pre-defined,
        and may subject to future deprecation.

.. py:class:: Video

    a subclass of :py:class:`Scan` used to represent video acquisition.
    For properties, refer to :py:class:`Scan`.

    The :py:attr:`size <Scan.size>` property must hold a :py:class:`Space` with more than
    two-dimensional. For example, the standard color videography will have
    three dimensions (i.e. width, height, and 3 color channels).

    Note that, in the case of "standard" videography, :py:attr:`sampling-rate <Scan.sampling-rate>`
    can be the same as :py:attr:`scan-rate <Scan.scan-rate>`, as it makes no sense to define
    the pixel-sampling rate (or pixel dwell-time, as it may be important for
    scanning microscopy).

.. py:class:: Volume

    a subclass of :py:class:`Scan` used to represent 3-D volume acquisition.
    For properties, refer to :py:class:`Scan`.

    The :py:attr:`size` property must hold a :py:class:`Space` with more than
    three-demensional.

Event and its subclasses
------------------------

Event
^^^^^

.. py:class:: Event

    for signal that "occurs" discretely from time to time.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This property must hold ``"Event"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: role

        a required ``string`` property referring to what role it plays in the context
        of this physiology experiment, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: quality

        a required ``string`` property describing the physical quality that
        this event type is supposed to reflect, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: generated-by

        a required property indicating what spatial existence generates/emits this event type,
        as it is inherited from :py:class:`Signal`.

    .. py:attribute:: monitored-by

        a required property indicating what spatial existence monitors/reads this event type,
        as it is inherited from :py:class:`Signal`.

    .. py:attribute:: values

        a required ``object`` property to describe what algebraic values
        this event type must hold, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

    .. admonition:: TODO

        add an example, and describe subclasses

        Image: image acquisition: needs size

State
-----

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
        of this physiology experiment, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: quality

        a required ``string`` property describing the physical quality that
        this state type is supposed to reflect, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: generated-by

        a required property indicating what spatial existence generates/emits this state type,
        as it is inherited from :py:class:`Signal`.

    .. py:attribute:: monitored-by

        a required property indicating what spatial existence monitors/reads this state type,
        as it is inherited from :py:class:`Signal`.

    .. py:attribute:: values

        a required ``object`` property to describe what algebraic values
        this state type must hold, as it is inherited from :py:class:`Signal`.

    .. py:attribute:: properties

        an optional property that holds schematic descriptions of additional properties.
        The semantics follows that of JSON Schema.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

    .. admonition:: TODO

        add an example
