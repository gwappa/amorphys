Subject description
===================

.. contents:: Contents
    :local:

"subjects" section
-------------------

A typical :py:class:`materials` section would look like below:

.. code-block:: JavaScript
    :caption: in: "materials.json"

    {
        "$schema": "https://.../amorphis.json#subject",
        "$description": "description of subjects for the foraging-behavior experiments.",

        "participant": {
            "type": "Participant",
            "description": "the participant to our foraging-behavior experiments",

            "implants": {
                "probe": {
                    "type": "Device",
                    ...
                }
            }
            ...
        }
    }

Note that the paths such as ``materials.json#subject`` may be referred to from
the other ``amorphys``-related documents such as ``setups.json`` or ``procedures.json``.


.. py:class:: subjects

    The "subjects" section is a subclass of :py:class:`section`.
    It is a mapping from names to :py:class:`Subject` entities indicating
    what type of subjects are used in this study.

    You can fill in the fields that are common across all subjects used here.
    For the fields that can vary between subjects, you can use
    :doc:`variable-type objects <../core/variable>` instead.

    .. py:attribute:: $description

        a recommended ``string`` field inherited from the :py:class:`section` class.
