Predefined subclasses for Spatial
=================================

Representative classes of the :py:class:`Spatial` class are described below.

.. contents:: Contents
    :local:

Subject entity
--------------

.. py:class:: Subject

    a subclass of :py:class:`Spatial` representing the subject of the study.
    Depending on whether it is a human being or not, it becomes
    either an :py:class:`Animal` or a :py:class:`Participant`.

    If it is a tissue cut out from an individual, then it becomes
    a :py:class:`Tissue`.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: age

        a required :py:class:`Age` property indicating the age of this :py:class:`Subject`.

    .. py:attribute:: license

        a required property representing a license term or more that is
        related to this subject e.g. the license for the animal experiment,
        or the informed consent conditions with the human experiment.

    .. py:attribute:: composition

        an optional property holding a :py:class:`Spatial` or an array of them,
        as it is inherited from :py:class:`Spatial`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

Subclasses of Subject
^^^^^^^^^^^^^^^^^^^^^

.. py:class:: Animal

    a subclass of :py:class:`Subject` representing a non-human individual.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: species-strain

        a required :py:class:`Strain` property indicating the species and strain
        of this :py:class:`Animal`.

    .. py:attribute:: age

        a required :py:class:`Age` property, as it is inherited from :py:class:`Subject`.

    .. py:attribute:: sex

        a required :py:class:`Sex` property of this :py:class:`Animal`.

    .. py:attribute:: death

        a required :py:class:`Death` property, indicating when and how this
        :py:class:`Animal` died.

    .. py:attribute:: license

        a required license-term property, inherited from :py:class:`Subject`.

    .. py:attribute:: composition

        an optional property holding a :py:class:`Spatial` or an array of them,
        as it is inherited from :py:class:`Spatial`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

    .. admonition:: TODO

        is it better having a property indicating "experiment-specific"?

.. py:class::  Participant

    a subclass of :py:class:`Subject` representing a human individual.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: age

        a required :py:class:`Age` property, as it is inherited from :py:class:`Subject`.

    .. py:attribute:: sexuality

        a required :py:class:`Sexuality` property of this :py:class:`Participant`.

    .. py:attribute:: license

        a required license-term property, inherited from :py:class:`Subject`.

    .. py:attribute:: composition

        an optional property holding a :py:class:`Spatial` or an array of them,
        as it is inherited from :py:class:`Spatial`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

    .. admonition:: TODO

        add property details??

.. py:class:: Tissue

    a subclass of :py:class:`Subject` representing a tissue or an organ
    that is cut out from an individual.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: origin

        a required property referring to the :py:class:`Animal` or the :py:class:`Participant`
        where this :py:class:`Tissue` instance originates from.

    .. py:attribute:: age

        a required :py:class:`Age` property, as it is inherited from :py:class:`Subject`.

    .. py:attribute:: license

        the required license-term property, inherited from :py:class:`Subject`.

    .. py:attribute:: composition

        an optional property holding a :py:class:`Spatial` or an array of them,
        as it is inherited from :py:class:`Spatial`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

    .. admonition:: TODO

        add property details

Component entity
----------------

.. py:class:: Component

    a subclass of :py:class:`Spatial` representing any chemical / physical
    component used for the study.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: supplier

        an optional (but recommended) property referring to an :py:class:`Individual`
        who supplied this :py:class:`Material` instance.

    .. py:attribute:: composition

        an optional property holding a :py:class:`Spatial` or an array of them,
        as it is inherited from :py:class:`Spatial`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

Material and its related classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:class:: Material

    a subclass of :py:class:`Component` representing any chemical / physical
    material used for the study.

    Being a :py:class:`Material` typically implies that it *does not have a
    specific form*. Normally, an experimenter uses a :py:class:`Material`
    as a :py:class:`Substance` or makes a :py:class:`Part` out of it.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: supplier

        an optional (but recommended) property inherited from :py:class:`Component`.

    .. py:attribute:: composition

        an optional property holding a :py:class:`Spatial` or an array of them,
        as it is inherited from :py:class:`Spatial`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

.. py:class:: Substance

    a subclass of :py:class:`Material` representing a (typically chemical)
    substance used for the study e.g. drug or some biochemical solutions.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: supplier

        an optional (but recommended) property inherited from :py:class:`Component`.

    .. py:attribute:: composition

        an optional property holding a :py:class:`Spatial` or an array of them,
        as it is inherited from :py:class:`Spatial`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

.. py:class:: Part

    a subclass of :py:class:`Spatial` representing an artificial building block
    for the experiment.

    Being a :py:class:`Part` implies that it has a certain specific *static shape*,
    and has some specific *static roles or functions* for the experiment to work properly.

    Typically, each :py:class:`Part` is made of one single :py:class:`Material` or two.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: made-of

        a required property referring to a :py:class:`Material`
        that this :py:class:`Part` is made of.

    .. py:attribute:: supplier

        an optional (but recommended) property inherited from :py:class:`Component`.

    .. py:attribute:: composition

        an optional property holding a :py:class:`Spatial` or an array of them,
        as it is inherited from :py:class:`Spatial`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

Apparatus and its related classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. py:class:: Apparatus

    a subclass of :py:class:`Component` representing an apparatus.

    Being an apparatus may imply that many parts are configured in some specific ways
    to execute *a specific role or a function*.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: model

        a required ``string`` property representing the model name of this apparatus.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: supplier

        an optional (but recommended) property inherited from :py:class:`Component`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.

    .. py:attribute:: composition

        an optional property holding a :py:class:`Spatial` or an array of them,
        as it is inherited from :py:class:`Spatial`.

    .. admonition:: TODO

        how to add any configurational parameter(s) for an Apparatus?

.. py:class:: Device

    a subclass of :py:class:`Apparatus` representing a device.

    Being a :py:class:`Device` implies that it reads or writes a :py:class:`Signal`,
    and/or executes a :py:class:`Program` in it.

    .. py:attribute:: type

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: model

        a required ``string`` property representing the model name of this apparatus.

    .. py:attribute:: description

        a required ``string`` property inherited as an :py:class:`Entity` instance.

    .. py:attribute:: supplier

        an optional (but recommended) property inherited from :py:class:`Component`.

    .. py:attribute:: generates

        an optional property consisting of a reference, or a list of references,
        to a :py:class:`Signal` instance or more.

    .. py:attribute:: monitors

        an optional property consisting of a reference, or a list of references,
        to a :py:class:`Signal` instance or more.

    .. py:attribute:: runs

        an optional property consisting of a reference, or a list of references,
        to a :py:class:`Program` instance or more.

    .. py:attribute:: composition

        an optional property holding a :py:class:`Spatial` or an array of them,
        as it is inherited from :py:class:`Spatial`.

    .. py:attribute:: reference

        an optional ``string`` or ``[ string ]`` property inherited as an
        :py:class:`Entity` instance.
