## 10-20 Knowledge Representation
* **Slot-filler Structures** - way to model logic with hiearchy.
* **Semantic Nets** - weak, visual, not very accurate though, allows inheritance
  can have contradictions, nodes - concepts, arcs - relationships.
* **Subtleties** - to represent binary relationships, use isa by
  passing an instance. have to specify properties of a set, or properties 
  of an instance
* **Event** - every event is an instance.
* **GS** - general statement.
* **Quantifiers** - instance is one link, for all is link to all nodes.
* **Intersection Search** - propagate two nodes, finds path to intersection which is
  the relation between the two.
* **Spreading Activation** - weighted sums of activity values, weight of relations
* **Marker Passing** - two activations that meet at a certain node can have different meaning.
* **Semantic Networks Disadvantages** - huge networks with many paths, 
  need to learn how to scale up.
* **Frames** - machine readable form more structure in nodes, collection of slots (attributes),
  constraints, list of lists, just a class system, more structure.
* **Frame System** - slots filled with other frames.
* **Is A** - subset.
* **Instance** - single individual.
* **Slot** - constrained by attributes, (default, inverse, single valued).
* **Frame Languages** - FRL, KRL, KL-ONE, KRYPTON.
* **Frame Issues** - quantifications, disjunctions, not good for deep deductions, 
  only good when structures are fixed and shallow.
* **Inheritance** - Frames good at inheritance, but not at ostrich, bird => fly or not fly.
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
* **Morphological Analysis** - in english, order matters, but other languages,
  have inflections, can add things to words and it'll change meanings. in finnish,
  one word can 10,000 ways to say it.
* **Morphophonology** - grouping of speech.
* **Prosodic** - intonatinal phrases and metrical grid.
* **Syntactic Analysis** - tree parser. 
* **Semantic Analysis** - predicate logic, word meaning to give the meaning of the sentence.
* **Pragmatic Analysis** - the little star and the big star, what type of stars? 
  celestial, celebrities, deals with context, sentences in different context.
* **Discourse Analysis** - the little star and the big star, two different objects,
  "the" lets you knows there is something new, combine sentences in context.
* **World Analysis** - world knowledge, common sense knowledge, implicit assumptions.
* **NLP Issues** - very ambiguous, all about solving ambiguity.
* **Phonological Issues** - things sound the same.
* **Syntactic Issues** - I shot an elephant in my pajamas.
* **Parsing** - can be regarded as a search problem, top down/bottom up, how to form
  tree from input. grammar, lexicon, parser.
* **Context Free Grammar** - simple, can apply rules without looking at whats nearby.
* **Context Free Grammar Issues** - inadequate, but context sensitive are hard to write.
* **Top Down Parsing** - start with sentence, tries to split into single spots.
* **Bottom Up Parsing** - start with words, try to form sentence, better than top down.
* **Chart Parsing** - bottom up, deals with edges in chart, vertices, position between words,
  edges represent constituents between vertices, faster, flexible, visualization.
* **Semantic Grammar** - the meaning is the parse result and result of actions.
* **Semantic Grammar Advantages** - result is immediately usable, ambiguities resolved using
  semantic info, syntax can be overridden.
* **Semantic Grammer Disadvantages** - lots of rules, slow, not a general model, but it is
  a practical approach that works.
* **Discourse Processing** - understanding language in context, sentence and later paragraph.
* **Anaphora** - Bill had a blue balloon. John wanted it. 
* **World Knowledge** - Sue opened the book she bought. The title page was worn. Books have title
  pages.
* **Implicit Assumptions** - Did Joe fail CS101? Joe is a a student, CS101 is hard.
* **Pragmatics** - It sure is cold in here. Means do something about it.
* **Axiomization of Communication** - to inform manes you believe it and believe someone else believes.
* **Sincerity of Request** - Can you open the door?
* **Reasonable of Request** - Why do you want it open?
* **Discourse Relation Theory** - Enumerates steps a sentence can have.
* **Narration** - events happen one after another, keep track of whats happening.
* **Elaboration** - sentences one after another describe each other.
* **Continuation** - last two events are related, and current event describes first one, the current
  event continues the second one.
* **Explanation** - the event in B caused event in A.
* **Commentary** - John and Mary are getting married. That is exciting news.
* **Reverse Relation** - Stylistic reasons, Max was sick. He took aspirin.

## 10-27 Rule Base and Expert Systems
* **Ruled Based Systems** - logical reasoning with lots of knowledge.
* **Forward Chaining** - situational, input-driven, populate database.
* **Backward Chaining** - goal directed, answer questions.
* **Production Systems** - formalization of rule based system, global database,
  how to run rules.
* **Expert Systems** - are production systems, require expert systems, 
  propogate knowledge.
* **Prolog** - everything is run by DFS.
* **Execution** - setup, see if terminates, if not apply rule.
* **Ways to Speedup** - monotonic, commutative, decomposable.
* **Matching** - thousands of rules, cant go through all, but sometimes a match
  is not exact.
* **Conflict Resolution** - if we have several rules, which do we apply?
* **Rule-Directed** - rules have numbers, higher priority has more chance,
  more specific come first.
* **Object-Directed** - short term memory over long term, importance of objects matched.
* **State-Directed** - apply all, best result is selected, best first search.
* **Metaknowledge** - rules, macros to be more efficient in solving problems.
* **SOAR** - forms macros, builds a library of how to solve problems, how to use the rules.
* **Expert Systems** - solve problems normally solved by human experts, easier to build 
  compared to common sense.
* **General Knowledge Baes** - rules and facts about domain, long term facts.
* **Inference Engine** - applies rules to knowledge, tries to find conclusion.
* **Case-Specific Knowledge** - facts, conclusions, confidence 
* **Explanation Subsystem** - tells how it derived the solution.
* **Vs Sub-Symbolic** - good since it gives an explanation vs neural networks, you want to
  know how the system diagnosed the patient.
* **Walkthrough** - presented a problem, expert system applies rules, if it needs more info,
  queries the user.
* **Expert System Shell** - Watson, takes the whole process and sells the shell minus the data.
* **EMYCIN** - medicinal diagnosis system.
* **XCON** - configure other machines, originally for VAX machines.
* **Knowledge Acquisition** - hard part, composed of domain expert, knowledge engineer, end user.
* **Domain Expert** - person who really knows the domain, but is biased, and knowledge can change.
* **Knowledge Engineer** - helps build conceptual model, and how rules look like.
* **MOLE** - prompts, symptoms and causes, tries to tie together, checks for errors, completeness,
  can allow user to refine by trying to solve problems.
* **Explanation** - an explanation is just following the rule chain, generation easy, understanding hard.
* **PROSPECTOR** - advice on mineral exploration.
* **Evaluation of MYCIN** - hard to prove correctness, beat human experts, cannot reason 
  about other fields, doesn't know limits of its reasoning.

## 10-27 Uncertainty
* **Uncertainty** - knowledge changes.
* **Nonmonotonic** - believe to be T/F.
* **Nonmonotnoic Reasoning** - three truth values, believed, disbelieved, unknown. When
  new facts are added, facts must be rechecked.
* **Nonmonotonic Logic** - first order predicate logic, with operator M "is consistent".
* **Undecidability** - first order predicate logic is semidecidable.
* **Abduction** - turn key => car starts, car starts so turn key, but could be wrong.
* **Formalization** - (a => b) and b and M(a) => a
* **Inheritance** - bird => flies, penguins => not flies, penguins => bird. this is a contradiction.
* **NM Inheritance** - if bird and not abnormal => flies, compact way to do inheritance
  without contradictions.
* **Truth Maintenence/TMS** - uses dependency-directed backtracking, tries to schedule day for tuesday,
  cant do it, try wednesday, succeeds.
* **Justification-Based TMS** - each assertion has a justification, IN means believed, OUT no good reason
  to believe. Justification is nonmonotonic if OUT is not empty, any in IN is nonmonotonic.
* **JTMS Problems** - hard to code, very complex, 
* **Statistical Reasoning** - degree of belief and belief update.
* **Bayesian Inference** - based on conditional probabilities, with incremental updates.
* **Bayesian Problems** - too many joint probabilities needed o(2^n) with n events, makes
  assumptions and represents ignorance.
* **Certainty Factor** - measure of belief - measure of disbelief, provided by experts. MYCIN uses this.
* **Problems** - confusing causual and evidential support.
* **Bayesian Network** - DAG, nodes represent hypothesis, arcs stand for direct causual influence.
  joint distribution function.
* **Belief Propogation** - data comes up from leaves and propogates down to other branches as 
  causal support.
* **Problems** - loops, sometimes we cant just have independent assumptions, computationally extensive.
* **Fuzzy Logic** - continuously valued logic, possibility of belonging. Seriously ill,
  combinations of restraints.

## 11-3 Vision
* **Low-Level** - edges, textures, color, optic flow.
* **Mid-Level** - grouping, segmentation.
* **High-Level** - reconstruction
* **Edge Detection** - discontinuity in brightness, gradients in brightness.
* **Gaussian Convolution** - averages of neighbors, used for smoothing, can combine
  two steps in one.
* **Edge in 2D** - take gradient instead of derivative.
* **Contours** - edges can be formed into contours, brain loves this, tend to be
  colinear or cocircular, probability of edge based on angle and distance.
* **Texture** - distribution of orientation and its formation of continuous regions.
* **Image Segmentation** - brightness, color, texture.
* **Optic Flow** - recognizing movement, plot how image moves over time, velocity vectors.
* **Recognition** - illumination, orientation, rotation, then feature classifier.
* **Non Maximal Surpression** - tells where feature classifier fired.
* **Histogram of Gradient Orientations (HOG)** - counts number horizontal, vertical lines,
  good for images with small number of objects.
* **HOG Problems** - perspective, aspect, occlusion, articulated objects.
* **Foreshortening** - object at angle looks shorter.
* **Aspect** - ring rotated looks like a line.
* **Deformation** - person can look different if his arm is up.
* **Occlusion** - cup rotated has no handle.
* **High-Level** - requires significant world knowledge, works best with good models, sigificant
  data and machine learning.
* **Stengths and Weaknesses** - can do very specific things like manufactoring but is poor in 
  very general cases.

## 11-3 Robotics
* **Industrial Robots** - highly accurate, but highly constrained, uses offline computations.
* **AI Robots** - interacts with environment, on-board computation, delivery etc.
* **Asimov Laws** - dont harm humans, dont disobey humans, dont harm yourself.
* **Robotic System** - controller (brain), body, environment (interacted with by body).
* **Controller/Body** - takes in perception from body, gives body commands.
* **Body/Environment** - environment gives body stimuli, gets actions from body.
* **Sensors** - touch, vision, infared, chemical.
* **Actuators** - wheels, arms, weapons.
* **Simulation/Embedded** - train in simulation, we can train without breaking robot.
* **Optimization vs Learning** - optimize for energy usage or exploration to learn more, learning
  should occur offline.
* **Layered Control** - delivery robot represented in layers of actions.
* **Low Level Layered Control** - change angles of arms.
* **Mid Level Layered Control** - see where to go without colliding, full body control.
* **High Level Layered Control** - planner, have a high level idea of what its actions are.
* **Modeling the World** - see where you are in the world, see what you can do, error accumulates
  and should be corrected.
* **Active Perception** - predict what happens, find error, correct error.

## 11-10 Subsymbolic AI
* **Cognitive Modeling Goals** - take over routine and dangerous tasks.
* **Example Areas** - natural language, memory, perception, problem solving, computational model.
* **Computational Model** - write cote to represent model to test theories, predictions.
* **Subsymbolic Processing** - NN breaks apart symbols.
* **Symbolic Cognitive Models** - knowledge structures to represent knowledge, requires a lot of
  human input (frames, semantic networks), big in the 1980s.
* **Boris/Cyrus/Soar** - symbolic cognitive models are powerful when specific, but don't learn,
  not robust, learns similar how humans learn.
* **Soar** - chunking, making macros, making expert systems that are cognitive, make same
  inferences as humans make, makes inferences that are cognitively valid.
* **Distributed Neural Network Models** - no reason, just reaction - similar to humans, 
  correlations with past experiences, no explicit rules, biologically inspired.
* **Symbolic Representation** - are discrete, disjoint, grammatical, compositional, reason.
* **Subsymbolic Representation** - messier, data items are different patterns of activity, reaction,
  patterns of activation.
* **Continuous** - fuzzy information.
* **Descriptive** - similar items are similarly represented.
* **Holographic** - any part contains information of the whole.
* **Conscious Rule Application** - symbol systems, approximate answer.
* **Intuitive Processing** - no rules, correlation with past answers with future questions,
  for intuition cognition, subsymbolic systems are better.
* **Symbolic Behavior** - conscious rule is just subsymbolic in disguise.
* **SPEC** - sequential parser network, agent-act-patient structure, RAAM+stack+segmenter.
* **External Memory Network** - sub symbolic memory, copies input to output, stack represented
  in the hidden layer, breaks when you put too many things in.
* **RAAM** recursive auto-associative memory, encodes a stack.
* **Dynamic Inference** - bring together difference contexts, use segmenter, difficult for network.
* **Segmenter Network** - global view of parsing process, removes stuff already read, 
  uses transition words, in the middle of the system.
* **Parsing** - 3 subtasks, case-role interpretation (hows words work together), memory (save objects),
  controller (uses memory in right way)
* **Training** - from 2 types of sentences, can generalize to 49 types. Optimizations include
  tail recursion. Performes like a human, limited by memory.
* **SPEC Error** - with noise, SPEC has difficulty remembering earlier words, makes plausible guesses.
* **Performance Errors** - add noise to stack to elicit errors in memory.
* **Semantic Effects** - train data with semantic restrictions (only cats get chased), allows it
  to be easier to remember, prefers words earlier in sentence.
* **Challenges** - approximate rule like reasoning, deep embeddings.
* **Subsymbolic Models** - encode soft constraints, can approximate intuition (easy), can approximate
  rule-like reasoning (hard).

# 11-10  Model of Schizophrenia
* **Delusions** - self is inserted into impersonal stories.
* **Topic Switching** - a sentence has loosely connected topics.
* **DISCERN** - neural network-based model of human story processing, remembers and paraphrases.
* **Script** - story chunk (i went to restaurant, ...), sequence of events.
* **Slot Filler** - pulled over I cop arrest(ed) DUI.
* **Emotion Code** - how positive or negative a line in a script is.
* **Sentence Parser** - translates string of word representations, goes to story parser.
* **Story Parser** - translates a string of sentences into the slot filler representation of a script.
* **Memory Encoder** - adds a memory cue to each script.
* **Story Generator** - retrieves one script at a time from episodic memory, turns into sentences.
* **Output Filter** - included in story generator, prunes overly distorted sentences.
* **Memory Cue** - is a transition to one script to another.
* **Personal Stories** - go to wedding, eat dinner.
* **Gangster Stories** - bomb city hall, movie scenes.
* **Self Character** - schizophrenics put self into gangster stories.
* **Semantic Memory Lesions** - loose associations, associations with random things, activation that
  spreads too fast, too far.
* **Hyper-Priming Hypothesis** - disorganized speech is caused by activation in semantic maps that spreads.
* **Semantic Blurring Hypothesis** - mixing neighboring word representations, lexicon.
* **Semantic Noise** - distort lexicon output with noise.
* **Semantic Overactivation** - increase the output activations of the lexicon.
* **Working Memory Disconnection** - connections cut between context layer connections.
* **Working Memory Noise** - distort context layer activation with noise.
* **Working Model Gain Change** - changing hidden layer sigmoid slope.
* **Working Model Excessive Arousal State** - increase hidden-layer bias.
* **Hyperlearning** - accelerated memory consolidation, overly intense training, caused schizophrenia,
  interesting because this symptom was discovered from the model.
* **Salience** - cannot distinguish what is important - everything looks important, develops psychosis.
* **Experiment I** - tell short stories, judge on recall, derailments, agency shift, lexical errors.
* **Important Outcome Variables** - recall performance, agency shifts, lexical errors, derailments.
* **Experiment I Results** - hyperlearning was able to match schizophrenic language the best.
* **Experiment II** - psychotics, a lot of delusions and derailments, but grammar is still okay, 
  DISCERN has good hyperlearning schizophrenia.
* **Distorted Language** - when WM noise is added, a lot of weird words come out, words dont make sense,
  schizophrenics dont actually say these things.
* **Delusion** - DISCERN adds "I" into a lot of gangster stories.
* **Derailments** - 90% of delrailments are to stories with same emotion, in hyperlearning,
  hyperlearning in memory encoder causes rapid context switches.
* **Medication Effects** - future work, to similate transition between two states to help recovery,
  antipsychotic medication reduces symptoms by slowing memory consolidation, test by looking for hyperlearning.

# 11-17 Evolving Neural Networks
* **Neural Nets** - powerful where no good theory of domain exists, statistical domains.
* **Reinforcement Learning** - difficult with large/continuous/hidden states.
* **Function Approximator** - generalized estimator for large states.
* **Neuroevolution** - direct nonlinear mapping from sensors to actions, has bias node, search space too big,
  can be recurrent, takes in past actions into account, hidden states are disambiguated through memory.
* **Advantages** - NE 3 orders of magnitude faster than RL for pole balancing, only method to solve two poles,
  powerful method for sequential decision tasks, optimize existing, discover novel solutions.
* **Advantages in Supervised Tasks** - good when network topology is important.
* **Input Variables** - state observed through sensors.
* **Output Variables** - actions determed by hidden layer.
* **Conventional Neuroevolution** - concat weight nodes into chromosome.
* **Chromosome** - strings of connection weights.
* **Genotype** - one kind of neural network, a score gets assigned to this.
* **Genetic Algorithm** - cross fit genotypes, add mutations, diversity is good, parallel search for optimal,
  taking piece of network and cross with another network.
* **Problems with CNE** - local optimals get focused on, convergenging populations stagnates progress,
  too many weight nodes (parameter) to be optimized simultaneously.
* **NEAT** - neural evolution of augmenting topologies, mutations add nodes and connections, elaborates
  on earlier behaviors, start with simple networks, no hidden nodes.
* **Complexify** - add mutations to networks, recurrent nodes, makes search more manageable, 
  by using incremental construction.
* **Lamarckian Evolution** - traits acquired can be passed to children, possible in NN, difficult to implement
  as diversity is reduced from backprop to do the same thing, progress stagnates.
* **Baldwin Effect** - learning selects promising invididuals, learning makes it more likely to
  find optimal.
* **Evolving Novelty** - picbreeder, humans are fitness functions, choose images to be evolved.
* **Fitness-Based Evolution** - rigid, gradual process, may find local max.
* **Novelty-Based Evolution** - new, innovative, often finds different but best solution, reward evolution
  for producing new, novel things.
* **Applications to Control** - pole-balancing benchmark, good surrogate for other tasks, like driving,
  controlling a finless rocket.
* **Simulation Environment** - general rocket simulator, models interactions between airframe, propulsion,
  aerodynamics, and atmosphere.
* **Control Policy** - shows how rocket is controlled along the journey.
* **Applications to Robotics** - controlling robot arm, walking, mobile robots.
* **Symmetry Evolution Approach for Multilegged Walking** - neural networks in each leg talk to each other.
* **Applications to Artificial Life** - try to learn how complex behaviors are learned in animals society.
* **Body-Brain Coevolution** - evolved virtual creatures that evolve together, they have "natural" behavior.
* **Pandemonium** - two opposite actions, highest trigger wins.
* **Evolving Flight or Fight** - evolves attack or retreat, then combines the both.
* **Stengths** - effective in continous, non-markov domains, sequential decision tasks. If you can simulate the
  problem, can find a solution, easy to adapt.

# 11-17 AI in Video Games
* **Real World Problems** - real world is complex, open ended, messy. Scale up is impractical, even dangerous.
* **Video Game Strengths** - virtual worlds are sophisticated but still controlled, formal, measurable, safe.
* **Video Game Successes** - Deep Blue, Chinook, but are largely brute force.
* **GOFAI** - based on search, A\* pathfinding as finite state machines, does not work well in video games
  because board games don't have multiple agents, embbeded, continous, noisy, large-dimensional, real time.
* **Computational Intelligence** - inspired by biology, is neural nets, evolution, reinforcement learning,
  powerful in pattern recognition, control. Good when its hard to form rules but have lots of data.
* **Neural Network Agents** - need memory to track past encounters.
* **Othello Strategies** - evolved against a alpha-beta program and won.
* **Neuroevolution Strength** - discovered novel strategies, works by tinkering.
* **Challenge of Evolving Multimodal Behavior** - many different tasks, how can we solve them in a single network?
* **Evolving Multimodal Behavior** - evolve separate neural networks, let the network decide when to use.
* **Evolution Discovered Task Division** - the network decides what task to do, how to do the task.
* **Challenge of Humanlike Behavior** - Botprize competition, decide who is human and who is computer.
* **Humanlike Behavior** - have to limit it with human like limitations, cannot undestand traps though.
* **NERO** - machine learning games, goal to show games are viable, real time, open-ended, requires discovery.
* **Neuroevolution Strength** - strong method for adaptation in games, adapts in real time, applications 
  are huge, entertainment, training simulators, robotics, resource optimizations intelligent assistants.
* **Neuroevolution Weakness** - requires many evaluations, best when parallel evaluations possible,
  best when combined with human guidance (examples or rules).
