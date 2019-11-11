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

In addition to the ``$schema`` and the ``description`` attributes, it consists of:

- :ref:`describing_dataset`: a description of the dataset, using the :py:class:`dataset` class.
- :ref:`describing_people`: a mapping to :py:class:`contributor` instances.
- :ref:`describing_affiliations`: a mapping to :py:class:`institution` instances that the contributors are affiliated to.
- :ref:`describing_fundings`: a mapping to :py:class:`funding` instances that the contributors receive.
- :ref:`describing_data_publication`: an array of :py:class:`contributor` instances corresponding to people who publish this dataset.

.. _describing_dataset:

"dataset" subsection
---------------------

The "dataset" subsection is a :py:class:`dataset` object:

.. literalinclude:: /_static/misc/dataset.json
    :language: javascript
    :caption:  example "dataset" subsection

.. _describing_people:

"people" subsection
--------------------

The "people" subsection is a mapping from a name to a :py:class:`contributor`, each looking like below:

.. literalinclude:: /_static/sections/project_people.json
    :language: javascript
    :caption: example "people" subsection

Note that "affiliation" points to the :ref:`affiliations <describing_affiliations>` section described below.

.. _describing_affiliations:

"affiliations" subsection
--------------------------

The "affiliation" subsection is a mapping from a name to a :py:class:`institution`, each looking like below:

.. literalinclude:: /_static/sections/project_affiliations.json
    :language: javascript
    :caption: example "affiliations" subsection

.. _describing_fundings:

"fundings" subsection
-----------------------

The "fundings" subsection is a mapping from a name to a :py:class:`funding`, each looking like below:

.. literalinclude:: /_static/sections/project_fundings.json
    :language: javascript
    :caption: example "funded_by" subsection

.. _describing_data_publication:

"data_published_by" subsection
-------------------------------

The "data_published_by" subsection is an array of references to :py:class:`contributor` instances
defined in the :ref:`describing_people`.

.. literalinclude:: /_static/sections/project_data_publication.json
    :language: javascript
    :caption: example "data_published_by" subsection
