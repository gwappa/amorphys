Experimental variables
======================

For a readability to human beings, subject- or session- dependent variables may
be better organized in tables, rather than JSON files.

"variables.json" provides a way to map experimental variables to corresponding scopes.

.. _variables-example:

An example
----------

Below is an example of "variables.json":

.. code-block:: JavaScript
    :caption: in: "variables.json"

    {
        "$schema": "https://.../amorphys.json#variables",

        "$description": "variable description for the foraging experiments.",

        "definitions": {
            "age": { "type": "integer", "minimum": 18 },
            "sex": { "type": { "enum": [ "male", "female", "other" ] } },
            "task-modes": { "type": { "enum": [ "static", "dynamic" ] } }
        },

        "subjects": {
            "participant": {
                "properties": {
                    "age": {
                        "$variable": { "$ref": "/definitions/age" },
                        "description": "the age of the participant."
                    },
                    "sex": {
                        "$variable": { "$ref": "/definitions/sex" },
                        "description": "the sex of the participant."
                    }
                },

                "phases": {
                    "surgery": {
                        "properties": {
                            "date": {
                                "$variable":   { "type": "string" },
                                "description": "the representation for the date of surgery."
                            }
                            "positionAP": {
                                "$variable":   { "type": "number" },
                                "description": "the A-P positioning of the probe, in mm."
                            },
                            "positionLR": {
                                "$variable":   { "type": "number" },
                                "description": "the L-R positioning of the probe, in mm."
                            }
                        }
                    },

                    "session": {
                        "properties": {
                            "date": {
                                "$variable":   { "type": "string" },
                                "description": "the representation for the date of this session."
                            },
                            "mode": {
                                "$variable":   { "$ref": "/definitions/task-modes" },
                                "description": "the mode of the task. 'static' means the food to find stays still at one point across trials, whereas in the 'dynamic' mode, the food changes its positions from trial to trial."
                            }
                        },

                        "programs": {
                            "task-control": {
                                "properties": {
                                    ...
                                },

                                "runs": {
                                    "properties": {
                                        ...
                                    },
                                    "conversions": {
                                        ...
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


Scopes
------

The notion of "scopes" is important. A "scope" refers to up to what level the
variable definition may be valid.

If it is subject-specific information, this must be in the ``properties`` section
directly below the path ``/subject/<type of the subject>``.
If it is session-specific information, it must be under the path
``/subject/<type of the subject>/phases/<type of the phase>/properties``.
These contexts can go down to the level of individual runs, and are referred to
as "subject scope", "phase scope", "program scope" and "run scope".

Structure of scopes
-------------------

Basic properties
^^^^^^^^^^^^^^^^

Each scope object may have the ``properties`` property, which maps a keyword to a
:py:class:`variable`.
Typically, the variable names used here are used for the column names of tables
that are going to be generated later during data acquisition.

As you can see in :ref:`the above example <variables-example>`,
the schema for a variable may be defined in the ``definitions`` section.
The ``definitions`` sections may be useful when you want to define the same structure
again and again as a common schema for different variables.

There are also cases where experimenters want to use a certain shorthand to
denote longer concepts (e.g. for description of a mouse strain).
For that purpose, the ``conversion`` property at the same level can be used
to hold :py:class:`condition` and/or :py:class:`formatter` objects that
depends on variables at the same scope.


Subsection for description of lower scope(s)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In addition to ``properties``, if the scope can have lower scopes, it can have
a special section dedicated for it.
The name of the property depends on the scope:

============== ============== ================================
Scope type     property name  Where the names are defined
============== ============== ================================
(root)         ``subjects``   :py:class:`subjects` section
subject-scope  ``phases``     :py:class:`procedures` section
phase-scope    ``programs``   :py:class:`acquisition` section
program-scope  ``runs``       (see below)
run-scope      –              –
============== ============== ================================

Under each special section, only the names defined elsewhere can be used.
for example, under the ``subjects`` property, only the names defined as the
"subject type"s in the :py:class:`subjects` section can be used.

.. caution::

	There is **no special section** within the run scope, because no name-based mapping occurs at this level.
