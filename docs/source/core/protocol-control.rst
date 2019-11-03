Description of protocol control
================================

Here, it is described as to how to abstract your stimulus-response sequence (i.e. protocol)
during acquisition.

Currently, it does not belong anywhere in the tree of entities
for the sake of simplicity in notation.

.. contents:: Contents
    :local:

Overview
--------

You can choose a suitable class from the two options:

- :py:class:`Sequencer`: describe as a sequence of :py:class:`StimulusBlock` objects.
- :py:class:`StateMachine`: describe in terms of transitions of :py:class:`MachineState`.

    - input can be :py:class:`Event`, including the "timeout" event.

Typically, if the next state of the protocol depends on some on-line contexts (e.g.
responses from the subject), then the use of :py:class:`StateMachine` would be appropriate.

Variable parameters, such as stimulus strengths and durations, may be
represented in terms of :py:class:`variable`.

Sequence-type stimulus description
----------------------------------

Sequencer
^^^^^^^^^^

.. py:class:: Sequencer

    :py:class:`Sequencer` consists of blocks of :py:class:`StimulusBlock`,
    and it is probably useful when the acquisition involves a fixed protocol
    of stimulus trains (possibly with variable parameters) while recording the
    responses from the subject.

    .. py:attribute:: type

        a required ``string`` property. It must hold the value ``"sequencer"``.

    .. py:attribute:: description

        a required ``string`` property, for a human-readable description of
        what this :py:class:`Sequencer` class is for.

    .. py:attribute:: sequence

        a required array of :py:class:`StimulusBlock` describing the stimulus sequence.

StimulusBlock
^^^^^^^^^^^^^

.. admonition:: TODO

    define and describe how to write


Context-dependent stimulus sequence
-----------------------------------

StateMachine
^^^^^^^^^^^^

.. py:class:: StateMachine

    This class is used when the output stimulus sequence depends on input signals
    e.g. the state of behavior of the subject.

    .. py:attribute:: type

        a required ``string`` property. It must hold the value ``"state-machine"``.

    .. py:attribute:: description

        a required ``string`` property, for a human-readable description of
        what this :py:class:`StateMachine` class is for.

    .. py:attribute:: initial

        the initial, entry :py:class:`State` for this state machine when it is reset.
        Normally, this property holds a reference to one of the states in :py:attr:`states`.

    .. py:attribute:: states

        a required mapping from the names to their corresponding :py:class:`MachineState` instances.

MachineState
^^^^^^^^^^^^

.. py:class:: MachineState

    The :py:class:`MachineState` class represents the state for a :py:class:`StateMachine`.

    .. py:attribute:: description

        a required ``string`` property, for a human-readable description of
        what this :py:class:`MachineState` class stands for.

    .. py:attribute:: transitions

        a required array of :py:class:`MachineStateTransition` objects,
        each describing a mapping between an incoming event and its corresponding
        state transition during this state.

    .. py:attribute:: timeout

        an optional temporal :py:class:`Quality`, describing when the timeout
        occurs for this state.

    .. py:attribute:: on-start

        an optional array of :py:class:`StimulusState` objects, describing
        what stimulus is turned on/off upon start of this state.

    .. py:attribute:: on-end

        an optional array of :py:class:`StimulusState` objects, describing
        what stimulus is turned on/off upon end of this state.

MachineStateTransition
^^^^^^^^^^^^^^^^^^^^^^

.. admonition:: TODO

    describe how to write

StimulusState
^^^^^^^^^^^^^

.. admonition:: TODO

    define and describe how to write
