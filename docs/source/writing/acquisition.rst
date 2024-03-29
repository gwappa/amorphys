Acquisition
===========

.. note::

    TODO: make a nice object diagram for "acquisition" section

.. contents:: Contents
    :local:

"acquisition" section
---------------------

A typical :py:class:`acquisition` section would look like below:

.. code-block:: JavaScript

    {
        "$schema":      "https://.../amorphys.json#properties/acquisition",
        "$description": "the acquisition programs related to the foraging behavior project.",

        "programs": {
            ...
        },

        "signals": {
            ...
        },

        "conversion": [
            ...
        ]
    }

.. caution::

	Note that, during actual acquisitions, not all the programs may be run. In other words, you can list as many programs as you can imagine in the `programs` field.

.. py:class:: acquisition

    The ``acquisition`` section of ``amorphys`` is a subclass of :py:class:`section`.
    It holds :py:class:`Program` and :py:class:`Signal` instances.

    .. py:attribute:: $description

        a recommended ``string`` field inherited from the :py:class:`section` class.

    .. py:attribute:: programs

        a required mapping that maps program names to :py:class:`Program` instances
        used in the experiments. In case the same program (e.g. Matlab) is used but
        in different ways (e.g. intrinsic signal acquisition vs behavioral control)
        during different contexts (e.g. surgery vs training sessions), it must be
        split into different instances.

        For an example Program, refer to :ref:`this section <program-example>`.

    .. py:attribute:: signals

        a required mapping that maps channel names to :py:class:`Signal` instances
        used in the experiments. Note that, as soon as a :py:class:`Signal` instance
        gets processed by a device or a program, it must turn into another distinct
        :py:class:`Signal` instance with a different name.

        For an example, refer to :ref:`this section <signal-example>`.

    .. py:attribute:: conversion

        a required array (but can be empty) of :py:class:`Relationship` objects
        that describes how each :py:class:`Signal` in :py:attr:`channels`
        relates to each other.

        For available vocabulary, refer to :ref:`signal-relationships`.
