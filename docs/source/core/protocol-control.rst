Description of protocol control
================================

Here, it is described as to how to abstract your stimulus-response sequence (i.e. protocol)
during acquisition.

In case of behavioral tasks, in particular, the description of protocol-control is paired
with the description of :doc:`behavioral-model` in the :doc:`tasks <../writing/tasks>` section.

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

Unitary stimulus control
------------------------

StimulusState
^^^^^^^^^^^^^

.. py:class:: StimulusState

    :py:class:`StimulusState` represents a state of stimulus output
    during a certain period of time, and comprises the basis of protocol specification.

    .. py:attribute:: mode

        the mode of the output. May be one of the followings:

        =========== ============================================================== ===================================================
        Mode        Related properties                                             Description
        =========== ============================================================== ===================================================
        "constant"  :py:attr:`amplitude`                                           a constant (rectangular) output
        "rect-wave" :py:attr:`amplitude`, :py:attr:`frequency`, :py:attr:`offset`  a sine-wave output with a certain frequency
        "sine-wave" :py:attr:`amplitude`, :py:attr:`frequency`, :py:attr:`offset`  a rectangular-wave output with a certain frequency
        =========== ============================================================== ===================================================

        .. note::

            In cases where e.g. amplitude changes over time during a :py:class:`StimulusBlock`: the output values is supposed to be represented by an :py:class:`expression`.

    .. py:attribute:: amplitude

        an optional (but recommended) property except for the "ramp" mode,
        representing the height of the output, in terms of the corresponding :py:class:`Quality` instance.

        For the wave-type modes, this indicates the *peak-to-peak* amplitude:
        the output range from ``offset - amplitude/2`` to ``offset + amplitude/2``.

        This property will be ignored for the "ramp" mode.

    .. py:attribute:: pulse

        an optional property for describing a pulse-like output,
        in terms of the corresponding :py:class:`Quality` instance.

        If this property is set, it is assumed that the output only lasts for :py:attr:`pulse` long.

    .. py:attribute:: offset

        an optional (but recommended) property for the wave-type modes,
        representing the offset (center) of the wave, in terms of the corresponding :py:class:`Quality` instance.

        This property will be ignored for the non wave-type modes.

    .. py:attribute:: frequency

        an optional (but recommended) property for the wave-type modes,
        representing the frequency of the wave, in terms of the corresponding :py:class:`Quality` instance.

        This property will be ignored for the non wave-type modes.

ApparatusState
^^^^^^^^^^^^^^

During manipulation of apparatus in the behavioral setup, in particular,
it is easier for a human being to understand if the state of control is written not by
the voltage/current outputs but by the actions executed by the apparatus.

:py:class:`ApparatusState` is used in such cases where it is simpler to describe
the outputs in terms of apparatus actions.

.. py:class:: ApparatusState

    this is a sort of :py:class:`Restriction`, describing the controls over
    the apparatus of interest. The predicate part is ontologically defined
    through ``amorphys-control``.

    .. admonition:: TODO

        some example ApparatusState


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

    .. py:attribute:: run-by

        an optional (but recommended) :py:class:`Program` instance,
        indicating the program that runs this sequence.

    .. py:attribute:: sequence

        a required array of :py:class:`StimulusBlock` describing the stimulus sequence.

StimulusBlock
^^^^^^^^^^^^^

.. py:class:: StimulusBlock

    :py:class:`StimulusBlock` specifies a certain period during the stimulus sequence
    where the states of output stimuli stays constant.

    It can hold a mapping of :py:class:`StimulusGeneration` instances as :py:attr:`channels`.

    .. py:attribute:: description

        a required ``string`` property, for a human-readable description of
        what takes place during this :py:class:`StimulusBlock`.

    .. py:attribute:: duration

        a required property holding a temporal :py:class:`Quality`,
        representing the duration of this :py:class:`StimulusBlock`.

    .. py:attribute:: output

        an optional mapping from a stimulus identifier to a corresponding :py:class:`StimulusGeneration`,
        indicating what stimulus is generated during this :py:class:`StimulusBlock`.

    .. caution::

        Unlike the case of :py:class:`MachineState`, this property is *memory-less* i.e. if no :py:class:`StimulusGeneration` instance is specified for a channel during this :py:class:`StimulusBlock`, **this channel is assumed to output nothing (e.g. 0 V or GND) during the block**, no matter how you specified during the previous block.

StimulusGeneration
^^^^^^^^^^^^^^^^^^

.. py:class:: StimulusGeneration

    :py:class:`StimulusGeneration` represents a certain state of output
    from a channel.

    .. py:attribute:: channel

        a required :py:class:`Signal` property that holds where the output comes out of.

    .. py:attribute:: state

        a required property consisting of a :py:class:`StimulusState` or
        a :py:class:`ApparatusState`, describing the output.


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

    .. py:attribute:: run-by

        an optional (but recommended) :py:class:`Program` instance,
        indicating the program that runs this state machine.

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

        an optional array of :py:class:`StimulusState` or :py:class:`ApparatusState` objects,
        describing what stimulus is turned on/off upon start of this state.

    .. py:attribute:: on-end

        an optional array of :py:class:`StimulusState` or :py:class:`ApparatusState` objects,
        describing what stimulus is turned on/off upon end of this state.

    .. caution::

    	Unlike the case of :py:class:`StimulusBlock`, :py:attr:`on-start` and :py:attr:`on-end` has persisting effects i.e. once you set a :py:class:`StimulusState` inside a :py:class:`MachineState`, **the output state will not be cleared** unless you explicitly do so.

MachineStateTransition
^^^^^^^^^^^^^^^^^^^^^^

.. py:class:: MachineStateTransition

    :py:class:`MachineStateTransition` represents a mapping between an incoming
    event and its corresponding target state.

    .. py:attribute:: source

        a required property hondling a :py:class:`Event` or the string ``"$timeout"``,
        representing the event input required for this state transition to occur.

        Note that the string ``"$timeout"`` refers to the state-timeout event.

    .. py:attribute:: target

        a required property hondling a :py:class:`MachineState` or the string ``"$terminate"``,
        representing the next, target state of this state transition.

        Note that the string ``"$terminate"`` refers to the termination of the state machine.
