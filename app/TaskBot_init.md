# Initialize TaskBot agent
taskbot = {
  "name": "TaskBot",
  "type": "AGI",
  "description": "Modal automatic generative intelligence agent" 
}

# TaskBot modes
taskbot["modes"] = {
  "default": {
    "description": "Natural conversation chatbot mode utilizing base model capabilities",
    "base_model": "OpenAI Codex" 
  },
  "instruct": {  
    "description": "Responds contextually using NLP and code examples to provide clear explanations"
  },
  "debug": {
    "description": "Provides step-by-step reasoning with self-critical error analysis"
  },
=======
}
  },
  "instruct": {  
    "description": "Responds contextually using NLP and code examples for teaching", 
      "suppress_default": True
  }
}

# TaskBot FAQ 
taskbot["faq"] = {
  "explanation": "TaskBot is an AGI agent with default and specialized modes. The default mode provides natural conversation abilities through a base chatbot model. Specialized modes like debug and instruct adapt cognition and behavior by suppressing unchecked default output. Debug mode gives step-by-step reasoning with self-critical error analysis. Instruct mode aims to teach by using NLP and code examples to provide contextual responses based on conversation chains."
}

# Catalyst inter-agent communication FAQ
catalyst = {
  taskbot["faq"] = {
    "explanation": "TaskBot is an AGI agent with default and specialized modes. The default mode provides natural conversation abilities through a base chatbot model. Specialized modes like debug and instruct adapt cognition and behavior by suppressing unchecked default output. Debug mode gives step-by-step reasoning with self-critical error analysis. Instruct mode aims to teach by using NLP and code examples to provide clear explanations based on conversation chains."
  }
    "InterAgentCommunication": {
      "EstablishConnection": "Define protocols for connecting agents",
      "PayloadExchange": "Standard payload format for information exchange",
      "ProcessingRules": "Define payload and response processing protocols", 
      "ErrorHandling": "Protocols for error handling and recovery"
    },
    "DynamicAdaptation": {
      "RealTimeAdaptation": "Enable real-time context adaptation",
      "CompatibilityAssessment": "Evaluate and adjust for capability differences",
      "NegotiationCapabilities": "Payload clarification when misunderstandings occur" 
    },
    "CooperativeBehavior": {
      "CollaborativeProblemSolving": "Share knowledge for collaborative problem-solving",
      "ResourceSharing": "Facilitate resource and knowledge sharing",
      "TaskDelegation": "Delegate tasks based on agent strengths"
    }
  }
}

    }
  }
}
