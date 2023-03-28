---
title: Evolutionary stable correlation as a core problem of social ontology
author: Valerii Shevchenko
affiliation: HSE University
abstract: 
keywords: Social ontology, evolutionary game theory
---

# Evolutionary stable correlation as a core problem of social ontology

## Introduction
In this paper, I argue that the emergence of evolutionary stable correlation is the core issue of naturalistic social ontology. According to rules-in-equilibria theory, social institutions are the central unit of social ontology [@guala2016b], and coordination is its main mechanism rooted in evolution [@shevchenko2023]. As institutions are normatively-driven self-sustaining behavioral regularities designed to solve coordination problems [@aoki2007], they share many features with 'animal conventions' that help animals solve coordination problems and maintain stable relationships [@hindriks2015]. Consequently, understanding the emergence of social institutions requires an examination of the evolutionary mechanisms that enable correlation of strategies with normative force as a key characteristic.

To expand, let us first look at Guala's [-@guala2016b] argument that has the following logic:

1. social institutions are backed not by constitutive rules of the form "X counts as Y in (the context of) C", like in Searle [-@searle1995],[^1] but by regulative rules of the form "do X if Y"
2. from a game-theoretic point of view, regulative rules can be seen as agents' strategies that comprise a *correlated equilibrium*[^2]
3. constitutive rules are linguistically transformed regulative rules with added theoretical term that represents a certain equilibrium
4. at the same time, many animal species including baboons, lions, swallowtails, and others exhibit behavioral patterns describable in the form of correlated equilibrium, as well [@maynardsmith1982]
5. despite the similarity of mathematical representation, the cases of 'animal conventions' and human social institutions differ in scope of actionable signals. Building on Sterelny [-@sterelny2003], Guala puts for forward an idea that humans can invent and follow new rules, whereas animals are bound to genetically inherited sets of behavioral responses
6. the arbitrariness of rules that humans can invent and follow is grounded in and ontologically depends on shared representations of a given community
7. put differently, the difference in scope of actionable signals between animals and humans can be explained by humans having social epistemology that grounds social ontology.

Although sound, this argument has an Achilles heel: the evolutionary roots of correlation of strategies as the basis of any self-sustaining social coordination, human or not, are still obscure and underdeveloped.

Guala and Hindriks base their account on Maynard Smith's, who does not use the notion of correlated eqiulibrium explicitly and discusses what he calls a *bourgeois equilibrium* — a situation in animal territorial behavior, when the most optimal strategy for an animal is to fight for a territory it "owns" it or not fight otherwise. This game is represented in the matrix below.

\begin{table}[h]
\centering
\begin{tabular}{|l|c|c|c|}
\hline
& \textbf{Hawk} & \textbf{Dove} & \textbf{Bourgeois} \\ \hline
\textbf{Hawk} & $\frac{(V-C)}{2}$, $\frac{(V-C)}{2}$ & $V$, $0$ & $\frac{(V-C)}{2}$, $V-C$ \\ \hline
\textbf{Dove} & $0$, $V$ & $\frac{V}{2}$, $\frac{V}{2}$ & $0$, $\frac{V}{2}$ \\ \hline
\textbf{Bourgeois} & $C-V$, $\frac{(C-V)}{2}$ & $\frac{(C-V)}{2}$, $C-V$ & $\frac{(C-V)}{2}$, $\frac{(C-V)}{2}$ \\ \hline
\end{tabular}
\caption{\small A game-theoretic matrix for a "hawk-dove-bourgeois" game from Maynard Smith's book "Evolution and theory of games". In this game, two players (represented by rows and columns) can choose to be either a hawk (fight for resources), dove (submit and share resources), or bourgeois (submit only when opponent is also bourgeois). The payoffs are determined by the value of the resource (V) and the cost of fighting (C). The table shows the payoff for each player given their own strategy and their opponent's strategy.}
\end{table}

Guala and Hindriks interpret bourgeois equilibrium as a correlated one. However, there are at least two interpretations of it: *correlated equilibrium* and *evolutionary stable strategy* (ESS)[^3] based on uncorrelated asymmetry. They are mathematically distinct, and we will look at both in detail later.

The presented ambiguity creates tension at the backbone of Guala's argument. It means that:

- either 'animal conventions' are mathematically different from human social institutions, for they represent ESS and not correlated equilibrium, and there comes the burden of showing how the former becomes the latter in the course of evolution;
- or that 'animal conventions' are themselves correlated, and there comes the burden of showing how humans acquired the capacity for social epistemology that ontologically grounds social ontology as rules-in-equilibria.

Taking into account the wealth of research on transition from ESS to correlation in game theory [@skyrms1994; @lee-penagos2016; @kim2017; @metzger2018; @herrmann2021], the first option in resolving the tension in Guala's argument becomes insufficient. The transition from ESS to correlation does not intrinsically presuppose the emergence of intentional compliance to norms, as in social institutions, which are normatively-driven and at the same time arbitrary, as will be covered later. Consequently, it will be needed to account for the second option, but to begin, we need to figure out whether social institutions indeed necessitate correlation of strategies. In this paper, I will address the source of the issue—Maynard Smith's notion of bourgeois equilibrium and its interpretations in regard to social coordination.

It is relevant, for if social institutions have emerged from 'animal conventions' with the aid of cognitive capacities like mindreading and/or mindshaping [@zawidzki2013], it constrains social ontology as the scope of possible objects of study to the logical derivatives of social institutions and social coordination in general as discussed in @shevchenko2023.

This paper is structured as follows. First, it discusses the relationship between social institutions, conventions, and norms, and how conventions emerge through Skyrms's deliberational dynamics and Harms's evolutionary functionalism. Second, it examines the correlation and asymmetry of strategies in the emergence of social institutions and explains what correlated equilibrium and uncorrelated asymmetry mean. Two views on correlation versus asymmetry are also discussed. Third, the paper explores the problem with correlation in social institutions as evolved correlated equilibria. It analyzes Guala's argument about the difference in scope of actionable signals in animals versus humans and Skyrms's interpretation of Maynard Smith's “bourgeois” concept. Fourth, it delves into the tension between bourgeois and correlated equilibria with a formal distinction between mixed strategy and correlated equilibria, as well as addressing where randomization of strategies comes from. Let us start with the notion of social institutions, move backwards by destructuring it into norms and conventions, study their relations and then gradually arrive at the issue of coordination either by correlation or by asymmetry of strategies. 

## Institutions vs. norms vs. conventions
According to @guala2016b, institutions are rules-in-equilibria, normatively-driven behavioral regularities represented as correlated equilibria. “Rules” here are the recipes guiding and prescribing certain behavior and are *used by the agents themselves*, and ”equilibria” are objective stable states of the strategic interaction between agents and population thereof. Other scholars pinpoint normative and self-sustaining nature of institutions. They are "humanly devised constraints that shape human interactions" [@north1990], "norm-governed social practices" [@tuomela2013] and "self-sustaining salient behavioral patterns" [@aoki2007]. It can be seen that institutions combine "subjective" and "objective" components: they are driven by social norms, that might vary from one population to another, and, at the same time, constrain possible actions and sustain itself.

If social norms are inherently important to institutions, what are they, and how do they differ from social institutions? According to @bicchieri2005, social norms are shared expectations, or "rules", about how people should behave in a given context. These expectations can be either prescriptive, telling individuals what they ought to do, or descriptive, reflecting what most people actually do. Social norms can be modeled as a set of rules or constraints that guide individual behavior. For example, let $X$ be the set of all possible behaviors that an individual can choose from in a given situation. A social norm $N$ can then be represented as a subset of $X$ that specifies which behaviors are considered acceptable or desirable by the group: $N \subseteq X$. The power of social norms lies in their ability to shape behavior without the need for formal enforcement mechanisms like laws or explicit regulations. Individuals often conform to social norms because they want to fit in and be accepted by their peers, or because they believe that following the norm is the right thing to do. Thus, norms are shared expectations about behavior in certain situations and institutions are behavioral patterns that are governed by such shared expectations.

The further required distinction to be made is that of institutions, norms, and conventions. But what are conventions in the first place? @lewis2008 defines conventions as regularities in behavior that are mutually expected and mutually beneficial for the agents involved. In other words, conventions are shared expectations about behavior that result in cooperative outcomes. To illustrate this concept, Lewis uses the example of driving on the right or left side of the road. This convention is mutually expected because everyone understands that it is necessary for traffic to flow smoothly and avoid accidents. It is also mutually beneficial because if everyone follows the convention, then there is a reduced risk of accidents and delays. Lewis also distinguishes between two types of conventions: coordination conventions and strategic conventions. Coordination conventions are those where agents need to coordinate their actions to achieve a common goal, such as deciding which side of the road to drive on. Strategic conventions are those where agents need to make strategic choices based on what they expect others to do, such as deciding whether to use a turn signal while driving.

For example, consider the following coordination game:

\begin{center}
\begin{tabular}{|c|c|c|}
\hline
& Drive on left & Drive on right \\
\hline
Drive on left & (1,1) & (-1,-1) \\
\hline
Drive on right & (-1,-1) & (1,1) \\
\hline
\end{tabular}
\end{center}

In this game, two drivers must choose whether to drive on the left or right side of the road. The payoffs indicate how well each driver does depending on their choice and their partner's choice. If both drivers choose the same side (either both drive on the left or both drive on the right), they each receive a payoff of $1$. If they choose different sides (one drives on the left while the other drives on the right), they each receive a payoff of $-1$. This game has two pure strategy Nash equilibria:[^4] both drivers driving on the left or both driving on the right. In other words, if both drivers follow these conventions, they will achieve a mutually beneficial outcome. Lewis argues that conventions can emerge in situations like this through repeated interactions between agents who learn to coordinate their behavior over time. As more people adopt a particular convention, it becomes more costly for others to deviate from it because they risk being penalized by their partners.

If conventions are mutually expected and mutually beneficial behavioral regularities, how are they different from both social norms and social institutions? O'Connor (2019) draws two crucial distinctions, namely between conventions and social norms, and between more and less arbitrary conventions. The initial distinction implies that not all behavioral regularities possess normative force, meaning that conventions and norms are not that the same. For instance, friends may have a convention of meeting every Friday evening at a bar, and failing to show up does not necessarily imply a violation of a norm. However, when two cars are driving in the same direction towards each other on the same side of the road, the drivers are compelled to swerve to avoid collision. Failing to do so may result in fines or even accidents; hence, swerving becomes an obligatory normative action.

Furthermore, as Bicchieri (2005) asserts, conventions differ from social norms in their association with self-interest and common interest. While they converge with self-interest, they do not necessarily coincide with common interest. In the case of friends gathering at a bar, there is minimal or no tension between self-interest and common interest; however, when driving cars on the road, there is an inherent tension between these interests. O'Connor notes that conventions and norms exist along a continuum, where conventions can acquire normative force based on their position on this spectrum.

The second distinction pertains to the arbitrary and historically contingent nature of conventions, with the recognition that they are subject to variation and could have been otherwise. This arbitrariness is a fundamental characteristic of conventions, as posited by Lewis. However, @gilbert1992 has critiqued Lewis's work, noting that not all potential resolutions to a coordination problem offer equal benefits for participants. Hence, where one mode of coordination is more desirable than another, conventionality is not entirely arbitrary. To put it differently, arbitrariness in the context of conventions illustrates a continuum ranging from contingency to necessity. For example, signaling among vervet monkeys may be construed as a convention in the Lewisian sense of recurrent behavioral patterns resolving coordination issues [cf. @harms2004; @skyrms2010]. Nevertheless, this conventionality is not historically contingent insofar as multiple solutions are equally remunerative since adaptive dynamics breaks the symmetry between equilibria. Agents may be genetically predisposed towards certain strategies. Some conventions as more functional and others as more arbitrary.

Putting this into a perspective:
- 'animal conventions' are more functional conventions where "normativity", if exists, is grounded in genetically inherited behavioral predispositions;
- social institutions are more arbitrary conventions where normativity is grounded in advanced cognitive capacities like mindreading

\begin{tikzpicture}
	\begin{axis}[
		title={},
		xlabel={},
		ylabel={},
		xmin=-1, xmax=1,
		ymin=-1, ymax=1,
		xtick={1}, xticklabels={Necessary, Arbitrary}, % Sets the tick labels from bottom to top
		ytick={1}, yticklabels={Genetically Inherited, Culturally Inherited}, % Sets the tick labels from left to right
		]
		 \addplot[only marks,mark size=3pt] coordinates {(-0.5, -0.5) (0.5, 0.5)}; % plot points
		 \addplot[mark=0,fill opacity=0.3] coordinates {(1,1) (2,2)}; % fill the area between points with opacity
		 \addplot[blue] coordinates {(1,0) (1,2)}; % vertical line from bottom to top
		 \addplot[blue] coordinates {(0,1) (2,1)}; % horizontal line from left to right
		 \node at (axis cs: -0.5,-0.5){Animal Conventions}; % name for first point
		 \node at (axis cs: 0.5, 0.5){Human Social Institutions}; % name for second point
	\end{axis}
\end{tikzpicture}

Essentially, social institutions are norm-driven conventions that require certain cognitive capacities which make recognition, complying to and changing of social norms possible. Two questions arise:

- if institutions are evolved 'animal conventions', how do the latter evolve themselves?
- do simple 'animal conventions' and social institutions evolve by the same evolutionary mechanism?

### Emergence of animal conventions

"Animal conventions" are behavioral regularities, where animals "know" how to behave. But how do they "know" that and how these were regularities established in the first place? @baraghith2019 compares game-theoretic and teleosemantic views on emergence of conventions as public meaning. His main claim is that theories of Skyrms [-@skyrms2010] and Millikan [-@millikan1987] share many aspects and can be synthesized to yield empirically testable and philosophically elaborated approach.

The author observes that signals, or public representations, become conventional by stabilization of a strategy profile in a Lewis signaling game, resulting in the emergence of behavioral regularities among involved agents. In other words, convention is generated by stabilization of a signaling system. According to Lewis, a signaling system is a *strict Nash equilibrium*[^5] of a signaling game.

One of the similarities in teleosemantic and signaling approaches is that evolution drives the emergence of successful coordination between agents, be it parts of an organism or different organisms. However, teleosemantic approach operates with the notion of a *function* [@millikan1987], whereas sender-receiver approach emphasizes *adaptive dynamics* by reinforcement learning [@skyrms2010].

In both approaches, conventions depend on their history and involve contingency. As Millikan [-@millikan2005, 29] puts it:

> “A convention is merely a pattern of behavior that is (1 ) handed down from one person, pair, or group of persons to others – the pattern is reproduced – and (2 ) is such that, if *the pattern has a function*, then it is not the only pattern that might have served that function about as well. Thus, if a different precedent had been set instead, a different pattern of behavior would probably have been handed down instead.”

As Baraghith notes, most criticism of teleosemantic view of the emergence of conventions has been that content—or representation of a world state by a sender—lacks explanation solely by its adaptive function or history. However, as Neander and Shea show, teleosemantics might solve the problem of mental content, intentionality, and thus, representation [@neander2008; @shea2018]. In its turn, sender-receiver approach has received criticism for being atomistic and not able to accommodate “mental life”—cases with agents having advanced cognitive capacities like midredaing [@sterelny2017].

Baraghith stresses the crucial difference between speaker meaning and public meaning. In other words, a convention as a signaling system involves two kinds of information: a representation of an observed world state by a sender, and a signal sent from sender to receiver. The former is internal, and the latter is external. Representation and signal are mental and behavioral parts of a representational system, respectively.

If a signaling system is a strategy profile of a signaling game, what is the latter? A signaling game represents a coordination problem between world states, signals and acts, which are associated probabilistically. The most simple case has two states $W=\{\sigma_{1,}\sigma_2\}$, two messages $M=\{m_{1,}m_2\}$ that a sender $S$ can transfer to a receiver $R$, and two acts $A=\{\alpha_1,\alpha_2\}$, by which $R$ can respond to a received signal. There are pure sender and receiver strategies. The former is a function $s: W\mapsto M$ from world states to signals, and the latter is a function $r: M \mapsto A$ from signals to acts. With two signals and two acts, both sender and receiver have 4 strategies each. Assuming that all strategies are equiprobable, 16 strategies are possible, from which only two are beneficial for both agents and constitute a strict NE.

%%in latex, draw an extensive form signaling game with two world states, two signals and two acts. mark strict Nash equilibria with arrows%%

\begin{tikzpicture}[node distance=2cm]
	\node (A) {$A$};
	\node (B) [right of=A] {$B$};

	\node (S1) [above of=A] {Signal 1};  
	\node (S2) [above of=B] {Signal 2};  

	\node (X1) [below left of=A] {$X_1$};  
	\node (Y1) [below right of=X1] {$Y_1$};

	\node (X2) [below left of=B] {$X_2$};  
	\node (Y2) [below right of=X2] {$Y_2$};

    % draw arrows between nodes: from each node to the next in the sequence
    % ... except for the last node which loops back to the first.

    % signal 1 -> A, B -> act 1, act 2 -> world state 1, world state 2
\draw[->] (S1) -- (A);
\draw[->] (B) -- (Y1);
\draw[->] (Y1) -- node[anchor=east,xshift=-0.25cm,yshift=-0.25cm] {\rotatebox{-45}{\tiny $\searrow $}}(X1);

    % signal 2 -> A, B -> act 1, act 2 -> world state 1, world state 2    
\draw[->] (S2) -- node[anchor=south west,xshift=-0.25cm,yshift=-0.25cm] {\rotatebox{45}{\tiny $\nearrow $}}(B);
\draw[->] (A) -- node[anchor=east,xshift=-0.25cm,yshift=-0.25cm] {\rotatebox{-45}{\tiny $\searrow $}}(X2);
\draw[->](Y2)--(X2);
		 % draw loop on last act/world state pair: Y --> X
 %\draw[->](Y)--(X);
		 % draw double arrows on Nash equilibria
\end{tikzpicture}

In an evolutionary perspective of Skyrms [-@skyrms2010], signaling systems are not strict Nash equilibria, but ESS. On this account, given an adaptive process that guides the behavior of agents, any signaling game iterated over time results in an ESS. Depending on initial conditions, population converges on one of the two signaling systems, what is often modeled with replicator dynamics.[^6]

Another detail of this approach is its connection to information theory. A signal $m_1$ carries information if it changes the probabilities of any world state. The information quantity is measured by how far the probability is moved, and information content—by direction of probability: increasing or decreasing. Franke and Wagner [-@franke2014] show the Bayesian likelihood of a world state $\sigma_i$ given a signal $m_j$: $$P(\sigma_i \mid m_j) = \frac{P(m_j \mid \sigma_i)\times{P(\sigma_i)}}{\sum_t P(m_j \mid \sigma_i)\times{P(\sigma_i)}}$$
It means that if state $\sigma_i$ occurs with prior probabilities $P(\sigma_i)$ and $P(m_{j}\mid \sigma_i)>0$, a signal $m_j$ is sent. Signals may initially contain no intrinsic meaning, and the dynamics does not require any sophisticated cognitive capacities of the agents. They do not need to have pre-existing mental language for a signaling system to be established [@skyrms2010, 7]. This makes sense in “animal conventions”, but not easily so in human ones. Thus, according to Skyrms' sender-receiver approach, convention is an ESS. It makes a lot of sense in “animal conventions”, but its application to human social institutions is not straightforward. As Huttegger puts it [-@huttegger2007, 413]:

> "There is at least one functional aspect of human languages that can fundamentally be expressed in terms of signaling systems: communication facilitates social coordination”.

However, it is not sufficient for evolutionary account of human social coordination resulting in social institutions.

Another important formal approach to the emergence of conventions is due to Harms [-@harms2004]. He synthesizes sender-receiver framework and Millikan's teleosemantics. According to this approach, any semantic convention, or “rule”, might be considered as a “function-stabilizing mechanism”. It helps to coordinate the behavior of different organisms or different parts of an organism to perform an evolutionary adapted biological function. Rules are sets of maps from conditions to processes one by one. They say what to happen next given a state of the world. Rules for evolutionary adapted traits (AT) might be expressed as
$$R_{AT}={\{\langle c_{i,}p_{i}\rangle} \mid AT \space sel \space p_{i}\space in \space c_i\}$$
A rule for an adaptive trait is a set of all ordered pairs of a condition and a process such that the trait was selected for performing the process $p_i$ in the conditions $c_i$. [@harms2004, 203].

It has been observed that animal signals not only inform about the world states, but also direct the behavior of others. For example, alarm calls of vervet monkeys both convey “Look, there is a leopard!” and “Run up the nearest tree” [@seyfarth1990; @baraghith2019]. Harms calls this “primitive content” that has both indicative and imperative functions [@harms2004, 189]. Millikan calls it “pushmi-pullyu” representation and notes that purely descriptive and directive representations require a more advanced cognitive process than primitives [@millikan2005, 166].

Evolutionary development of primitive content leads to the divergence of its descriptive and directive functions due to advanced cognitive capacities. As Harms suggest, it introduces a stabilizing, or regulatory mechanism $SM$ that works “atop” of conventions as rules for adaptive traits and guides behavior in case of failure of $R_{AT}$. It employs a corrective signal $CS = \{cs_{1}, ...,cs_n\}$ to "enforce" the initial convention when a signal is not sent in the presence of a world state it was selected for:
$$R_{SM}={\{\langle \sigma_{i} \wedge \neg m_{j} \space where \space \space \langle \sigma_{i,}m_{j}\rangle} \in R_{AT} \rangle\mid SM \space sel \space cs \space when \quad (\sigma_{i} \wedge \neg m_{j})\}$$
The rule for a stabilizing mechanism is a set of ordered pairs consisting of the failure of an adaptive trait in the first place and a corresponding corrective signal in the second place. If the adaptive trait fails, the stabilizing mechanism will detect this failure and send a corrective signal/action to restore it[^1]. This division is echoed in Millikan's work as firstand higher-order reproductive families [@millikan1987, 23]. According to it, conventions $R_{AT}$ are firstand stabilizing mechanisms $R_{SM}$ are second-order reproductive families that serve the same goal of restoring a first-order proper function.

It is tempting to say that on an O'Connor's "convention—social norm" continuum $R_{AT}$ is closer to conventions and $R_{SM}$  is to norms, but in Harms conventions *are* function-stabilizing mechanisms containing normative component by definition: $$\text{convention} = \langle R_{AT}, R_{SM} \rangle$$If a functional convention has normativity by default, and if institutions are norm-driven behavioral regularities, how do they differ from "animal conventions"? According to Guala and Hindriks, the difference is in scope of actionable signals. Animals have a more limited set of actionable signals than humans, as their behavior is tightly coupled to the stimuli. In game-theoretic terms, for a signaling system is an ESS, it is disatvantageous for the agents to deviate from the signal-act coupling. However, as @sterelny2003 suggests, humans have the ability to decouple stimulus and behavioral response through representations of the environment. This, in theory, allows for invention and following different rules for the same signal. But how is this decoupling is possible, and does it affect the transition from "animal conventions" to social institutions?

In O'Connor's terms, the transition from narrow set of actionable signals to the wider one is that from functional to arbitrary conventions. It means that behavioral regularities "might have been otherwise", just like Guala and Hindriks propose. However, the game-theoretic implications of this are unclear, and several questions arise:

- do social norms as expectations evolve due to an increased degree of arbitrariness in conventions?
- what introduces arbitrariness into functional conventions? If, according to Guala and Hindriks, representations of environment are key differentiator for a wider set of actionable signals, are they what introduces arbitrariness?
- how does representation of environment itself evolve? 

In other words, we need to study the relationship between the two axes of "convention space" built upon O'Connor's two distinctions. 

## Correlation and asymmetry of strategies
So far, we have established that conventions as "function-stabilizing mechanisms" might evolve from repeated signaling games and that it is possible to measure their arbitrariness. The next important question is what kind of equilibrium a convention is if it of evolutionary origin? 

Guala and Hindriks draw inspiration for their rules-in-equilibria theory of social institutions in Maynard Smith's concept of *"bourgeois equilibrium"* [@maynardsmith1982]. They see the "Hawk-dove-bourgeois" game of animal territorial ownership as a prototypical "animal convention". According to the authors, bourgeois equilibrium is essentially a correlated equilibrium, however Maynard Smith uses bourgeois to define ESS. It creates tension, for correlated equilibrium and ESS are mathematically distinct: the former is "too loose" and the latter is "too strict", and it is unclear how they can be combined. Hence, the issue consists of clarifying the status of bourgeois equilibrium in comparison to correlated equilibrium, ESS and mixed-strategy equilibrium, as well. It is due to being at the core of Guala's argument for institutions as correlation rooted in evolution. Let us look at the Maynard Smith's notion of bourgeois equilibrium represented by the "Hawk-dove-bourgeois" (HDB) game.

### Maynard Smith's "Hawk-dove-bourgeois" game

Maynard Smith introduces the notion of "bourgeois equilibrium" (BE) in the context of animal behavior in evolutionary perspective [-@maynardsmith1982]. 

It is a game-theoretic solution concept that takes into account that players may not always be able to perfectly predict each other's moves and reach an ideal Nash equilibrium. Instead, they settle for a BE which is an acceptable compromise between their own and their opponents' goals. It assumes that each player is trying to maximize their own self-interest, but no player is attempting to dominate or exploit the others. A "bourgeois equilibrium" occurs when all players have reached a strategy profile (a combination of strategies for all players) such that none of them can improve their payoff by changing only their own strategy, while also recognizing the strategies of the other players. In BE, each player chooses a strategy independently. This is distinct from mixed-strategy equilibrium, correlated equilibrium and evolutionary stable correlation, which involve coordination or communication among players. 

More precisely, BE is a type of ESS where individuals cooperate with each other instead of competing. It is different from the other types of equilibria in that it does not rely on the assumption that players are completely rational and make optimal decisions based on their individual payoffs. Instead, this type of equilibrium assumes that players will use a mixture of cooperation and defection, depending on the situation they find themselves in. 

In comparison, a mixed-strategy equilibrium is an equilibrium in which players employ a combination of strategies instead of only one strategy in order to maximize their expected payoff. Mathematically, this can be represented as $P_i(s_i, s_{-i}) = \sum_{s_j} p(s_j) \cdot u_i(s_i, s_j)$ for all players $i$ and all strategies $s$, where $P_i$ is the expected payoff for player $i$, $p$ is the probability distribution over the strategies employed by all players, and $u$ is the utility function for player $i$. In contrast, bourgeois equilibrium does not require any probabilistic elements; rather it simply requires that each player select a single strategy that they believe will yield the best outcomes. 

Correlated equilibrium (CE) is an extension of NE where each player's strategy depends on an additional set of random variables called "signals." Mathematically, this can be represented as $\sum_{a \in A} P(a) \cdot v (a | x) = v(x)$, where $A$ is the set of possible action profiles, $P$ is a probability distribution over those profiles, and $v$ is the utility function for player i. CE is different from BE in that it allows for the possibility of coordination amongst the players, such as by having one player’s strategy depend on another’s. This coordination does not occur in bourgeois equilibrium, which instead focuses on each individual’s strategy being independent from one another.

Evolutionary stable correlation (ESC) describes a situation in which two or more agents have adapted to cooperate with each other to achieve higher payoffs than either could achieve alone. Mathematically, this can be represented as $\max_{p \in \Delta} [U(p)]$, where $\Delta$ is the set of probability distributions over actions taken by agents and $U$ represents their joint utility function.

Mathematically, BE is represented by a NE, which is defined as: $$(s_1^*, s_2^*, \dots s_n^*) \in S_1 \times S_2 \times \dots S_n$$
where $s_i^*$ represents the optimal strategy for player $i$. 
In contrast, a mixed-strategy equilibrium can be represented as: $$(p_1, p_2, \dots p_n) \in D$$ 
where $D$ is the set of probability distributions over $S_1 \times S_2 \times\dots S_n$. A correlated equilibrium (CE) can be represented as: $$(s_{c1}, s_{c2},\dots s_{cn}) \in S_{C1} \times S_{C2} \times\dots S_{Cn}$$ 
where $S_{Ci}$ represents the set of strategies available to Player $i$ given the coordination between players. And an evolutionary stable correlation (ESC) can be represented by a Nash Equilibrium with strictly dominant strategies: $$(s^{* *}, s^{* *},\dots s^{* *}) \in S'$$ 
where $S'$ is the set of strict dominant strategies.

### Interpretation of HDB: correlation
There are two main interpretations of bourgeois equilibrium: with correlation and with uncorrelated asymmetry. Let us look closer at each. 

What is meant by "correlation of strategies" in the first place? Correlation of strategies is a stable state of strategic interaction. It is represented by the concept of correlated equilibrium that goes beyond the Nash equilibrium and allows players to coordinate their strategies through the use of a common randomizer, such as a coin toss or a dice roll. This allows players to make decisions based on their beliefs about how the other players will act, which can increase the efficiency of their strategies. The concept of correlated equilibrium has been used to explain various phenomena in strategic decision making, including how people form coalitions, how firms cooperate and compete, and how players interact in team games. 

Correlated equilibria can be defined by the following equation: 
$$\max_{x_1,...x_n} \sum_{i=1}^{n} u_i(x_i) $$
$$\text{s.t.} \quad x_1 = c(y_1,...y_{n-1}) \quad \forall i>1: x_i=c(y_i)$$
where $u_i$ represents the utility function for each player $i$, $x$ represents the strategy chosen by each player $i$, and $y$ represents the common randomizer chosen by all players. The equation states that the optimal strategy for each player is dependent on both their own decisions and on those of other players, which reflects how correlated equilibria allow people to take into account each other’s behavior when making decisions.  

If bourgeois strategy is an ESS, it does not presuppose any randomization. However, many scholars studying the emergence of conventions interpret them as CE. Some researchers base their explanations on interpretation of HDB. For example, @guala2016b defines social institutions as CE with normative force rooted in HDB. Gintis explicitly refers to HDB as not to strict NE, but as to CE [@gintis2009a].

The intrinsic problem with bourgeois as CE is the source of randomization. Some scholars appeal to Nature as to a such source, calling it a *correlation device*, thus eliminating the tension between the requirement of randomization and symmetry of ESS [@cripps1991; @skyrms2014; @metzger2018]. In particular, Gintis defines CE as an NE of a game $G$ augmented by the initial move by Nature that who observes a random variable $\gamma$ on a probability space $(\Gamma, p)$ and issues directives $f_{i}(\gamma) \in S$ to each player $i$, such that choosing the directive is a best response given agents having a common prior $p$ and assuming other players are also following Nature's directives [@gintis2009a, 135-136]. 

In their theory, Guala and Hindriks appeal to Skyrms's interpretation of the "Hawk-dove" that is with correlation. According to Skyrms, the implicative nature of the "bourgeois" strategy in the form "if own, then Hawk" and "if do not own, then Dove" is genuinely correlative. “Bourgeois” is correlated equilibrium spontaneously arising from symmetry-breaking that happens when individuals randomize the choice of their strategies and do not know whether they are “hawkes” or “doves” [-@skyrms2014, 78].

### Interpretation of HDB: uncorrelated asymmetry
Another interpretation of HDB involves uncorrelated asymmetry instead of correlation. @oconnor2019 employs this interpretation in her treatment of emergence of unfairness due to social categories as solutions to inherently institutional coordination problems. On this account, HDB strategy profiles are based not on correlation, but on uncorrelated asymmetry. It is a feature of games where players extract additional information from environment not included in the structure of a game. For example, they know that they are “Hawks” or “Doves” rather than their strategies are randomized. This underlies an important methodological distinction between correlated equilibrium and evolutionary stability.[^7] 

## Evolution, Bayesian updating and correlation

## Conclusion

## References
[^1]: For example, “bills issued by the Bureau of Engraving and Printing (X) count as dollars (Y) in the United States (C)“ [@searle1995, 28].
[^2]: Correlated equilibrium is a general solution concept introduced by Aumann [-@aumann1974; -@aumann1987]. As opposed to the classic Nash equilibrium, where players choose their strategies independently, here players choose strategies based on a public signal the value of which they assess privately, thus coordinating their actions according to a given correlation device.
[^3]: An ESS is a strategy which, if adopted by a population, is resilient to invasion by any alternative strategy. Mathematically, an ESS can be defined as a strategy profile $\boldsymbol{s} = (s_1, s_2, ... , s_n)$ such that $\forall \boldsymbol{s'} \neq \boldsymbol{s}$, we have $\pi(\boldsymbol{s}, \boldsymbol{s}) > \pi(\boldsymbol{s}, \boldsymbol{s'})$, where $\pi$ is the average payoff of the population playing the strategies $\boldsymbol{s}$ and $\boldsymbol{s'}$ [@maynardsmith1982].
[^4]: Nash equilibrium is a solution concept describing a strategy profile consisting of each player's best response to the other player's strategies where no one gains bigger payoff by deviating unilaterally.
[^5]: A strict Nash equilibrium is a Nash equilibrium where the player would even do worse by deviating unilaterally.
[^6]: Replicator dynamics is a mathematical model used to describe the evolution of biological populations. It is based on the idea that individuals in a population can replicate themselves over multiple generations, and that their success or failure depends on their behavior relative to other members of the population. Mathematically, it is given by $\dot{x_i} = x_i(f_i(x) - \bar{f}(x))$, where $x_i$ is the proportion of individuals in the population exhibiting a particular behavior, $f_i(x)$ is the fitness associated with that behavior, and $\bar{f}(x)$ is the average fitness in the population.
[^7]: There is an interesting similarity between a semantic regulatory mechanism like Harms' and regulatory networks in biology, that govern the dynamical repertoire of a given system like structural and regulatory genes [[@albert2014]].