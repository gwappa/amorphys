Core materials
==============

.. contents:: Contents
    :local:

"materials" section
-------------------

A typical :py:class:`materials` section would look like below:

.. code-block:: JavaScript
    :caption: in: "materials.json"

    {
        ...(TODO)...
    }

Note that the paths such as ``materials.json#subject`` may be referred to from
the other ``amorphys``-related documents such as ``setups.json`` or ``procedures.json``.

.. py:class:: materials

    The ``materials`` section of ``amorphys`` is a subclass of :py:class:`section`,
    and consists of the following properties:

    .. py:attribute:: $description

        a recommended ``string`` field inherited from the :py:class:`section` class.

    .. py:attribute:: subject

        a required :py:class:`Subject` property indicating what type of subjects are
        used in this study. You can fill in the fields that are common across all subjects used.

        For the fields that can vary between subjects, you can use :doc:`variable-type objects <../core/variable>`
        instead.

    .. py:attribute:: core-materials

        an optional mapping from names to :py:class:`Spatial` objects, indicating
        what materials are used throughout the course of an experiment,
        along with the :py:attr:`subject`.

        Possible entities include:

        - implanted components (head-posts, cannula, chronic windows etc.)
        - materials that are chronically introduced into the body (chronic drug admin., virus injection etc.)
