Entity
======

.. contents:: Contents
    :local:

Entity class
------------

.. py:class:: Entity

    The ``Entity`` is a class for JSON objects representing physical existences.
    It has two required properties, ``type`` and ``description``.

    .. py:attribute:: type

        a ``string`` object representing the type of this Entity instance.
        normally, here comes the name of the subclass that this entity belongs to.

    .. py:attribute:: description

        a ``string`` description of this Entity instance.

    In addition to the above required properties, an Entity instance can have
    the following optional property:

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property that contains the URL(s)
        related to this Entity instance. It can start with, for example,
        ``https://`` (in case the reference is a web page), or with ``doi:``
        (in case it is described elsewhere with a DOI).

Types of entities
-----------------

Depending on what dimension(s) it lives in, entities are categorized differently.

Note that, a class of an entity may be implied from the ontology of the
:py:attr:`type <Entity.type>` property.

Spatial entity
^^^^^^^^^^^^^^

The :py:class:`Spatial` class is a subclass of :py:class:`Entity`, and is used
for entities that require some physical space.

You can check representative subclasses of :py:class:`Spatial`: see :doc:`spatial` for details.

.. py:class:: Spatial

    the root class of all the spatial existence classes.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

The nature of each :py:class:`Spatial` entity is represented ontologically.

Temporal entity
^^^^^^^^^^^^^^^

The :py:class:`Temporal` is a subclass of :py:class:`Entity`, and is
used to represent a certain temporal event or phase.

You can check representative subclasses of :py:class:`Temporal`: see :doc:`temporal` for details.

.. py:class:: Temporal

    the root class of all the temporal existence classes.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This field must hold ``"Temporal"`` or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

The nature of each :py:class:`Temporal` entity is represented ontologically.

Qualitative entity
^^^^^^^^^^^^^^^^^^

The :py:class:`Quality` is a subclass of :py:class:`Entity`, and is used
to represent a certain quality that goes between spatial entities.

An example entry for a :py:class:`Quality` entity looks like below:

.. _quality-example:

.. code-block:: JavaScript
    :caption: in: "acquisition.json"

    {
        "type":         "Signal",
        "role":         "behavior",
        "dimension":    "calcium",
        "values":       { "type": "number" },
        "generated-by": { "$ref": "setups.json#postdoc-room/components/probe" },
        "monitored-by": { "$ref": "setups.json#postdoc-room/components/photodiode" },
        "description":  "the calcium signal taken from the surface probe of the participant."
    }

You can check representative subclasses of :py:class:`Quality`: see :doc:`quality` for details.

.. py:class:: Quality

    the root class of all the classes related to qualitative existence.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: role

        a required ``string`` property referring to what role it plays in the context
        of this physiology experiment.

        Must be one of: ``"command"``, ``"behavior"``, ``"configuration"``.

    .. py:attribute:: dimension

        a required ``string`` property describing the physical dimension that
        this signal is supposed to reflect.

        The exact vocabulary shall be ontologically defined elsewhere, but possibly
        includes: ``"position"``, ``"voltage"``, ``"weight"``, ``"calcium"``.

    .. py:attribute:: generated-by

        a required property that holds a :py:class:`Spatial` entity, or a reference to it.
        If there are multiple entities, a list of :py:class:`Spatial` entities may be used.
        This property indicates what spatial existence generates/emits this quality.

    .. py:attribute:: monitored-by

        a required property that holds a :py:class:`Spatial` entity, or a reference to it.
        If there are multiple entities, a list of :py:class:`Spatial` entities may be used.
        This property indicates what spatial existence monitors/reads this quality.

    .. py:attribute:: values

        a required ``object`` property to describe what algebraic values
        this :py:class:`Quality` must hold.

        For representing numeric definitions, you can use a JSON Schema-related
        representation such as ``{ "type": "number", "minimum": 0.0 }``.

        If this :py:class:`Quality` holds an enumerative values,
        you can give a mapping here e.g.

        .. code-block:: JavaScript

            {
                "high": {
                    "description": "TTL-high"
                },
                "low": {
                    "description": "TTL-low"
                }
            }

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

The quality underlying each :py:class:`Quality` entity is represented ontologically.

Programs and Routines
^^^^^^^^^^^^^^^^^^^^^

A :py:class:`Routine` class is capable of reading/holding/writing :py:class:`Quality`,
and of storing data in a certain format.

A :py:class:`Program` controls one :py:class:`Routine` or more, and
it normally resides in a certain :py:class:`Spatial` entity
(e.g. a PC or a microcontroller) that in turn reads or writes :py:class:`Quality` entities.

The format of data files is described using a :py:class:`DataFile` instance.

An example :py:class:`Program` entity would look like below:

.. _program-example:

.. code-block:: JavaScript
    :caption: in: "acquisition.json"

    {
        "type":        "manual-operation",
        "description": "a post-hoc manual operation of behavioral states",

        "runs-on":  { "$ref": "setups.json#postdoc-room/components/PC" },
        "supplier": { "$ref": "organization.json#people/Keisuke" },
        "routines": {
            "annotation": {
                "reads": { "$ref": "../channels/video" },
                "generates": { "$ref": "../channels/behavioral-states" },
                "stores": {
                    "anno": {
                        "data": { "$ref": "../channels/behavioral-states" },
                        "extension": ".csv",
                        "format": "text/csv"
                    }
                }
            }
        }
    }

.. py:class:: Program

    The :py:class:`Program` is a subclass of :py:class:`Entity`, and is used
    to represent an algorithm for signal I/O and data storage.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.
        This property must hold ``"Program"``, or the name of one of its subclasses.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance,
        describing the function of this program in the experiment.

    .. py:attribute:: runs-on

        a required property that holds a :py:class:`Spatial` entity.
        This represents the "hardware" part of the program.

        For this :py:class:`Program` to process a certain :py:class:`Quality`,
        this :py:class:`Quality` must be monitored / read by the :py:class:`Spatial`
        entity that runs the :py:class:`Program`.

    .. py:attribute:: routines

        a required mapping from names to their corresponding :py:class:`Routine` entities.

    .. py:attribute:: supplier

        an optional property that holds an :py:class:`Individual` entity, or a reference to it.

        This property describes the "software" (algorithm) part of the program.
        Normally, this is the individual who developed the program. In cases
        where the program represents a sort of "manual" operations (e.g.
        manual annotation of behavioral states), the person who did the job
        will appear here.

        If there are multiple suppliers, it can hold a list of them.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

.. py:class:: Routine

    The :py:class:`Routine` is *not* a subclass of :py:class:`Entity`.
    In fact, this class is rather like a small companion class for the sake of
    easier description of a :py:class:`Program` entity.

    Normally a :py:class:`Routine` instance is defined inside a :py:class:`Program`
    instance, and is never referred to from outside of it.

    .. py:attribute:: reads

        a required property that holds a reference to a :py:class:`Quality` instance
        this routine uses.

    .. py:attribute:: generates

        a required property that holds a reference to a :py:class:`Quality` instance
        this routine generates.

    .. py:attribute:: stores

        an optional mapping that maps the identifiers of the data files
        to the corresponding :py:class:`DataFile` specifications that this routine generates.


.. py:class:: DataFile

    another companion class for :py:class:`Program` and :py:class:`Routine`
    being used to describe a data file.

    .. py:attribute:: data

        a required property that holds a :py:class:`Quality` to be saved in this data file.
        If there are multiple of them, this property can hold all of them as a list.

    .. py:attribute:: extension

        a required ``string`` property that holds the extension of the data file.

    .. py:attribute:: format

        a required ``string`` representation of the format of the content of this data file.
        It is recommended that this property follows what is specified in
        `Multipurpose Internet Mail Extension (MIME) types <https://www.iana.org/assignments/media-types/media-types.xhtml>`_,
        but in cases where the format is binary and not specified there, you can use
        ``application/<your application name>`` instead.
