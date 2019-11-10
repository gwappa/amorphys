Making a project description
=============================

.. admonition:: TODO

    - add tutorial for the "project" section
    - make a nice object diagram for "organization" section

.. contents:: Contents
    :local:

Organization of "project" section
----------------------------------

A typical :py:class:`project` would look like below:

.. literalinclude:: /_static/sections/project.json
    :language: javascript
    :caption: in: "project.json"

In addition to the ``$schema`` and the ``_description`` attributes, it consists of:

- :py:attr:`dataset <project.dataset>`: a description of the dataset, using the :py:class:`dataset` class.
- :py:attr:`people <project.people>`: an array of :py:class:`contributor` instances.
- :py:attr:`affiliations <project.affiliations>`: an array of :py:class:`institution` instances that the contributors are affiliated to.
- :py:attr:`funded_by <project.funded_by>`: an array of :py:class:`funding` instances that the contributors receive.
- :py:attr:`data_published_by <project.data_published_by>`: an array of :py:class:`contributor` instances corresponding to people who publish this dataset.

Describing "dataset" subsection
--------------------------------

The "dataset" subsection is a :py:class:`dataset` object:

.. literalinclude:: /_static/misc/dataset.json
    :language: javascript
    :caption:  example "dataset" subsection
