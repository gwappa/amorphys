Miscellaneous
==============

dataset
--------

.. py:class:: dataset

    a class to represent the metadata for this project dataset as a whole,
    including a license information based on a :py:class:`license` object.

    a typical :py:class:`dataset` would look something like below:

    .. literalinclude:: /_static/misc/dataset.json
        :language: javascript
        :caption:  example dataset object

    .. py:attribute:: name

        a required ``string`` property representing the identifiable name of this dataset as a whole.

    .. py:attribute:: description

        a required ``string`` property representing the description of this dataset as a whole.

    .. py:attribute:: keywords

        an optional array of ``string`` objects representing the free keywords for this dataset.

    .. py:attribute:: license

        a required :py:class:`license` object corresponding to the license clause of this dataset publication.

    .. py:attribute:: references

        a required array of :py:class:`citation` objects referring to the articles related to this dataset.

credit
-------

.. py:class:: credit

    a ``string`` role of a :py:class:`contributor`, specified in terms of
    `contributor roles <https://dictionary.casrai.org/Contributor_Roles>`_
    (as it is defined in the `CRediT taxonomy <https://www.casrai.org/credit.html>`_).

    It must be one of the followings:

    - **conceptualization**
    - **project-administration**
    - **supervision**
    - **funding-acquisition**
    - **investigation**
    - **methodology**
    - **software**
    - **formal-analysis**
    - **visualization**
    - **writing-original-draft**
    - **writing-review-editing**
    - **data-curation**

funding
--------

.. py:class:: funding

    (TODO)
