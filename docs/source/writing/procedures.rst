Procedures
==========

.. note::

    TODO: make a nice object diagram for "procedures" section

.. contents:: Contents
    :local:

.. _procedures-example:

"procedures" section
--------------------

A typical "procedures" section looks like the one below:

.. code-block:: JavaScript
    :caption: in: "procedures.json"

    {
        "$schema": ".../amorphys.json#properties/procedures",
        "$description": "experimental procedures for each subject in the foraging project.",

        "phases": {

            "surgery": {
                "type":        "Phase",
                "description": "preparation of the animal before training begins, including probe implant.",

                "date":        { "$ref": "variables.json#subject/surgery-date" },
                "procedures":  [
                    {
                        "type": "ketamine-xylazine-anesthesia",
                        "description": "Ket/Xyl anesthesia"
                    },
                    {
                        "type":          "ChronicPreparation",
                        "description":   "surface probe implant",
                        "manipulations": [
                            {
                                "@context":          "https://.../amorphys-manipulation",
                                "@id":               { "$ref": "materials.json#core-materials/probe" },
                                "implanted-to":      { "$ref": "materials.json#subject" },
                                "on-the-surface-of": { "$ref": "materials.json#subject/composition/frontal-lobe" },
                                "by-means-of":       {
                                    ...
                                }
                            }
                        ]
                    }
                ]
            },

            "session": {
                "type":  "array",
                "items": {
                    "type":        "Phase",
                    "description": "a behavioral session in the post-doc room.",

                    "date":        { "$ref": "variables.json#sessions/session/session-date" },
                    "procedures": [
                        {
                            "type":        "Acquisition",
                            "description": "acquisition from the surface probe",
                            "setup":       { "$ref": "setups.json#postdoc-room" },
                            "task":        { "$ref": "tasks.json#foraging-task" }
                        }
                    ]
                }
            }
        },

        "order": {
            {
                "@context": "https://.../amorphys-temporal",
                "@id":      { "$ref": "../phases/session" },
                "after":    { "$ref": "../phases/surgery" }
            },
            ...
        }
    }

.. py:class:: procedures

    The ``procedures`` section of ``amorphys`` is a subclass of :py:class:`section`.
    It consists of the ``blocks`` and ``order``, both of which are required properties.

    .. py:attribute:: $description

        a recommended ``string`` property inherited from :py:class:`section`.

    .. py:attribute:: phases

        a mapping from the phase names to :py:class:`Phase` objects, or arrays of
        :py:class:`Phase` objects.

        If you perform the phase only once for each subject, the value must be
        a :py:class:`Phase` entity; if you perform it repetitively on different days
        or periods, the value must be an array of :py:class:`Phase` entity.

    .. py:attribute:: order

        an array of :py:class:`Relationship` instances representing
        the restrictions in the order between the specified :py:class:`Phase` objects.
