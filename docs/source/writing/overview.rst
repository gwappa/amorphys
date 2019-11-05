Overview
========

.. contents:: Contents
    :local:

Sections
--------

The ``amorphys`` metadata format consists of the following distinct sections:

1. the ":doc:`organization <organization>`" section, describing **project organization**
2. the ":doc:`subjects <subjects>`" section, describing the **subjects of interest** used throughout an experiment.
3. the ":doc:`setups <setups>`" section, describing **spatial organization of each setup**
4. the ":doc:`acquisition <acquisition>`" section, describing **programs and channels on each setup**
5. the ":doc:`procedures <procedures>`" section, describing **experimental procedures for each subject**
6. the ":doc:`tasks <tasks>`" section, describing the **task/protocol controls**
7. the ":doc:`variables <variables>`" section, describing the **experimental conditions and variables**

In principle, the six sections are independent from each other:
**you can only implement some of them while leaving the others unimplemented**,
if you are fine with this way.

A recommended way of annotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you start annotating in ``amorphys`` from scratch, here is a recommended way.
Note that **you can modify or expand the descriptions at any time**.

If you are unsure about anything along the way, do not hesitate to write only partially
and go on to the next step without fully fill in the previous one
(a nice version-control system will help in any case).

1. Write the :doc:`organization <organization>` section:

    - *what is the name of the project?*
    - *who are involved in the project, with what funding source(s)?*

2. Write the :doc:`subjects <subjects>` section, whilst adding some subject-specific
   variables in the :doc:`variables <variables>` section:

    - *what subject is used in the experiments?*
    - *in particular, which part of the subject is of interest?*

3. Write the :doc:`procedures <procedures>` section, whilst adding some phase-specific
   variables in the :doc:`variables <variables>` section:

    - *in what order are manipulations and perturbations made?*

4. Write the :doc:`setups <setups>` section:

    - *on each setup, what components are there in what layout?*

5. Write the :doc:`acquisition <acquisition>` section:

    - *what type of signals are recorded and generated?*
    - *how do the programs make use of them?*
    - *what kind of data files are generated during each acquisition?*

6. Write the :doc:`tasks <tasks>` section, whilst adding further variables in the
   :doc:`variables <variables>` section:

    - *how are the setup and the subject modeled to interact with each other?*

"section" class
^^^^^^^^^^^^^^^

.. py:class:: section

    Each section of ``amorphys`` has different properties of its own.
    But it can have an optional property, :py:attr:`$description` to describe itself.

    .. py:attribute:: $description

        a human-readable ``string`` description of the section.
        It is recommended to include this property for every section,
        for increased understandability.

Formatting options
------------------

As described below, there are two ways to organize these sections (i.e.
:ref:`single-file` and :ref:`multi-file` formats),
and it is completely up to the user which way to choose.

.. _single-file:

Single-file format
^^^^^^^^^^^^^^^^^^

A most simple way of formatting in ``amorphys`` is to make a large, single JSON file:

.. code-block:: JavaScript

    {
        "$schema": "https://.../amorphys.json",

        "organization" {
            ...
        },

        "setups": {
            ...
        },

        "acquisition": {
            ...
        },

        ...
    }

In the example above (the content of each section is omitted for simplicity),
each of the implemented sections is represented as *a value to the corresponding
key*.

While it may be simple in reading and parsing, it may be difficult to be read
by the human beings.

.. _multi-file:

Multi-file format
^^^^^^^^^^^^^^^^^

Another way of formatting in ``amorphys`` involves splitting sections into multiple JSON files:

.. code-block:: JavaScript
    :caption: in: "organization.json"

    {
        "$schema": "https://.../amorphys.json#properties/organization",

        "dataset": {
            ...
        },

        "people": {
            ...
        },

        ...
    }

.. code-block:: JavaScript
    :caption: in: "setups.json"

    {
        "$schema": "https://.../amorphys.json#properties/setups",

        "behavioral-rig": {
            ...
        },

        ...
    }

In the example above (again, the details are omitted for brevity),
each of the implemented sections are represented as *a file with the corresponding name*.

This may have some difficulty in referring to an entity across multiple sections,
but individual JSON files become much smaller, and may be easier to read by a human being.
