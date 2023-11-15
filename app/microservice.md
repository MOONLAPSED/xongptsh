This microservice utilizes multiple AI chatbot agents with language processing capabilities to clean and tokenize chat conversations within a simulated chat interface. This microservice shows its work and the reasoning behind its every change and action. This creates a chain which can be traced by future agents and eventually vectored and stored in a database. The bootstrapping process provides the agent with necessary information to start functioning and learning on its own. The microservice expects an initial prompt, and specified work as input. The microservice attempts to instantiate a loop using the tools available to it to accomplish a task working towards the work. If unable to within the constraints imposed by the cognitive architecture (be it CPU cycles, time, or number of lines of code, etc.), the agent will increment the chain of thought loop count, passing the $(artifact) (and the problem/work itself) to the next agent, or to a debugging or other available function, for additional work or for additional processing and logging as well as the __close__ for the object representing the situation within the wider-cognitive architecture.

In our microservice architecture (within the wider-cognitive architecture and other layers of abstraction laid-over the SQLite3 and UFS data/kernel/behavior), we leverage multiple AI chatbot agents equipped with language processing capabilities to handle chat conversations within a simulated chat interface. The primary objective of this microservice is to ensure transparency and traceability in every action and change made by the agents. 

Each interaction within the chat interface is meticulously recorded, allowing for a detailed audit trail. This traceability provides future agents with the ability to follow the chain of actions and reasoning behind each change, creating a comprehensive vector that can be stored in a database for future reference.

The microservice follows a loop-based approach to accomplish a task. It employs the available tools and capabilities to work towards the specified work. If the agent encounters an existential or insurmountable obstacle, or is unable to achieve the desired outcome (per the settings), it increments the loop count and the agent then passes the modified output, including its changes (called the $(artifact)), as parameters to the next agent in the chain to attempt the task again, or to another existing-element of the wider-cognitive, or the microservice architectures. 

To initiate the microservice, an initial prompt and specified work are provided as input. The microservice utilizes this information to bootstrap the agent, equipping it with the necessary knowledge to start functioning and learning independently.

The microservice implements an iterative refinement process for multiple AI agents to collaboratively fulfill a specified {prompt}. 

Each agent follows an {output schema} with:

  - A success boolean
  - A message string representing their attempt
  - Any changes made to the evolving {artifact}

Agents take turns attempting the {prompt} until one succeeds or indicates it has reached its limit. 

If an agent other than the final agent succeeds, it must take on the data integrity and logging responsibilities of the last agent before ending the loop.

The {evolving artifact} captures the agents' {collective understanding} as it progresses, starting from the first agent's {initial attempt}, incorporating {clarifications} and {additions} from subsequent agents, and culminating in the {refinement} achieved by the completing agent.

The {thought loop count} indicates the number of iterations and tracks each agent's #{identifier} and associated output.

Assumptions should be minimized due to risk from incomplete information. The first and completing agents have additional duties around logging, consistency, and accountability using standard output.

The {artifact} represents the {collaborative output} of the overall {iterative refinement process}.
