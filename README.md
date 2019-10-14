# amorphys

"amorphys" stands for "asymptotic metadata organization in physiology", whatever it means.

## Background

Description of (neuro-)physiology experiments involves lots of painstaking annotation processes
([Zehl et al., 2016 _Front Neuroinform_](https://www.frontiersin.org/articles/10.3389/fninf.2016.00026/full)).
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

To efficiently handle metadata of (neuro-)physiological experimenta,
I believe that __metadata annotation must be aware of this multi-dimensional nature of
experimental descriptions__.

## What is amorphys?

`amorphys` aims to solve this problem of multi-dimensionality by building a relational structure
to describe the experiment of interest:

- Each single concept may be defined as an entity in a certain dimension.
- Different entities may interact with each other across the border of dimensions,
  using a _reference_ to each other.
- `amorphys` provides a basic set vocabulary for description of interactions.

The basic grammar of `amorphys` is defined in [JSON schema](https://json-schema.org/),
and references may be made using [JSON reference](https://json-spec.readthedocs.io/reference.html).
You can write `amorphys`-compliant experiment descriptions in, and not limited to, JSON and YAML.

## Structure

In `amorphys`, you can describe different aspects of your experiment:

- `organization`: overall description of the project, and people involved in it.
- `setups`: spatial configurations of different setups being used in the experiment,
  along with all the physical components that comprise them.
- `acquisition`: different programs used to acquire raw data, and all the signals they deal with.
- `procedures`: a temporal sequences of manipulations/perturbations made to the subject(s).
- `tasks`: organization of stimuli and responses for behavioral tasks and stimulation protocols.
- `variables`: experimental variables that may vary across experiments.

Note that you can start from partial implementation: for example,
you can first only implement `organization` and `setups`,
and then expand the description to `acquisition` and `procedures`.

For experimental variables used during each single experiment, you can put
actual values into a table (e.g. in the tab-separated-value (TSV) format).

## How is it going to work?

I hope that _individual researchers_ (i.e. not only data curators) can make
use of the `amorphys` format.

For the moment, `amorphys` is written (almost) completely by hand, which is a cumbersome job
(I don't recommend anybody to do this).
I plan to implement a GUI `amorphys` editor at some point, but it will still be a burden
for researchers.
However, as it is a machine-readable format, I expect a tool that is built on top of this format.

For example, I can imagine a graphical tool for designing an experiment which exports the configurations
out into the `amorphys` format.
By doing so, one would readily share his/her experimental description with other _even before starting the experiment_.
This strategy would also be useful when people want to replicate an experiment done by somebody else.

Another example is when running an experiment.
If the software knows the big picture of your experiment as it acquires the data,
it is possible to organize the dataset (in a specific directory structure) as it collects it.
The important point here is that the solution can be adapted to _any_ experiment designs,
as they are already generalized by the `amorphys` format.

After specification of the format, I am willing to implement tools like these.

## License

The MIT License.
