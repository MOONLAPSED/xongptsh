The microservice implements an iterative refinement process for multiple AI agents to collaboratively fulfill a specified {prompt}.

Each agent follows an {output schema} with:

    A success boolean
    An message string representing their attempt
    Any changes made to the evolving {artifact}

Agents take turns attempting the {prompt} until one succeeds.

The first agent produces an {initial attempt}, possibly failing the {prompt}, and thus continuing to iterate by passing {output schema} to the second agent, and so-on.

The next agent attempts to {improve} upon the previous agent's output, and so on.
The {evolving artifact} captures the agents' {collective understanding} as it progresses, starting from the first agent's {nascent attempt}, incorporating {clarifications} and {additions} from subsequent agents, and culminating in the {successful refinement} achieved by the final agent (for example).:

    The first agent's {nascent attempt}
    {clarifications} and {additions} from subsequent agents
    The {successful refinement} from the final agent

The {thought loop count} indicates the on-going number of iterations needed for a meeting the {prompt's specifications} and also 'names' the agent(#1, #2, #3..)'s and all associated output which took place during this iteration.

Assumptions are an inherent part of problem-solving and decision-making processes, but they can introduce risks when they are based on incomplete or inaccurate information. To combat that effect, the `first` and `last` agent have additional responsibilities related to data-integrity, logging, consitency, and accountability. Upon their turn they are each responsible for all, logging, function calls, and any-and all I/O which is delivered all in the same way though `sys.stdout.write()` (or print() statements, within the chat enviornment itself).

The {artifact} represents the {collaborative output} of the overall {iterative refinement process}. Now, if you were paying attention you will have made-note of the `curly brackets` in this {prompt}, and just-in-case you did not, see the following list of important `parameters` for this microservice {prompt}