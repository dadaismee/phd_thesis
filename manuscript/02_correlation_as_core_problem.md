---
title: Evolutionary stable correlation as a core problem of social ontology
author: Valerii Shevchenko
affiliation: HSE University
abstract: 
keywords: Social ontology, evolutionary game theory
header-includes:
  - \usepackage{pgfplots}
---

# Evolutionary stable correlation as a core problem of social ontology

## Introduction
In this paper, I argue that the emergence of evolutionary stable correlation is the core issue of naturalistic social ontology. According to rules-in-equilibria theory, social institutions are the central unit of social ontology [@guala2016b], and coordination is its main mechanism rooted in evolution [@shevchenko2023]. As institutions are normatively-driven self-sustaining behavioral regularities designed to solve coordination problems [@lewis2008; @aoki2007], they share many features with 'animal conventions' that help animals solve coordination problems and maintain stable relationships [@hindriks2015]. Consequently, understanding the emergence of social institutions requires an examination of the evolutionary mechanisms that enable correlation of strategies with normative force as a key characteristic.

To expand, let us first look at Guala's [-@guala2016b] argument that has the following logic:

1. social institutions are backed not by constitutive rules of the form "X counts as Y in (the context of) C", like in Searle [-@searle1995],[^1] but by regulative rules of the form "do X if Y"
2. from a game-theoretic point of view, regulative rules can be seen as agents' strategies that comprise a *correlated equilibrium*[^2]
3. constitutive rules are linguistically transformed regulative rules with added theoretical term that represents a certain equilibrium
4. at the same time, many animal species including baboons, lions, swallowtails, and others exhibit behavioral patterns describable in the form similar to correlated equilibrium [@maynardsmith1982]
5. despite the similarity of mathematical representation, the cases of 'animal conventions' and human social institutions differ in scope of actionable signals. Building on Sterelny [-@sterelny2003], Guala puts for forward an idea that humans can invent and follow new rules, whereas animals are bound to genetically inherited sets of behavioral responses
6. the arbitrariness of rules that humans can invent and follow is grounded in and ontologically depends on shared representations of a given community
7. put differently, the difference in scope of actionable signals between animals and humans can be explained by humans having social epistemology that grounds social ontology.

Although sound, this argument has an Achilles heel: the evolutionary roots of correlation of strategies as the basis of any self-sustaining social coordination, human or not, are still obscure and underdeveloped.

Guala and Hindriks base their account on Maynard Smith's, who does not use the notion of correlated eqiulibrium explicitly and discusses what he calls a *bourgeois equilibrium* — a situation in animal territorial behavior, when the most optimal strategy for an animal is to fight for a territory it "owns" or not fight otherwise. This game is represented in the matrix below.

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

This paper is structured as follows. ***First, it discusses the relationship between social institutions, conventions, and norms, and how conventions emerge in Skyrms's dynamics and Harms's evolutionary functionalism.*** Second, it examines the correlation and asymmetry of strategies in the emergence of social institutions. Third, the paper explores the source of randomization in correlation as the problem in social institutions as evolved correlated equilibria. We will analyze Guala's argument about the difference in scope of actionable signals in animals versus humans and Skyrms's interpretation of Maynard Smith's “bourgeois” concept. Fourth, it delves into the tension between bourgeois and correlated equilibria with a formal distinction between mixed-strategy and correlated equilibria.

Let us start with the notion of social institutions, destructure it into norms and conventions, study their relations and gradually arrive at the issue of coordination either by correlation or by asymmetry of strategies.

## 1. Social institutions as rules-in-equilibria
@hindriks2015 present a unified theory of social institutions as rules in equilibria represented symbolically by theoretical terms like "money" or "marriage". It bridges accounts of regulative rules, equlibria of strategic games and constitutive rules, where the former two are complementary and comprise a rules-in-equilibria account, and the latter supplements it by providing a symbolic representation.

According to @guala2016b, institutions as rules-in-equilibria are normatively-driven behavioral regularities comprising correlated equilibria. “Rules” here are the recipes guiding and prescribing certain behavior and are used by the agents themselves, and ”equilibria” are objective stable states of the strategic interaction between agents and population thereof. Other scholars pinpoint normative and self-sustaining nature of institutions. They are “humanly devised constraints that shape human interactions” [@north1990], “norm-governed social practices” [@tuomela2013] and “self-sustaining salient behavioral patterns” [@aoki2007]. It can be seen that institutions combine “subjective” and “objective” components: they are driven by social norms, that might vary from one population to another, and, at the same time, constrain possible actions and sustain itself.

The rule-based account conceives of social institutions as rules guiding and constraining behavior in social interaction or "humanly devised constraints" of social interactions [@north1990]. In sociology, the tradition of treating institutions as rules dates back to such classical figures as @weber1924 and @parsons2015, and it continues to thrive today. The equlibrium-based account sees institutions as behavioral regularities and, most importantly, solutions to coordination problems. The constitutive rules account sees institutions as systems assigning statuses and functions to physical entities [@searle1995].

According to the authors, the rule-based account is insufficient, for it cannot explain why some rules are followed and others not. To address this issue, an equilibrium account is needed to show the strategic character of rule-following.

Hindriks and Guala illustrate this point by comparing the two paradigmatic games from game theory, which are prisoner's dilemma and stag hunt. Although mutual defection in the prisoner's dilemma is a Nash equlibrium (NE),[^4] it is not a social institution, however, for it is not self-sustaining due to independence of players' strategies. In contrast, the mutual decision to hunt a stag instead of a hare, which are also both NE, is an institution, for it requires correlation of players' strategies to achieve a bigger joint payoff. The latter means that the strategy is salient and beneficial for players, what explains why some rules are followed and other not.

\begin{center}
\begin{tabular}{|c|c|c|}
\hline
& $C$ & $D$ \\
\hline
$C$ & $-1,-1$ & $-3,0$\\
\hline
$D$ & $0,-3$ & $-2,-2$ \\
\hline
\end{tabular}
\begin{tabular}{|c|c|c|}
\hline
& $S$ & $H$ \\
\hline
$S$ & $4,4$ & $1,3$\\
\hline
$H$ & $3,1$ & $2,2$ \\
\hline
\end{tabular}
\caption{Prisoner's dilemma (left) and Stag hunt (right)}
\end{center}

However, the notion of players' correlated strategies as an *explanans* of the stability of institutions is insufficient, as the authors point out, for it is too permissive. The authors provide an example of non-human animals solving coordination problems but still not having institutions. For example, male baboons, lions, swallowtails and some other species exhibit a recurring behavioral pattern that can be described in terms of correlated equilibrium. Males patrol an area to mate with females and have ritual fights with intruders if encountered. The evolved pair of players' strategies minimizes possible damage to both parties and lets the incumbent occupy territory and mate [@maynardsmith1982]. The authors use Maynard Smith's exposition of animal territorial behavior represented as a “Hawk-Dove-Bourgeois” game to provide an example of a prototypical social institution:

\begin{center}
\begin{tabular}{|c|c|c|}
\hline
& $H$ & $D$ & $B$\\
$H$ &$-1$ &$2$ &$0.5$\\
\hline
$D$ &$0$ &$1$ &$0.5$ \\
\hline
$B$ &$-0.5$ &$1.5$ &$1.0$
\hline
$D$ & $0,-3$ & $-2,-2$ \\
\end{tabular}
\caption{\\small "Hawk-Dove-Bourgeois" game}
\end{center}

Presented with a terrestrial resource, a “Hawk” player fights over it, a “Dove” retreats and “Bourgeois” uses a strategy “fight if own and retreat if do not own”. In this game, Guala and Hindriks see the “bourgeois” strategy “fight of own” as a correlated one, meaning that players coordinate their actions by conditioning them on an external signal. As they say, its is a "simple pre-emption device: whoever occupied the land first has the right to use it" [@hindriks2015, 465]. In this case, the temporal order of occupation is used as correlation device. Overall, this correlation fulfills the necessary condition of being an institution.

@guala2015 illustrate the applicability of HDB to humans with a game where two tribes, spatially separated by a dry river, graze their cattle. The dry river serves as a “focal point”—a salient feature of the environment that the members of both tribes have been aware of [@schelling1980]. It also serves as a correlation device, for it is a source of a public signal that coordinated actions of different tribes without their explicit agreement. Thus, the shepherds of both tribes have three possible strategies: “Graze”, “Not graze” and “Graze if North / South of the river” according to the history of their territorial occupation. The members of one tribe might be killed by the members of another if grazing their cattle on another side of the dry river which the other tribe possesses. The most stable set of strategies is grazing if on the own side of the dry river. However, this is insufficient, for the payoff structure of the game is uniform for animal and human cases. Hence, we cannot discriminate between them solely on this basis.

\begin{center}
\begin{tabular}{|c|c|c|}
\hline
& $G$ & $NG$ & $GIS$\\
\hline
$G$ &$-1$ &$2$ &$0.5$\\
\hline
$NG$ &$0$ &$1$ &$0.5$ \\
\hline
$GIN$ &$-0.5$ &$1.5$ &$1.0$
\end{tabular}
\caption{\small Grazing game: the player strategies are Graze, Not Graze and Graze if North / Graze if South}
\end{center}

What, then, distinguishes animal conventions from human social institutions? Guala and Hidriks argue that they differ in the scope of actionable signals. Building on the work of @sterelny2003, they say that animals may only respond to a limited set of stimuli, but humans, with their ability to use representations and symbols to condition behavior, can decouple stimulus and response and invent new rules. For example, butterflies cannot coordinate on anything but who occupied the sunspot first and unable to create new equilibria. Humans, however, can go beyond this: establishing various correlations, devising new strategies, and expanding the number of equilibria.

There are two types of rules:

- agent-rules that agents formulate to represent and guide their behaviour
- observer-rules that observer formulates to represent and summarize others' behaviour.

Strategies can be described as rules, but a-rules influence behaviour and o-rules only describe it [@guala2016b, 54].

Institutions are composed of both subjective and objective components: they are determined by varying social norms as rules and simultaneously restrict certain behaviors and their own perpetuation. But how they are connected?

Guala and Hindriks argue that an adequate theory of institutions must have three explanatory components [@guala2015, 469]:

- coordination
- correlation
- representation.

Following the logic of the authors, institutions coordinate behavior by correlation of strategies, and humans are able to devise many strategies and equilibria given the same correlation device, or signal, due to an advanced cognitive capacity for conditioning behavior on representation of the environment. At the same time, as rules-in-equilibria theory has “rules” and "equilibria” parts, they must be somehow connected. For this reason, rules are symbolic representations of strategies in a game that comprise equilibria. They not only serve as symbolic markers of the properties of equilibria, but considerably save cognitive effort. As Aoki notes [-@aoki2007, 6]:

> “An institution is a self-sustaining, salient pattern of social interaction, as represented by meaningful rules that every agent knows, and incorporated as agents' shared beliefs about the ways the game is to be played”.

```{.mermaid background=transparent format=svg}
graph LR;
	subgraph Objective
		3(Observer rules)
		1(Correlated equilibrium)
		1<-.->3
	end
	subgraph Subjective
		3<-.Representation.->4
	end
	4(Agent rules)
```

However, it is not evident how exactly rules represent strategies. To clarify this issue, the authors, drawing on @hindriks2005, propose to bridge their rules-in-equilbria account of institutions with the constitutive rules account. The latter presents institutions as systems of statuses and functions, paradigmatically proposed by @searle1995 as the formula "X counts as Y in C”. Searle draws a sharp distinction between constitutive and regulative rules, emphasizing the difference in their syntax, for that of the latter is “do X if Y”.

The constitutive rules approach argues that our beliefs are essential for the existence of institutions, which involve more than just actions. This applies to objects, persons, and events too—for example, “Bills issued by the Bureau of Engraving and Printing count as money in the United States” [@searle1995, 28]. X can be replaced by predicates that refer to any ontological category [@guala2015, 470].

As the authors note, constitutive rules are linguistically transformed regulative rules, aided with a new term to name an institution. Combining these accounts enables researchers to investigate Y terms like “money” used by individuals in everyday life and analyze their internal regulative and strategic character, thus bridging explicit ontology of social science and implicit ontology of ordinary language. The main idea of this argument, thus, is that constitutive rules can be developed at will from regulative rules or game-theoretic strategies by introducing institutional terms [@guala2015, 477].

$$\text{Regulative rules} \, + \, \text{Institutional terms}= \text{Constitutive rules}$$

For example, one can transform a regulative rule "if a bill is issued by the Bureau of Engraving and Printing, it can be used to pay for goods in the United States" into "Bills issued by the Bureau of Engraving and Printing count as money in the United States" by adding an institutional term "money".

## 2. Rules, norms and conventions
What are the rules Guala and Hindriks are talking about? As they stipulate that institutions are norm-governed salient social practices, or behavioral regularities, rules are norms. It is the case for agent rules, though. So, what roles do norms play in institutions? Guala notes that social norms fulfill two functions highlighted by @north1990: they make behaviour more stable and more predictable. However, as noted by Searle, they introduce new behaviours, as well, and they do it by changing game payoffs. Norms help explain not only the persistence of institutions, but also its emergence. But if social norms are inherently important to institutions, what are they, and how do they differ from social institutions?

@hindriks2019 elaborates on the definition of social institutions as norm-governed social practices and explicates how norms might govern practices. His main idea is that modeling social norms as sanctions with costs that agents incur for violating norms, is insufficient for its perception by agents as legitimate. According to the author, this account fails to capture the motivation by the norm itself and not by the costs of its violation. He claims that it is normative expectations and normative beliefs that complement sanctions as a source for norm existence and perception as legitimate. Social norm governs a practice if its participants are motivated to follow its rule to a noteworthy extent.

Social norms can influence behavior due to sanctions imposed for violating them. Such sanctions modify people's preferences in cooperation games and motivate them to cooperate [@ullmann-margalit1977]. Apart from this, norms can be seen as legitimate, which leads people to conform even if it might not be in their best interest [@bicchieri2005]. This is evidenced by the difficulty people experience when deciding to violate norms. In other words, decisions to conform are often more complex than a simple cost-benefit calculation.

Hindriks highlights coordination and cooperation types of social norms. Coordination norms such as first-come-first-serve as standing in line are contrasted by cooperation norms like “I-will-scratch-your-back-if-you-scratch-mine”. Game-theoretically, this distinction is represented by either aligning or conflicting interests of agents in a game, respectively.

To this end, social institutions can be seen as solutions to coordination or cooperation games. Coordination games have at least two solutions that benefit all players. For example, two sides of the road to drive on. It does not matter on which particular side all the drivers drive, but the side being the same does matter, e.g, left in the UK or right in Europe. Cooperation games have one solution optimal for all players. For example, hunting a stag requires several participants but has a higher payoff for each, whereas hunting a rabbit can be done alone and has a lower payoff. It is more beneficial for everyone to cooperate and hunt a stag to get a higher payoff.

Hindriks studies the conditions of possibility for such behavioral regularities that successfully solve coordination and cooperation problems. He starts with the notion of convention, which is a population-wide beneficial regularity of behavior, deviating unilaterally from which is disadvantageous [@lewis2008 [1969]]. As there are two or more equally profitable solutions, or equilibria, in coordination problems, the mutual convergence of the agents on the same solution becomes important, otherwise there will be miscoordination. Lewis, a pioneer of game-theoretic analysis of conventions, argues that given recurrent situations with coordination problems, people choose by precedent. They condition their behavior on what they expect others to do, enabling coordinated behavior among the population.

Lewis's account of conventions states that a behavioral regularity is a convention in a population P in a coordination game situation S if the following criteria are fulfilled:

- (1) Members of P conform to the regularity;
- (2) They expect others to conform;
- (3) They prefer to conform if others do so;
- (4) This is common knowledge of the form "everybody knows that everybody knows that P".

At the same time, Lewis regards conventions as norms and does not make a sharp distinction between the two.

[[📝 🚧 Evolutionary stable correlation as a core problem of social ontology#^c1f8b0|Add on Vanderschraaf]]

On this game-theoretic account, social norms are modeled as sanctions with costs that can alter behavior by influencing agents' preferences, as agents face costs for not conforming to it. High costs and a greater likelihood of violation-detection increase the incentive to cooperate. Institutions, in their turn, are maintained partly because of these norm costs.

At the same time, introduction of sufficiently high delta parameter into cooperation problems transforms them into coordination ones. For instance, given a Prisoner's dilemma with a high delta parameter representing a cost for norm violation, the game becomes that of coordination with two equilibria — “Cooperate, cooperate” and “Defect, defect” (CC, DD) instead of only one — DD [@crawford1995]. This shows that normative rules can in principle be coordination devices, or “choreographers”, as Gintis puts it [@gintis2009a].

\begin{center}
\begin{tabular}{|c|c|c|}
\hline
& $C$ & $D$ \\
\hline
$C$ & $-1,-1$ & $-3,0-\delta$\\
\hline
$D$ & $0-\delta,-3$ & $-2,-2$ \\
\hline
\end{tabular}
\begin{tabular}{|c|c|c|}
\hline
& $C$ & $D$ \\
\hline
$C$ & $-1,-1$ & $-3,0$\\
\hline
$D$ & $0,-3$ & $-2,-2$ \\
\hline
\end{tabular}
\caption{\label{fig:delta-transformation-coordination-game}{Delta parameter transforming cooperation game into coordination game.}}
\end{center}

Hindriks draws a distinction between social norms and conventions: norm-compliance is motivated, and conventions are self-reinforcing. He also calls them descriptive and normative conventions. @bicchieri2005 has stated this in terms of the relationship between self-interest and common interest. They coincide in conventions and do not in norms. It means there can be conventions without norms. However, contra Lewis, @gilbert1992 explicitly treats conventions as intrinsically normative and calls them quasi-agreements conceptually linked to joint intentions, which generate normative reasons for conformity. At the same time, @brennan2013 argue that conventions can become normative because they protect or promote some value. @guala2010 support this by empirical evidence.

Overall, conventions are self-reinforcing, so sanctions are not necessary for creating and maintaining a mutually beneficial behavioral regularity. However, both Lewis and Bicchieri acknowledge that exceptions may exist, making some conventions more fragile than others. Norms, in their turn, make confirming more attractive and thus help to stabilize conventions to ensure collective benefits and prevent malfunctions.

According to the rules-in-equilibria theory of institutions that Hindriks defend along with Guala, institutions are norm-governed social practices. And Hindriks defines a social practice as a regularity in behavior that involves norms. Practices arise in response to signaling devices, which are salient features of the environment that enable agents to align their behaviors in beneficial ways, creating new strategies and thus giving rise to conventions. Interdependent behavioral regularities in coordination games arise from signaling rules of the form “if D, do A”, whereby agents condition their behavior on a signal to coordinate mutually beneficial interactions and achieve collective benefits. In a case of a traffic light, the light itself serves a signaling device that helps to make traffic safer and more efficient by coordinating behaviors.

As normativity pervades social interaction, Hindriks distinguishes two types of normative standards: deontic ones, such as right/wrong, and evaluative ones, such as better/worse. Deontic standards signify obligations, while evaluative standards refer to the quality of performance in various activities, e.g., hosting guests. Social practices can feature either deontic and evaluative standards, evaluative standards only, or neither. As an example, a group of friends that loathes rules may also dislike evaluative standards. This suggests that conventions involve signaling rules, but do not necessarily include normative rules. Therefore, social practices can exist without being an institution.

Hindriks discusses several views of social norms. The 'normative-beliefs view' holds that when people encounter a coordination or cooperation game situation, they are expected to act in a certain way and this is generally known. @brennan2013 define social norms as normative principles or rules which are commonly accepted and known. Social norms are thus generally accepted and recognized normative beliefs.

However, the phenomenon of “pluralistic ignorance” counteracts the 'normative-beliefs view' by being too restrictive in requiring acceptance of the norm. Hindriks provides an example of college students believing that they are expected to drink heavily on weekends, while not really liking doing it. They do not believe that they ought to do so, but they acknowledge that others believe that college students generally do it. To reflect it, the secind, normative-expectations view, proposes that a social norm exists in a population if its rule is present in the normative expectations of its members. This differs from the normative-beliefs view in that it does not require acceptance of the norm, only acknowledgment of it, and that knowledge of others' attitudes is not necessary. It permits inclusion of the norm in first-order beliefs.

Bicchieri's theory [-@bicchieri2005] is largely akin to the normative-expectations view, yet there are three key differences. Firstly, she limits the concept of a social norm to regulations that address cooperation problems, while Hindriks includes coordination ones, as well. Secondly, her conception of normative expectations does not make them normative, strictly speaking, for they are higher-order empirical expectations. Someone has a normative expectation if they expect others to adhere to a descriptive rule of 'Everybody does A'. According to Bicchieri, this involves obligations. However, as Hindriks stipulates, an expectation of behavior differs from the belief that a normative rule applies; the former being an expectation, the latter a belief about what should be done.

The third view of social norms is 'conditional-preferences view'. It holds that a social norm exists when enough participants prefer to conform to it given empirical and normative expectations [@bicchieri2005]. However, @southwood2019 argues that people may secretly wish to break the norm if others do the same and expect each other to do so. According to the conditional-preferences view, perceiving a social norm as legitimate is when someone regards the relevant normative expectations as well-founded. This can motivate people to act accordingly [@bicchieri2005].

Overall, the normative-beliefs view holds that people need only possess normative beliefs featuring a rule for it to be perceived as legitimate; these beliefs are self-justifying. The conditional-preferences view, however, states that legitimacy is derived from justified normative expectations.

According to Hindriks, neither of these two views is adequate. The normative-beliefs view holds that social norms are self-justifying and tend to be regarded as legitimate. Yet, pluralistic ignorance shows that this is not always the case. The normative-expectations view suggests that perceived legitimacy is based on justified normative expectations, which lead to corresponding beliefs. This belief lies at the core of what it means for a social norm to be seen as legitimate, and can only be suitably justified with empirical and normative expectations. The conditional-preferences view fails to capture this complexity, while the normative-expectations view does so by explicating legitimacy in terms of an agent's normative beliefs. This motivates agents to conform and makes a difference to behavior within institutions.

Moreover, the normative-expectations view states that a social norm has authority if the normative beliefs people have are suitably justified. This is only true if the expectations are both justified and true, indicating that there is an applicable regularity and that others believe the norm applies.

According to Hindriks, for a social norm to govern a social practive, its participants must adhere to it. This will create an institution, which will be perceived as legitimate and have authority. However, norm-following alone is too demanding an explanation for institutions that are not seen as legitimate. Sanctions, which are important in formal and informal norms, demonstrate that norm-following does not always lead to conformity.

In sum, a norm governs a practice only if it motivates a substantial number of participants. It happens when it is deemed significant to conform to it. Norm-conformity is not enough for norm-governance, as demonstrated by the example of the convention to drive on the right-hand side of the road. This convention is self-reinforcing, but does not motivate anybody and does not constitute an institution. Thus, neither norm-following nor norm-conformity is necessary for norm-governance and norm-conformity is insufficient.

To this end, social institutions are norm-driven conventions, or social practices, that require cognitive capacities for recognition, complying to and changing of social norms.

## 3. The problem with "representation"
As might be seen from the exposition, the authors base their argument on the notion of insufficiency—of both rules and equilibria as distinct explanations of institutions. However, while justifying the insufficiency of equilibria with applicability of the concept of correlated equilibria to both humans and animals, the authors use the notion of representation in a broad sense, although appeal to @sterelny2003, who uses it in a narrower sense of an advanced cognitive capacity. It means that coordination and correlation are insufficient, and representation is needed.

However, the character of the term "representation" is ambiguous: a-rules "represent" game-theoretic strategies in a more philosophical sense and not in a cognitive one, while the authors mention terms like stimuli, behavior and representation, that clearly imply a narrower cognitive perspective and not a wider philosophical one. From a social-scientific point of view, representation as a relation makes sense, it allows for investigation of Y-terms, or institutional terms, used by agents by observing a social practices, circumscribing social norms that govern them and then trying to figure out the respective strategies in equilibrium. However, representation as a cognitive capacity does not have any immediate practical application, especially in sociological data. Hence, there is need to discern two notions of representation in Guala's and Hindriks' argument:

- representation as relation
- representation as cognitive capacity.

If, according to the authors, representation as a cognitive capacity distinguishes human conventions from animal ones, which is a crucial step in their argument from insufficiency of both rules and equilibria, it means that the representation as a relation between the rules and equilibrium might ontologically depend on representation as a cognitive capacity.

As the authors base their argument on Sterelny's, the capacity for inventing and following new normative rules depends on response breadth and decoupled representation of environment accessible to humans. However, crucially, there is no explicit conceptual link between representation as a cognitive capacity that grounds rule invention and representation of strategies by a-rules. The former is a feature of agents, and the latter the feature of a theory describing the agents.

When the authors introduce representation as a final condition for satisfactory theory of institutions along with coordination and correlation, they mainly mean "representation-as-relation", as they use it to clarify and justify the relationship between the two parts of the theory: rules and equilibria. Representation here means that agents are capable of representing equilibria and their salient features in symbolic form [@hindriks2015, 466]. According to the authors, this is possible due to an advanced cognitive capacity for decoupling a stimulus and behavior with the aid of representation of environment. This decoupling allows for conditioning behavior, or strategies, on many coordination devices, and the authors take it for humans to be equivalent to "following different rules". Here rules are symbolic representations of the strategies "that ought to be followed in a given game" [@hindriks2015, 467].

Here is a problem with this argument. It presupposes that behavior conditioning, and hence strategy selection, occurs already being based on existing rules. To follow a rule, it should exist. At the same time, these rules are a-rules, and they already represent existing strategies "that ought to be followed in a given game".
It means that behavior is conditioned on the existing strategies, and this involves a vicious circle: inventing new rules requires not only a capacity for stimulus-behavior decoupling, but existing equilbria, for here salient features of existing equilibria are used as coordination devices. In other words, the authors equate representation of salient features of the environment with representation of existing strategies, or behavioral responses, that preexist in the current game structure and "ought to be followed". It means that agents directly represent game structure with the aid of a-rules and institutional terms, which is odd.

Would this work without representation as a cognitive capacity? No, for stimulus-behavior decoupling is key for a capacity to invent and follow new rules which distinguishes human social institutions and animal conventions. The introduction of (decoupled) representation as a cognitive capacity is only due to justifying the this difference: although the payoff structure in both HDB games is the same, human agents are able to devise and converge on new equilibria given the same coordination device, or signal. For example, if butterflies can coordinate only on the precedence of occupying the sun spot, for they use the temporal order of territory occupation as a coordination device, humans are not genetically hardwired for using one and only coordination device for a given situation. We can interpret the same coordination device differently. As a simple example, many countries have a nod as "yes" and head shake as "no". However, it is the opposite in Bulgaria. A set of signals is the same, but the equilibrium is different. And it crashes when a foreigner tries to understand a native. Overall, the argument will not succeed without representation as a cognitive capacity, for there will still be no difference between human social institutions and animal conventions in game-theoretic terms.

And would the argument work without the notion of representation as a relation between rules and equilibria? No, as well, as it is the crux of the argument and of the unification done by rules-in-equilibria theory. Representation here logically connects rules and equilibria and helps to further connect it to constitutive rules theory by the notion of institutional, or Y-terms, as in "X count as Y in C" formula.

A more interesting question is whether representation as relation is possible without representation as a capacity. No, for as there is no structural difference between animal conventions and human social institutions without a human capacity for stimulus-behavior decoupling, there is no added representation of strategies with a-rules by agents. Animals seemingly cannot represent strategies with formulated normative rules. And if there is no decoupling, hence there is no "new rules and strategies". Apart from this, according to the authors, representation is needed to condition the behavior on the features of existing equilibria "that ought to be followed" to introduce brand new strategies and equilibria. It means that behavior conditioning, either in Sterelny's sense of salient features of immediate environment or in Guala's and Hindriks' sense of a-rules as representations of salient features of existing equilibria, requires a capacity for a decoupled representation.

Thus, for the whole argument about social institution as rules-in-equilibria to succeed, Guala and Hindriks should show two things:

- that correlated equilibrium is indeed supported both in human and animal conventions in the first place. It is for @maynardsmith1982, from whom they take the notion of bourgeois equilibrium, uses ESS and not correlated equilibrium;
- that representation as a relation between rules and equilibrium is ontologically dependent on representation as a cognitive capacity.

For the theory to fully work, it is needed to clarify the mechanics of decoupled representation: how it contributes to the emergence of new strategies to the extent that agents acquire an advanced capacity to represent game structure and salient features of equilibria, if they do at all. However, this is out of scope of this paper. Now we take a step back and analyze the notion of a "Hawk-Dove-Bourgeois" game as introduced by @maynardsmith1982 that plays a crucial role in the argument of Guala and Hindriks.

## 4. Correlation and asymmetry of strategies
So far, we have established that conventions as "function-stabilizing mechanisms" might evolve from repeated signaling games and that it is possible to measure their arbitrariness. The next important question is what kind of equilibrium a convention is if it of evolutionary origin?

Guala and Hindriks draw inspiration for their rules-in-equilibria theory of social institutions in Maynard Smith's concept of *"bourgeois equilibrium"* [@maynardsmith1982]. They see the "Hawk-dove-bourgeois" game of animal territorial ownership as a prototypical "animal convention". According to the authors, bourgeois equilibrium is essentially a correlated equilibrium, however Maynard Smith uses bourgeois to define ESS. It creates tension, for correlated equilibrium and ESS are mathematically distinct: the former is "too loose" and the latter is "too strict", and it is unclear how they can be combined. Hence, the issue consists of clarifying the status of bourgeois equilibrium in comparison to correlated equilibrium, ESS and mixed-strategy equilibrium, as well. It is due to being at the core of Guala's argument for institutions as correlation rooted in evolution. Let us look at the Maynard Smith's notion of bourgeois equilibrium represented by the "Hawk-dove-bourgeois" (HDB) game.

### 4.1 Maynard Smith's "Hawk-dove-bourgeois" game
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

### 4.2 Interpretation of HDB: correlation
There are two main interpretations of bourgeois equilibrium: with correlation and with uncorrelated asymmetry. Let us look closer at each.

What is meant by "correlation of strategies" in the first place? Correlation of strategies is a stable state of strategic interaction. It is represented by the concept of correlated equilibrium that goes beyond the Nash equilibrium and allows players to coordinate their strategies through the use of a common randomizer, such as a coin toss or a dice roll. This allows players to make decisions based on their beliefs about how the other players will act, which can increase the efficiency of their strategies. The concept of correlated equilibrium has been used to explain various phenomena in strategic decision making, including how people form coalitions, how firms cooperate and compete, and how players interact in team games.

Correlated equilibria can be defined by the following equation:

$$\max_{x_1,...x_n} \sum_{i=1}^{n} u_i(x_i) $$

$$\text{s.t.} \quad x_1 = c(y_1,...y_{n-1}) \quad \forall i>1: x_i=c(y_i)$$

where $u_i$ represents the utility function for each player $i$, $x$ represents the strategy chosen by each player $i$, and $y$ represents the common randomizer chosen by all players. The equation states that the optimal strategy for each player is dependent on both their own decisions and on those of other players, which reflects how correlated equilibria allow people to take into account each other’s behavior when making decisions.

If bourgeois strategy is an ESS, it does not presuppose any randomization. However, many scholars studying the emergence of conventions interpret them as CE. Some researchers base their explanations on interpretation of HDB. For example, @guala2016b defines social institutions as CE with normative force rooted in HDB. Gintis explicitly refers to HDB as not to strict NE, but as to CE [@gintis2009a].

The intrinsic problem with bourgeois as CE is the source of randomization. Some scholars appeal to Nature as to a such source, calling it a *correlation device*, thus eliminating the tension between the requirement of randomization and symmetry of ESS [@cripps1991; @skyrms2014; @metzger2018]. In particular, Gintis defines CE as an NE of a game $G$ augmented by the initial move by Nature that who observes a random variable $\gamma$ on a probability space $(\Gamma, p)$ and issues directives $f_{i}(\gamma) \in S$ to each player $i$, such that choosing the directive is a best response given agents having a common prior $p$ and assuming other players are also following Nature's directives [@gintis2009a, 135-136].

In their theory, Guala and Hindriks appeal to Skyrms's interpretation of the "Hawk-dove" that is with correlation. According to Skyrms, the implicative nature of the "bourgeois" strategy in the form "if own, then Hawk" and "if do not own, then Dove" is genuinely correlative. “Bourgeois” is correlated equilibrium spontaneously arising from symmetry-breaking that happens when individuals randomize the choice of their strategies and do not know whether they are “hawkes” or “doves” [-@skyrms2014, 78].

### 4.3 Interpretation of HDB: uncorrelated asymmetry
Another interpretation of HDB involves uncorrelated asymmetry instead of correlation. @oconnor2019 employs this interpretation in her treatment of emergence of unfairness due to social categories as solutions to inherently institutional coordination problems. On this account, HDB strategy profiles are based not on correlation, but on uncorrelated asymmetry. It is a feature of games where players extract additional information from environment not included in the structure of a game. For example, they know that they are “Hawks” or “Doves” rather than their strategies are randomized. This underlies an important methodological distinction between correlated equilibrium and evolutionary stability.

## 5. Evolution, Bayesian updating and correlation

## Conclusion

## References
[^1]: For example, “bills issued by the Bureau of Engraving and Printing (X) count as dollars (Y) in the United States (C)“ [@searle1995, 28].
[^2]: Correlated equilibrium is a general solution concept introduced by Aumann [-@aumann1974; -@aumann1987]. As opposed to the classic Nash equilibrium, where players choose their strategies independently, here players choose strategies based on a public signal the value of which they assess privately, thus coordinating their actions according to a given correlation device.
[^3]: An ESS is a strategy which, if adopted by a population, is resilient to invasion by any alternative strategy. Mathematically, an ESS can be defined as a strategy profile $\boldsymbol{s} = (s_1, s_2, ... , s_n)$ such that $\forall \boldsymbol{s'} \neq \boldsymbol{s}$, we have $\pi(\boldsymbol{s}, \boldsymbol{s}) > \pi(\boldsymbol{s}, \boldsymbol{s'})$, where $\pi$ is the average payoff of the population playing the strategies $\boldsymbol{s}$ and $\boldsymbol{s'}$ [@maynardsmith1982].
[^4]: Nash equilibrium is a solution concept describing a strategy profile consisting of each player's best response to the other player's strategies where no one gains bigger payoff by deviating unilaterally.