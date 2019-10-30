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

        "channels": {
            ...
        }
    }

.. py:class:: acquisition

    The ``acquisition`` section of ``amorphys`` is a subclass of :py:class:`section`.
    It holds :py:class:`Program` and :py:class:`Quality` instances.

    .. py:attribute:: $description

        a recommended ``string`` field inherited from the :py:class:`section` class.

    .. py:attribute:: programs

        a required mapping that maps program names to :py:class:`Program` instances
        used in the experiments. In case the same program (e.g. Matlab) is used but
        in different ways (e.g. intrinsic signal acquisition vs behavioral control)
        during different contexts (e.g. surgery vs training sessions), it must be
        split into different instances.

        For an example Program, refer to :ref:`this section <program-example>`.

    .. py:attribute:: channels

        a required mapping that maps channel names to :py:class:`Quality` instances
        used in the experiments. Note that, as soon as a :py:class:`Quality` instance
        gets processed by a device or a program, it must turn into another distinct
        :py:class:`Quality` instance with a different name.

        For an example channel (Quality), refer to :ref:`this section <quality-example>`.
