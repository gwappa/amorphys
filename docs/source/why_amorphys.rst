Why amorphys?
==============

Motivations
------------

Below are some motivations behind development of ``amorphys``.

1. **Help researchers design their experiments**

    Writing metadata is a daunting task, because you don't feel the necessity to write
    it after everything is done, and you think you understand everything about your
    setups. Maybe it is not the right time to start writing metadata; metadata is
    for people who don't know (probably anything) about how you did your experiments.

    But what if you start writing metadata as you design your experiments?

    Your mind may be so disorganized at first that you need something that helps you
    organize what sort of a rig to be set up, and what material to be prepared.
    This situation may be similar to that when a newcomer wants to start an experiment
    like you, after you finished your work.

    I believe that, for a researcher, the use of metadata from the very beginning of
    the project is the right strategy.

2. **Help researchers organize their raw data**

    When you begin your experiment, you will probably use an ad-hoc format of
    organizing your raw data. It may be the format that worked with your
    previous project, or may be something you made up on-site.
    In fact, this works totally fine by itself. By looking at the name, you will see
    what you did in the past. By examining the content, you will see what you acquired.

    The problem may arise when things get more complex. If your data acquisition
    involves multiple programs (possibly running on multiple computers) that acquire
    data in different formats, it becomes harder to keep the naming convention consistent,
    and harder to keep the raw data organized at one place. As the time passes,
    you may forget what you have exactly done, and where you placed your raw data
    (even if it exists "somewhere in one of your external HDDs").

    The last thing you may be afraid of would be when a researcher leaves your lab for long.
    Different people have their own convention of how to organize their own data.
    It makes sense as long as you find out how the others did to organize their data,
    but if not, all the knowledge that used to be in his/her mind, is basically lost,
    even though the raw data is still there.

    I believe that, if a program can manage the organization of your raw data
    in accordance with your metadata, there will be an increased chance of
    finding out, and making sense of, the existing data sets.

3. **Help researchers make use of the data acquired by others**

    This is the pressure that a researcher would normally face.
    People in some grant offices would say, "why can't you share your data with others?
    it will help each other, and reduce the number of unnecessary experiments!"

    In reality, however, it is not known how to take advantages of having data shared
    (except for the possibility of meta-analysis; see :ref:`below <meta-analysis>`),
    in the field of animal neurophysiology, in particular.

    From a user's point of view, it is still hard to find out any experiments
    that may help your project at all.
    From a provider's point of view, on the other hand, you have troubles in
    what metadata to be shared, for your data to be discovered by somebody
    who may find it useful. Giving arbitrary "key words" to datasets can cause
    more confusion than solving any, because people in different sub-disciplines,
    who are the most likely potential users, often think differently, and use
    different vocabulary.

    I believe that, in many cases, you don't need to describe your experiments
    in words. In every experiment, there is a specific structure to examine
    some scientific question. If you could describe this structure, and if the others
    could "read" this structure, you would not have to "summarize" what you did
    in your experiments. In addition, if it is about reading a certain aspect
    of the structure, even a computer program can do it. This means that a
    search engine could be built from thousands of shared datasets.

    I hope to specify a minimal metadata structure enough to describe the important aspects
    of your experiments.

.. _meta-analysis:

4. **Help researchers reconcile contradicting results**

    Currently, most researchers in the field of neurophysiology (of animals,
    in particular) do not share their data and their metadata, and talk about them
    in the format of journal articles. Probably it is a better way of discussing
    about diverse scientific issues, than talking over lots of raw data and metadata.
    However, this sometimes become problematic, when findings do not reproduce.
    Sometimes different research groups do almost the same type of experiments,
    and draw completely opposite conclusions. In another case, a research group
    reports some great finding (or a method) that, seemingly, helps proceed the
    field of science. People around it are fascinated, and try to reproduce their
    report, and they just fail.

    In such cases, it is extremely easy to say "what they reported was wrong. period."
    But I believe that the progress of science occurs through attempts to reconcile
    seemingly contradicting results. Before judging the others as being wrong,
    one must ask how these contradictory results come about.

    In doing so, comparison of experimental conditions is necessary.
    In most cases, the difference does not lie in what people reported,
    but where people took granted and did not report.
    By definition, these hidden conditions can not be incorporated at the time
    they publish their metadata. But addition of hidden variables can occur
    any time, even during the very progress of the project. I think that it is
    important for science to keep the metadata format so flexible that you can
    incorporate additional conditions at any moment.

Core concerns
--------------

Description of (neuro-)physiology experiments involves lots of painstaking annotation processes
(`Zehl et al., 2016 *Front Neuroinform* <https://www.frontiersin.org/articles/10.3389/fninf.2016.00026/full>`_).
A pivotal issue is that annotation spans multiple, conceptual dimensions such as:

- all the different sorts of experimental variables
- descriptions on spatial configuration,
- temporal sequences of manipulations
- different types of signals
- distinct flows of information
- etc.

all of which must be taken care of, in order to make a grasp of one single experiment.
Further, experimental subjects (hardwares, softwares, animals, signals) require a multi-dimensional
way of description, and their interactions are often multi-dimensional.

To efficiently handle metadata of (neuro-)physiological experiments,
I believe that **metadata annotation must be aware of this multi-dimensional nature of
experimental descriptions**.

Core concepts
--------------

``amorphys`` aims to solve this problem of multi-dimensionality by building a relational structure
to describe the experiment of interest:

- Each single concept may be defined as an entity in a certain dimension.
- Different entities may interact with each other across the border of dimensions,
  using a *reference* to each other.
- ``amorphys`` provides a basic set vocabulary for description of interactions.

The basic grammar of ``amorphys`` is defined in `JSON schema <https://json-schema.org/>`_,
and references may be made using `JSON reference <https://json-spec.readthedocs.io/reference.html>`_.
You can write ``amorphys``-compliant experiment descriptions in, and not limited to, JSON and YAML.


How is it going to work?
------------------------

I hope that *individual researchers* (i.e. not only data curators) can make
use of the ``amorphys`` format.

Editor UI
^^^^^^^^^

For the moment, ``amorphys`` is written (almost) completely by hand,
which is a cumbersome job (I don't recommend anybody to do this).
I plan to implement a GUI ``amorphys`` editor at some point, but it will
still be a burden for researchers.

Designer UI
^^^^^^^^^^^

However, as it is a machine-readable format, I expect a tool that is built
on top of this format.

For example, I can imagine a graphical tool for designing an experiment which exports the configurations
out into the ``amorphys`` format.
By doing so, one would readily share his/her experimental description with other *even before starting the experiment*.
This strategy would also be useful when people want to replicate an experiment done by somebody else.

Experiment runner
^^^^^^^^^^^^^^^^^

Another example is when running an experiment.
If the software knows the big picture of your experiment as it acquires the data,
it is possible to organize the dataset (in a specific directory structure) as it collects it.
The important point here is that the solution can be adapted to *any* experiment designs,
as they are already generalized by the ``amorphys`` format.

After specification of the format, I am willing to implement tools like these.
