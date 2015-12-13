## 10-20 Knowledge Representation
* **Slot-filler Structures** - way to model logic with hiearchy.
* **Semantic Nets** - visual, not very accurate though, allows inheritance
  can have contradictions, nodes - concepts, arcs - relationships.
* **Subtleties** - to represent binary relationships, use isa by
  passing an instance. have to specify properties of a set, or properties 
  of an instance
* **Quantifiers** - instance is one link, for all is link to all nodes.
* **Intersection Search** - propagate two nodes, finds path to intersection.
* **Spreading Activation** - weighted sums of activity values, weight of relations
* **Marker Passing** - 
* **Frames** - more structure in nodes, collection of slots (attributes), constraints, 
  list of lists, just a class system.
* **Frame System** - slots filled with other frames.
* **Is A** - subset.
* **Instance** - element.
* **Slot** - constrained by attributes, (default, inverse, single valued).
* **Frame Issues** - 
* **Frame Languages** - FRL, KRL, KL-ONE, KRYPTON.
* **Frame Issues** - quantifications, disjunctions, not good for deep deductions.
* **CYC System** - Lenat, want to capture human common sense, turn encyclopedia 
  into frame structures, comes up with questions.
* **Botany Halo** - Porter, multifuncitonal knowledge, machine learning,
  gets Chemistry AP credit.
* **Watson** - shallow database, statistical matching, machine learning.
* **NELL** - never ending language learning, reads the web, extracts facts.

## 10-20 NLP
* **Rationalist** - belief language is innate.
* **Empiricist** - belief language is a product of human mind, induced.
* **Phonological Analysis** - form segmentation of sounds into syllables,
  string of discrete phonemes.
* **Morphological Analysis** - 
* **Morphophonology** - grouping of speech.
* **Prosodic** - intonatinal phrases and metrical grid.
* **Syntactic Analysis** - tree parser. 
* **Semantic Analysis** - predicate logic.
* **Discourse Analysis** - 
* **Pragmatic Analysis** - what type of stars? celestial, celebrities, 
  deals with context.
* **NLP Issues** - very ambiguous.
* **Parsing** - can be regarded as a search problem, top down/bottom up.
* **Context Free Grammar** - can apply rules without looking at whats nearby.
* **Context Free Grammar Issues** - inadequate, context sensitive are hard to write.
* **Top Down Parsing** - start with sentence, tries to split into single spots.
* **Bottom Up Parsing** - start with words, try to form sentence.
* **Chart Parsing** - bottom up, deals with edges in chart.

## 11-3 Vision
* **Low-Level** - edges, textures, color, optic flow.
* **Mid-Level** - grouping, segmentation.
* **High-Level** - reconstruction.
* **Edge Detection** - discontinuity in brightness, gradients in brightness.
* **Gaussian Convolution** - averages of neighbors, used for smoothing.
* **Edge in 2D** - take gradient instead of derivative.
* **Contours** - edges can be formed into contours, brain loves this.
* **Texture** - distribution of orientation, form continuous regions.
* **Optic Flow** - plot how image moves over time, velocity vectors.
* **Recognition** - illumination, orientation, rotation, then feature classifier.
* **Non Maximal Surpression** - tells where eyes are on a face.
* **Histogram of Orientations (HOG)** - counts number horizontal, vertical lines,
  good for images with small number of objects.
* **Occlusion** - cup rotated has no handle.

## 11-3 Robotics
* **Industrial Robots** - highly accurate, but highly constrained, uses offline
  computations.
* **AI Robots** - interacts with environment, on-board computation, delivery etc.
* **Asimov Laws** - dont harm humans, dont disobey humans, dont harm yourself.
* **Robotic System** - controller, body, environment.
* **Controller/Body** - takes in perception from body, gives body commands.
* **Body/Environment** - environment gives body stimuli, gets actions from body.
* **Sensors** - touch, vision, infared, chemical.
* **Actuators** - wheels, arms, weapons.
* **Simulation/Embedded** - train in simulation.
* **Optimization vs Learning** - energy usage and exploration.
* **Layered Control** - delivery robot represented in layers of actions.

## 11-10 Subsymbolic AI
* **Subsymbolic Processing** - NN breaks apart symbols.
* **Symbolic Cognitive Models** - knowledge structures to represent knowledge.
* **Boris/Cynrus/Soar** - symbolic cognitive models are powerful when specific,
  don't learn, not robust.
* **Distributed Neural Network Models** - no reason, just reaction - similar to
  humans, correlations with past experiences.
* **Symbolic Representation** - are discrete, disjoint, grammatical, compositional, reason
* **Subsymbolic Representation** - messier, data items are different patterns of activity,
  reaction.
* **Continuous** - fuzzy information.
* **Descriptive** - similar items are similarly represented.
* **Holographic** - any part contains information of the whole.
* **Conscious Rule Application** - symbol systems, approximate answer.
* **Intuitive Processing** - no rules, correlation with past answers with future questions.
* **Symbolic Behavior** - conscious rule is just subsymbolic in disguise.
* **SPEC** - sequential parser network, agent-act-patient structure, RAAM+stack+segementer.
* **RAAM** recursive auto-associative memory, encodes a stack.
* **Dynamic Inference** - bring together difference contexts, use segmenter.
* **Segmenter Network** - removes stuff already read, uses transition words.
* **SPEC Error** - with noise, SPEC has difficulty remembering earlier words.
* **Segantic Effects** - train data with semantic restrictions (only cats get chased).
* **Challenges** - approximate rule like reasoning, deep embeddings.

# 11-10  Model of Schizophrenia
* **Delusions** - self is inserted into impersonal stories.
* **Topic Switching** - a sentence has loosely connected topics.
* **DISCERN** - neural network-based model of human story processing.
* **Script** - story chunk (i went to restaurant, ...).
* **Story Parser** - translates a string of sentences into the slot filler representation 
  of a script.
* **Story Generator** - retrieves one script at a time from episodic memory, turns into sentences.
* **Memory Cue** - is a transition to one script to another.
* **Personal Stories** - go to wedding, eat dinner.
* **Gangster Stories** - bomb city hall, movie scenes.
* **Self Character** - schizophrenics put self into gangster stories.
* **Semantic Memory Lesions** - loose associations.
* **Hyper-Priming** - disorganized speech is caused b  activation in semantic maps that spreads.
* **Semantic Noise** - distort lexicon output with noise.
* **Semantic Overactivation** - increase the output activations of the lexicon.
* **Working Memory Disconnection** - connections cut between context layer connections.
* **Working Memory Noise** - distort context layer activation with noise.
* **Working Model Gain Change** - changing hidden layer sigmoid slope.
* **Excessive Arousal State** - increase hidden layer bias.
* **Hyperlearning** - accelerated memory consolidation, overly intense training, caused schizophrenia.
* **Experiment I** - tell short stories, judge on recall, derailments, agency shift, lexical errors.
* **Experiment II** - psychotics, grammar is still okay, DISCERN has good hyperlearning schizophrenia.
* **Derailments** - hyperlearning in memory encoder causes rapid context switches.

# 11-17 Evolving Neural Networks
* **Neural Nets** - powerful where no good theory of domain exists.
* **Reinforcement Learning** - difficult with large/continuous/hidden states.
* **Function Approximator** - generalized estimator for large states.
* **Neuroevolution** - direct nonlinear mapping from sensors to actions, has bias node, search space too big.
* **Advantages** - NE 3 orders of magnitude faster than RL for pole balancing.
* **Conventional Neuroevolution** - concat weight nodes into chromosome.
* **Genotype** - one kind of neural network, a score gets assigned to this.
* **Genetic Algorithm** - cross fit genotypes, add mutations, diversity is good.
* **Problems with CNE** - local optimals get focused on, convergent stagnates progress, too many weight nodes.
* **NEAT** - neural evolution of augmenting topologies, mutations add nodes and connections.
* **Complexify** - add mutations to NN, makes search  more manageable, incremental construction.
* **Lamarckian Evolution** - traits acquired can be passed to children, possible in NN, difficuilt to implement
  as diversity is reduced, progress stagnates.
* **Baldwin Effect** - learning selects promising invididuals.
* **Evolving Novelty** - picbreeder, humans are fitness functions, choose images to be evolved.
* **Fitness-Based Evolution** - rigid, gradual process, may find local max.
* **Novelty-Based Evolution** - new, innovative, often finds different but best solution.
