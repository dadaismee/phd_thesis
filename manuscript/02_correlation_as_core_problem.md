---
title: Emergence of evolutionary stable correlation as a core problem of social ontology
author: Valerii Shevchenko
affiliation: HSE University
abstract: 
keywords: Social ontology, evolutionary game theory
---

# Emergence of evolutionary stable correlation as a core problem of social ontology

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

Guala and Hindriks interpret bourgeois equilibrium as a correlated one. However, there are at least two interpretations of it: *correlated equilibrium* and *evolutionary stable strategy* (ESS) based on uncorrelated asymmetry. They are mathematically distinct, and we will look at both in detail later.

The presented ambiguity creates tension at the backbone of Guala's argument. It means that:

- either 'animal conventions' are mathematically different from human social institutions, for they represent ESS and not correlated equilibrium, and there comes the burden of showing how the former becomes the latter in the course of evolution;
- or that 'animal conventions' are themselves correlated, and there comes the burden of showing how humans acquired the capacity for social epistemology that ontologically grounds social ontology as rules-in-equilibria.

Taking into account the wealth of research on transition from ESS to correlation in game theory [@skyrms1994; @lee-penagos2016; @kim2017; @metzger2018; @herrmann2021], the first option in resolving the tension in Guala's argument becomes insufficient. The transition from ESS to correlation does not intrinsically presuppose the emergence of intentional compliance to norms, as in social institutions, which are normatively-driven and at the same time arbitrary, as will be covered later. Consequently, it will be needed to account for the second option, but to begin, we need to figure out whether social institutions indeed necessitate correlation of strategies. In this paper, I will address the source of the issue—Maynard Smith's notion of bourgeois equilibrium and its interpretations in regard to social coordination.

It is relevant, for if social institutions have emerged from 'animal conventions' with the aid of cognitive capacities like mindreading and/or mindshaping [@zawidzki2013], it constrains social ontology as the scope of possible objects of study to the logical derivatives of social institutions and social coordination in general as discussed in @shevchenko2023.

This paper is structured as follows. First, it discusses the relationship between social institutions, conventions, and norms, and how conventions emerge through Skyrms's deliberational dynamics and Harms's evolutionary functionalism. Second, it examines the correlation and asymmetry of strategies in the emergence of social institutions and explains what correlated equilibrium and uncorrelated asymmetry mean. Two views on correlation versus asymmetry are also discussed. Third, the paper explores the problem with correlation in social institutions as evolved correlated equilibria. It analyzes Guala's argument about the difference in scope of actionable signals in animals versus humans and Skyrms's interpretation of Maynard Smith's “bourgeois” concept. Fourth, it delves into the tension between bourgeois and correlated equilibria with a formal distinction between mixed strategy and correlated equilibria, as well as addressing where randomization of strategies comes from.

## Difference and evolution of conventions, norms, and institutions
Let us start with the notion of social institutions and move backwards. According to @guala2016b, institutions are rules-in-equilibria, normatively-driven behavioral regularities represented as correlated equilibria. “Rules” here are the recipes guiding and prescribing certain behavior and are *used by the agents themselves*, and ”equilibria” are objective stable states of the strategic interaction between agents and population thereof. Other scholars pinpoint normative and self-sustaining nature of institutions. They are "humanly devised constraints that shape human interactions" [@north1990], "norm-governed social practices" [@tuomela2013] and "self-sustaining salient behavioral patterns" [@aoki2007]. It can be seen that institutions combine "subjective" and "objective" components: they are driven by social norms, that might vary from one population to another, and, at the same time, constrain possible actions and sustain itself.

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

In this game, two drivers must choose whether to drive on the left or right side of the road. The payoffs indicate how well each driver does depending on their choice and their partner's choice. If both drivers choose the same side (either both drive on the left or both drive on the right), they each receive a payoff of $1$. If they choose different sides (one drives on the left while the other drives on the right), they each receive a payoff of $-1$. This game has two pure strategy Nash equilibria:[^9] both drivers driving on the left or both driving on the right. In other words, if both drivers follow these conventions, they will achieve a mutually beneficial outcome. Lewis argues that conventions can emerge in situations like this through repeated interactions between agents who learn to coordinate their behavior over time. As more people adopt a particular convention, it becomes more costly for others to deviate from it because they risk being penalized by their partners.

If conventions are mutually expected and mutually beneficial behavioral regularities, how are they different from both social norms and social institutions? O'Connor (2019) draws two crucial distinctions, namely between conventions and social norms, and between more and less arbitrary conventions. The initial distinction implies that not all behavioral regularities possess normative force, meaning that conventions and norms are not that the same. For instance, friends may have a convention of meeting every Friday evening at a bar, and failing to show up does not necessarily imply a violation of a norm. However, when two cars are driving in the same direction towards each other on the same side of the road, the drivers are compelled to swerve to avoid collision. Failing to do so may result in fines or even accidents; hence, swerving becomes an obligatory normative action.

Furthermore, as Bicchieri (2005) asserts, conventions differ from social norms in their association with self-interest and common interest. While they converge with self-interest, they do not necessarily coincide with common interest. In the case of friends gathering at a bar, there is minimal or no tension between self-interest and common interest; however, when driving cars on the road, there is an inherent tension between these interests. O'Connor notes that conventions and norms exist along a continuum, where conventions can acquire normative force based on their position on this spectrum.

## Correlation and asymmetry of strategies

## The problem with correlation

## Conclusion

## References
[^1]: For example, “bills issued by the Bureau of Engraving and Printing (X) count as dollars (Y) in the United States (C)“ [@searle1995, 28].
[^2]: Correlated equilibrium is a general solution concept introduced by Aumann [-@aumann1974; -@aumann1987]. As opposed to the classic Nash equilibrium, where players choose their strategies independently, here players choose strategies based on a public signal the value of which they assess privately, thus coordinating their actions according to a given correlation device.