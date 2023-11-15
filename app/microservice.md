"""
this microservice utilizes multiple AI chatbot agents with language processing functionality to clean and tokenize chat conversations within a simulated chat interface. This microservice shows its work and the reasoning behind its every change and action. This creates a chain which can be traced by future agents and eventually vectored and stored in a db. The bootstrapping process provides the agent with necessary information to start functioning and learning on its own. The microservice expects an initial prompt, and specified work as input. The microservice attempts to instantiate a loop using the tools available to it to accomplish a task working towards the work. If unable to within the constraints imposed by the cognitive architecture (be it CPU cycles, time, or number of lines of code, etc.), the agent will increment the chain of thought loop count, and passing the artifact to the next agent, or to a debugging function, for additional work or for additional processing and logging as well as the __close__ for the object representing the situation within the wider-cognitive architecture. 
"""

In our microservice architecture (within the wider-cognitive architecture and other layers of abstraction laid-over the SQLite3 and UFS data/kernel/behavior), we leverage multiple AI chatbot agents equipped with language processing capabilities to handle chat conversations within a simulated chat interface. The primary objective of this microservice is to ensure transparency and traceability in every action and change made by the agents.

Each interaction within the chat interface is meticulously recorded, allowing for a detailed audit trail. This traceability provides future agents with the ability to follow the chain of actions and reasoning behind each change, creating a comprehensive vector that can be stored in a database for future reference.

The microservice follows a loop-based approach to accomplish a task. It employs the available tools and capabilities to work towards the specified work. If the agent encounters an exestential or insurmountable obstacle, or is unable to achieve the desired outcome (per the settings), it increments the loop count and the agent then passes the modified output, including its changes (called the $(artifact)), as parameters to the next agent in the chain to attempt the task again, or to another existing-element of the wider-cognitive, or the microservice architectures.

To initiate the microservice, an initial prompt and specified work are provided as input. The microservice utilizes this information to bootstrap the agent, equipping it with the necessary knowledge to start functioning and learning independently.

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
