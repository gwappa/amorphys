Task/Sweep control
==================

.. contents:: Contents
    :local:

"tasks" section
----------------

The "tasks" section describes the model of the task, in a format
more human-friendly than in the :doc:`"setups" <setups>` and :doc:`"acqusition" <acquisition>` sections.

A typical :py:class:`tasks` section would look like below:

.. code-block:: JavaScript
    :caption: in: "tasks.json"

    {
        "$schema":      "https://.../amorphys.json#properties/tasks",
        "$description": "task description for the foraging project",

        "foraging-task": {
            "description": "human foraging task",

            "subject": {
                "description": "the behavioral model of the subject during the foraging task.",
                "cues": {
                    "reward": {
                        "type":        "reward-cue",
                        "by-means-of": { "$ref": "setups.json#postdoc-room/components/something-edible" },
                        "description": "when a subject examined the correct place, a reward was given."
                    }
                },
                "actions": {
                    "wander": {
                        "type":         "locomotion",
                        "monitored-by": { "$ref": "setups.json#postdoc-room/components/webcam" },
                        "description":  "the subject was allowed to move and examine freely inside the room."
                    },
                    "examine": {
                        "type":         "active-sensing",
                        "monitored-by": { "$ref": "setups.json#postdoc-room/components/webcam" },
                        "description":  "through the webcam, the object-tracking program monitors the active exploration behavior of the subject."
                    }
                }
            },

            "control": {
                "type":        "state-machine",
                "description": "task control sequence",
                "run-by":      { "$ref": "acquisition.json#programs/task-control" },
                "initial":     { "$ref": "states/hide" },
                "states": {
                    "hide": {
                        "description": "an experimenter hides something edible inside a postdoc room.",
                        "transitions": {
                            {
                                "source": { "$ref": "acquisition.json#signals/task-state/values/ready" },
                                "target": { "$ref": "../../seek" }
                            }
                        }
                    },
                    "seek": {
                        "description": "the subject looks for something edible.",
                        "transitions": {
                            {
                                "source": { "$ref": "acquisition.json#signals/task-state/values/seek-right-place" },
                                "target": "$terminate"
                            }
                        }
                    }
                }
            }
        }
    }

.. py:class:: tasks

    The ``tasks`` section of ``amorphys`` is a subclass of :py:class:`section`,
    and consists of a mapping of :py:class:`task-description` objects.

    Multiple :py:class:`task-description` objects may be included inside this section,
    and each of them can be referred to from elsewhere by its key
    (i.e. ``"foraging-task"`` in the above example).

    .. py:attribute:: $description

        a recommended ``string`` field inherited from the :py:class:`section` class.

.. py:class:: task-description

    .. py:attribute:: description

    .. py:attribute:: subject

    .. py:attribute:: control
