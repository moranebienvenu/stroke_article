---
numbering:
  heading_2: false
  figure:
    template: Fig. %s
---


# Introduction

Stroke remains a major global public health issue, profoundly affecting individuals' quality of life through a wide range of consequences, including aphasia, motor and sensory deficits, behavioral changes, and even death (Brain Injury Canada, 2024). It is among the most devastating non-communicable diseases (NCDs), ranking second in global mortality and third in combined mortality and disability. Globally, by age 25 one in four adults is expected to experience a stroke in their lifetime, and more than half of these events will occur before the age of 70. In 2021, nearly 12 million people experienced a first-ever stroke, of which 65.3% were ischaemic, and 52.6% occurred in men [@Feigin2025]. Despite the slightly higher incidence in men, women who survive a stroke often experience more severe long-term disability. This difference is partly attributed to the older average age at which women suffer strokes and to the loss of estrogen's neurovascular protection after menopause. Knowing that estrogen and progesterone enhance vasodilatation effects, whereas testosterone is believed to have opposed vascular effects [@Haast2012].

Ischaemic stroke results from an obstruction of cerebral blood flow, usually due to a thrombus or embolus, while haemorrhagic stroke is caused by bleeding from a ruptured vessel. Ischaemic stroke is the most common form of stroke. In fact, the present study focuses exclusively on ischaemic stroke, particularly those resulting in aphasia since it affects approximately 1/3 of stroke patients [@Pedersen1995]. Aphasia is a disorder that impairs the production and comprehension of language, as well as reading and writing, due to brain damage. While stroke recovery has been widely studied, sex-specific mechanisms underlying aphasia recovery remain underexplored, especially in the acute phase (<72 hours post-stroke). 
Recent advances in molecular neuroimaging offer novel tools to explore these mechanisms. Hansen et al. recently published a neurotransmitter atlas of normative receptor and transporter densities maps, which was later used by Alves et al. to develop an MRI white matter atlas of neurotransmitter circuits representing the axonal projections of acetylcholine, dopamine, noradrenaline, and serotonin receptors and transporters. Their method allows to chart how stroke damages neurotransmitter systems, which distinguishes pre and postsynaptic disruption. Their method offers a promising approach to customize stroke treatment based on individual profiles.

Nevertheless, there is still limited understanding of how biological sex modulates early neurotransmitter dynamics following stroke. In particular, the role of key neurotransmitters involved in language and memory, such as the ones used by Alves et al. to develop their tool and also glutamate, and γ-aminobutyric acid (GABA), remains underexplored in the context of sex-specific recovery trajectories after stroke. These neurotransmitters are all relevant to cognitive and linguistic functions. Identifying sex-linked neurochemical differences in these systems could pave the way for more personalized therapeutic strategies

The objective of this study is twofold: (1) to determine whether and how biological sex influences neurotransmitter receptor and transporter dynamics during the acute phase of post-stroke aphasia; and (2) to assess whether these early neurochemical patterns can help predict long-term language recovery. Ultimately, this work aims to contribute to more personalized stroke rehabilitation approaches, including the tailored use of receptor agonists or transporter inhibitors, recognizing that men and women may respond differently to the same pharmacological intervention.


# Materials and methods

## Participants

Forty-eight individuals with aphasia (PWA) were recruited from the Neurology Unit of the Hôpital du Sacré-Cœur de Montréal (HSCM), part of the CIUSSS du Nord-de-l’Île-de-Montréal. Sixteen participants were later excluded due to the following reasons: brain tumors, right or bilateral stroke, left-handedness, MRI intolerance, multiple strokes, or voluntary withdrawal/refusal to continue participation. Ultimately, fifteen participants completed all three timepoints up to the chronic phase.
Inclusion criteria for PWA were: (1) first-ever left-hemispheric ischemic stroke in the middle cerebral artery (MCA) territory; (2) presence of aphasia affecting speech production and/or comprehension in the acute phase; (3) native French speaker; (4) aged 18 to 85; and (5) right-handed. Exclusion criteria included: (1) major psychiatric illness; (2-3) history of traumatic brain injury or intracranial surgery; (4) alcoholism or drug abuse; (5) learning disability; (6) uncorrected hearing or vision problems; (7) MRI contraindications (e.g., metallic implants or claustrophobia); (8) aphasia due to a subthalamic stroke; (9) pronounced subcortical arteriosclerosis. No exclusion was made based on aphasia severity or lesion size in the acute phase. Participants enrolled in active speech-language therapy at the time of recruitment were also excluded.
MRI acquisition and lesion processing

Participants underwent MRI scans at three timepoints: (1) ≤3 days post-stroke (acute phase), (2) 10–14 days (subacute phase), and (3) 6–12 months (chronic phase). Longitudinal T1-weighted images were processed using FreeSurfer to create within-subject templates. Diffusion-weighted and T1-weighted images were processed using the TractoFlow pipeline [@Theaud2020], generating diffusion tensor metrics: fractional anisotropy (FA), axial diffusivity (AD), and radial diffusivity (RD).
Lesion segmentation was performed semi-automatically using the Clusterize toolbox on MD maps in the acute and subacute phases, and on RD(AD?) maps for the chronic phase. All lesion segmentations were manually reviewed and corrected by an experienced researcher in tracing lesions in PWA. Binary lesion masks were then created at each timepoint in RAS orientation (1 mm isotropic resolution). These masks and corresponding anatomical images were transformed into MNI152 2 mm space using FSL’s FLIRT (nearest-neighbor interpolation, no smoothing, zero padding). The NeuroTmap pipeline [@Alves2025] was applied to compute neurotransmitter-specific lesion’s metrics, including sum of receptor and transporter’s location density map voxels or white matter projection map voxels intersected by the lesion, and pre- and postsynaptic ratios of the studied neurotransmitters systems. The NeuroT-Map tool and associated scripts are publicly available on GitHub at: https://github.com/Pedro-N-Alves/NeuroT-Map?tab=readme-ov-file. 

## Language Assessment

At each timepoint, participants underwent a language battery test which included:

- Naming: DO-80, [@Deloche1997] Boston naming test [@Kaplan1983]
- Verbal fluency:  Montréal Évaluation de la Communication (MEC) [@Joanette2004]. 
- Word and pseudoword repetition: Montréal-Toulouse-86 (MT-86) [@Nespoulous1992]
- Sentence comprehension: MT-86 [@Nespoulous1992], Token test [@Renzi1978]
- Spontaneous speech: Western Aphasia Battery [@Kertesz2006]
- Dysarthria: Robertson dysarthria profile [@Robertson1987]
- Semantics: Pyramid and Palm Tree Test [@Howard1992]
- Executive Function: Ruff Figural Fluency Test [@Ruff1986]
- Visual Neglect: Bells Test [@Gauthier1989]

These tests have been found to be acceptable, reliable, and valid measures for PWA [@Wallace2017]. All assessments were conducted by a certified speech-language pathologist. Audio-video recordings were used to ensure reliability. Three core language subscores were derived: naming, repetition, and comprehension. Based on the previous work of Osa García et al., each subscore was scaled from 0 to 10 based on task-specific maximums, yielding a total aphasia severity index, named the Composite Score, ranging from 0 to 30.

## Statistical Analysis 

We performed a series of generalized linear models (GLMs) using a Tweedie distribution (variance power =1.4) with a logarithmic link function to accommodate continuous outcomes with skewed distributions and potential zero-values. In the acute full-sample analysis (n = 32), models included interaction terms between sex, lesion volume, and age to explore their potential modulatory effects on the relationship between acute phase neurotransmitter metrics (voxelwise damage to density and projection maps, as well as pre- and post-synaptic ratios) and early language outcomes. We also ran stratified GLMs in men and women separately, without interaction terms but controlling for lesion volume. Finally, an additional GLM was conducted using acute-phase neurotransmitter metrics as early predictors of chronic-phase language outcomes (n=16), adjusting for sex and lesion volume as covariates.

Additionally, two-sample tests (Student’s or Welch’s t-test, or Mann–Whitney U test) were used depending on the normality (Shapiro–Wilk test) and variance homogeneity (Levene’s test). Comparisons were performed between men and women separately for each predictor and outcome variable in the acute phase (nm=19; nf=13), as well as for group-level differences across timepoints (e.g., acute vs. chronic assessments; nm=7; nf=9). The significance threshold was set at α = 0.05 (with the Benjamini-Hochberg false discovery rate correction).

Linear mixed models (LMMs) with time (acute, subacute, chronic) and biological sex as fixed effects were conducted to evaluate longitudinal changes in language scores. Pearson or Spearman correlations were computed between neurotransmitter ratios, between ratios and clinical scores, and between damage metrics and outcomes. All correlation tests were performed separately and jointly for males and females in the acute phase. Also, same correlation tests were made with acute metrics and chronic outcomes. Group-level descriptive statistics (mean, median, SD) were also computed.

# Results

We first examined sex-related differences in neurotransmitter system disruption and language outcomes during the acute phase after stroke, and whether early post-stroke imbalance could predict long-term language recovery.

To visualize disruptions, group-averaged male (n = 23) and female (n = 15) data were overlaid on circular graphs showing lesion effects on receptor/transporter density maps, tract projection maps, and derived synaptic disruption ratios (Fig.1), computed with the NeuroT-Map method by Alves et al.. Note that these sample sizes differ from those used for statistical analyses, as not all participants had clinical data but all had lesion masks.


:::{figure} #fig1cell
:label: fig1
:name: fig-neurotmap-analysis
:placeholder: ./static/tmp.jpg
:height: 400px

Interactive NeuroTmap analysis showing base and overlay comparisons. 
Users can select different sessions (V1, V2, V3) and sex filters (men, women, all) to explore the data interactively.
Left panel: Proportion of each neurotransmitter system affected by the lesion based on receptor/transporter location density maps. Middle panel: Proportion of each neurotransmitter system affected by the lesion based on receptor/transporter tract projection maps. Right panel: Synaptic disruption ratios for men and women, shown in natural logarithmic scale. Abbreviations: 5HT1a serotonin receptor 1a, 5HT1b serotonin receptor 1b, 5HT2a serotonin receptor 2a, 5HT4 serotonin receptor 4, 5HT6 serotonin receptor 6, 5HTT serotonin transporter, α4β2 acetylcholine receptor α4β2, D1 dopamine receptor 1, D2 dopamine receptor 2, DAT dopamine transporter, M1 muscarinic 1 receptor, Nor noradrenaline transporter, VAChT acetylcholine vesicular transporter.

:::


When controlling for equal lesion volume, women exhibited greater damage to neurotransmitter systems than men on both density and projection maps, although overall involvement was low (< 2.5%), except for the serotonin transporter in women (3.5%) on location maps injury  [](#fig1).

Concerning the synaptic disruption graph, the presynaptic ratio compares transporter damage to receptor damage. A positive value means transporters are more affected, while a negative value means receptors are more affected. The postsynaptic ratio does the opposite, comparing receptor to transporter damage. Since one transporter can be linked to several receptors, the postsynaptic damage is averaged across them. Both ratios are calculated from the overlap between lesion maps and the density or projection maps of transporters and receptors (Alves et al., 2025).
Synaptic ratios revealed opposite sex-specific patterns: men showed a predominance of transporters over receptors damages in dopaminergic systems, while women showed the reverse, with the opposite holding true for cholinergic systems. Serotonergic disruption imbalance was also more pronounced in women (Fig.1). In addition, statistical testing revealed a significant sex difference for only the presynaptic 5HT1A ratio (Mann–Whitney U = 106, p = 0.049), with women showing higher values compared to men. This corresponds to an estimated +37.7% (=e0.32) increase in transporter damage relative to receptor damage. 
Global and sex-stratified GLM analyses including age and lesion volume covariates showed no significant associations between synaptic ratios and language outcomes (naming, repetition, comprehension, composite score), although sex-specific trends were apparent ({numref}`tab1-glm`). These nonsignificant results (p >0.05), likely reflect the limited sample size.


:::{table} Table 1 – Percentage change in acute clinical scores per 0.1 unit increase in acute neurotransmitter ratio
:widths: auto
:align: center
:class: tight-table
:name: tab1-glm


| **System**      | **Synaptic Ratio** | **Group** | **Repetition [%]** | **Naming [%]** | **Comprehension [%]** | **Composite [%]** |
|-----------------|-------------------:|:----------|-------------------:|----------------:|-----------------------:|------------------:|
| **Cholinergic** | Pre-α4B2 | Global | 16.81 | 3.39 | 1.63 | 8.06 |
|  |  | Men | 31.18 | (14.78) | (6.47) | 4.55 |
|  |  | Women | 2.08 | 1.19 | 1.22 | 2.03 |
|  | Pre-M1 | Global | 4.30 | 1.74 | 1.97 | 3.09 |
|  |  | Men | 0.48 | (13.12) | (5.52) | (3.29) |
|  |  | Women | 3.99 | 5.34 | 5.27 | 4.69 |
|  | Post-VAchT | Global | (8.22) | (2.92) | (2.80) | (5.35) |
|  |  | Men | (3.48) | 28.31 | 11.6 | 5.54 |
|  |  | Women | (4.60) | (5.65) | (5.79) | (5.32) |
| **Dopaminergic** | Pre-D1 | Global | 4.40 | 1.80 | (1.17) | 2.03 |
|  |  | Men | 8.05 | 2.62 | (1.31) | 3.76 |
|  |  | Women | 0.01 | 2.36 | (0.40) | 0.25 |
|  | Pre-D2 | Global | 0.80 | (4.96) | (4.29) | (2.34) |
|  |  | Men | 16.63 | 0.44 | (4.51) | 5.30 |
|  |  | Women | (5.04) | (6.23) | (3.89) | (4.69) |
|  | Post-DAT | Global | (2.65) | 2.52 | 3.64 | 0.54 |
|  |  | Men | (10.67) | (2.05) | 2.82 | (4.55) |
|  |  | Women | 4.85 | 4.76 | 3.94 | 4.36 |
| **Serotonergic** | Pre-5HT1a | Global | 0.36 | 1.48 | 2.57 | 1.55 |
|  |  | Men | (3.99) | (1.84) | 0.65 | (1.33) |
|  |  | Women | 3.74 | 4.47 | 5.17 | 4.28 |
|  | Pre-5HT1b | Global | (0.12) | 1.21 | 1.11 | 0.74 |
|  |  | Men | (2.79) | (0.74) | (0.64) | (1.34) |
|  |  | Women | 1.94 | 2.87 | 3.71 | 2.81 |
|  | Pre-5HT2a | Global | (0.42) | 1.26 | 1.74 | 0.88 |
|  |  | Men | (4.85) | (1.57) | (0.08) | (1.90) |
|  |  | Women | 2.43 | 3.28 | 3.75 | 3.08 |
|  | Pre-5HT4 | Global | (3.06) | (2.10) | 2.02 | (0.67) |
|  |  | Men | (6.46) | (4.66) | 1.72 | (2.15) |
|  |  | Women | 3.66 | 2.94 | 3.36 | 3.38 |
|  | Pre-5HT6 | Global | (1.20) | 1.88 | 2.31 | 0.93 |
|  |  | Men | (5.59) | (0.36) | 0.56 | (1.66) |
|  |  | Women | 2.95 | 4.00 | 5.13 | 3.95 |
|  | Post-5HTT | Global | 0.77 | (1.27) | (2.08) | (0.92) |
|  |  | Men | 5.31 | 1.55 | (0.28) | 1.83 |
|  |  | Women | (3.40) | (4.12) | (4.87) | (4.04) |

:::


{numref}`tab1-glm` summarizes the estimated effects of a 0.1 increase in pre- or post-synaptic damage imbalance on language performance (naming, repetition, comprehension, and composite score), stratified by sex and neurotransmitter system. In the cholinergic system, pre-α4β2 imbalance was estimated to enhance repetition, particularly in men, but reduce naming and comprehension scores in men, whereas pre-M1 showed negative effects in men and modest benefits in women. Post-VAChT effects were overall estimated as unfavorable, yet sex-specific: predicted improvements in naming and comprehension for men and declines across tasks for women. In the dopaminergic system, pre-D2 was estimated to support repetition in men but impair comprehension, with women showing consistent negative associations; post-DAT exhibited the reverse pattern for women and men exhibited an unfavorable pattern for all scores except comprehension. In the serotonergic system, presynaptic imbalances were generally predicted to benefit women and be neutral or negative in men, while post-5HTT showed the opposite trend.

We then examined correlations between pre- and post-synaptic ratios in the acute phase (n = 38). Several strong positive associations emerged across neurotransmitter systems (e.g., pre-M1 with pre-5HT1b/2a, r > 0.8, p < 0.05). Post-hoc power was high (mean = 0.904). Stratified analyses revealed sex-related differences: women exhibited more and stronger correlations, including strong positive associations between post-DAT and serotonergic presynaptic ratios, and strong negative associations between pre-D2 and both pre-M1 and serotonergic presynaptic ratios. These patterns were not observed in men. The mean post-hoc statistical power for all significant correlations remained high in both subgroups (0.948 in men, 0.927 in women) [](#fig2).


:::{figure} #fig2cell
:label: fig2
:name: fig-correlation-analysis
:placeholder: ./static/tmp.jpg

Interactive correlation heatmaps showing the relationship between pre- and post-synaptic ratios across location and projection maps in the acute phase separately for All participants, Men, and Women. Pearson’s r was used for normally distributed pairs (Shapiro-Wilk test, p > 0.05), Spearman’s rₛ otherwise. Colors indicate correlation (–1 = blue, +1 = red); only FDR-significant correlations (p < 0.05) are shown in bright colors, non-significant in grey. Panels: all participants (left, n=38), men (center, n=23), women (right, n=15). 
Users can select different sessions (V1, V2, V3), systems to analysed (Synaptic ratio, Loc, Tract, Clinical outcomes) and group filters (Aphasic, Non-Aphasic) to explore the data interactively.
:::

We then applied linear mixed-effects modeling for each bounded clinical language outcome (0–10 for naming, repetition, and comprehension; 0–30 for the composite), with fixed effects for time (acute, subacute and chronic phases), sex (reference: women in the acute phase), and their interaction, while adjusting for lesion volume. A random intercept accounted for within-subject variability, and residual diagnostics (QQ plots, Shapiro-Wilk tests) supported the model assumptions ({numref}`tab2-mixed-model`).

::::{table} Table 2 – Mixed Linear Model Regression
:widths: auto
:align: center
:class: tight-table
:name: tab2-mixed-model

| Outcome        | Effect               | Coeff  | SE     | Z      | P-value | [CI 95%]             |
|----------------|----------------------|--------|--------|--------|----------|----------------------|
| **Repetition** | Intercept            | 6.943  | 1.007  | 6.989  | 0.000    | [4.970 ; 8.916]     |
|                | Time[T.V2]           | 0.675  | 0.860  | 0.785  | 0.432    | [-1.010 ; 2.361]    |
|                | Time[T.V3]           | 2.177  | 0.942  | 2.311  | 0.021    | [0.331 ; 4.023]     |
|                | Sexe[T.M]            | -1.029 | 1.090  | -0.944 | 0.345    | [-3.166 ; 1.107]    |
|                | Time[T.V2]:Sexe[T.M] | 0.571  | 1.129  | 0.505  | 0.613    | [-1.643 ; 2.784]    |
|                | Time[T.V3]:Sexe[T.M] | 1.198  | 1.357  | 0.883  | 0.377    | [-1.461 ; 3.858]    |
|                | Group Var            | 4.990  | 1.461  | —      | —        | —                    |
| **Naming**     | Intercept            | 5.966  | 0.902  | 6.613  | 0.000    | [4.198 ; 7.735]     |
|                | Time[T.V2]           | 0.453  | 1.037  | 0.437  | 0.662    | [-1.579 ; 2.485]    |
|                | Time[T.V3]           | 0.489  | 1.110  | 0.440  | 0.660    | [-1.686 ; 2.663]    |
|                | Sexe[T.M]            | -0.974 | 1.005  | -0.969 | 0.332    | [-2.943 ; 0.995]    |
|                | Time[T.V2]:Sexe[T.M] | 1.080  | 1.361  | 0.794  | 0.427    | [-1.587 ; 3.748]    |
|                | Time[T.V3]:Sexe[T.M] | 4.651  | 1.587  | 2.930  | 0.003    | [1.539 ; 7.762]     |
|                | Group Var            | 1.522  | 0.659  | —      | —        | —                    |
| **Comprehension** | Intercept         | 6.102  | 0.731  | 8.342  | 0.000    | [4.668 ; 7.535]     |
|                | Time[T.V2]           | 1.198  | 0.697  | 1.720  | 0.086    | [-0.168 ; 2.564]    |
|                | Time[T.V3]           | 2.869  | 0.756  | 3.795  | 0.000    | [1.387 ; 4.351]     |
|                | Sexe[T.M]            | 1.003  | 0.797  | 1.258  | 0.208    | [-0.559 ; 2.565]    |
|                | Time[T.V2]:Sexe[T.M] | -0.355 | 0.913  | -0.388 | 0.698    | [-2.145 ; 1.435]    |
|                | Time[T.V3]:Sexe[T.M] | 0.702  | 1.088  | 0.646  | 0.519    | [-1.430 ; 2.835]    |
|                | Group Var            | 2.117  | 0.757  | —      | —        | —                    |
| **Composite**  | Intercept            | 19.103 | 2.196  | 8.698  | 0.000    | [14.799 ; 23.408]   |
|                | Time[T.V2]           | 2.353  | 2.213  | 1.063  | 0.288    | [-1.985 ; 6.691]    |
|                | Time[T.V3]           | 5.563  | 2.393  | 2.324  | 0.020    | [0.872 ; 10.253]    |
|                | Sexe[T.M]            | -0.975 | 2.383  | -0.410 | 0.682    | [-5.643 ; 3.692]    |
|                | Time[T.V2]:Sexe[T.M] | 1.225  | 2.903  | 0.422  | 0.673    | [-4.465 ; 6.914]    |
|                | Time[T.V3]:Sexe[T.M] | 6.664  | 3.441  | 1.937  | 0.053    | [-0.080 ; 13.408]   |
|                | Group Var            | 15.545 | 2.218  | —      | —        | —                    |

::::

{numref}`tab2-mixed-model` showed naturally that for each clinical score, lesion volume was negatively associated with most scores (p < 0.001; p < 0.05 for repetition). Women improved in repetition over time (β = 2,177, p = 0.021). Naming showed a significant time × sex interaction at V3 (β = 4.651, p = 0.003), with men improving more than women in chronic phase. Comprehension and composite scores improved in women (p < 0.001 and p < 0.05 at V3, respectively), with a non-significant trend for greater composite score improvement in men (β = 6.664, p = 0.053).

To illustrate longitudinal changes in neurotransmitter system disruption and synaptic ratio imbalance, we overlaid acute (n=38) and chronic (n=17) group-averaged data in circular graphs as we did in [](#fig1), as shown in [](#fig3).


:::{figure} #fig3cell
:label: fig3
:name: fig-cross-correlation-analysis
:placeholder: ./static/tmp.jpg

Interactive NeuroTmap analysis showing base and overlay comparisons for all subjects in acute versus chronic phases. 
Panels and Abbreviations as in Fig.1.
Users can select different sessions (V1, V2, V3) to explore the data interactively.
:::

Neurotransmitter system damage was slightly higher in the chronic phase than in the acute, with each percentage difference being significant according to a Wilcoxon signed-rank test (p < 0.05). Synaptic ratios were more imbalanced in the chronic phase for the cholinergic and serotonergic systems (except pre-5HT4 and pre-5HT1a), whereas dopaminergic ratios tended toward zero in the chronic phase, with pre-D2 reversing sign compared to acute phase. Only, post-VAChT showed a negative significant increase in the chronic phase (Paired t-test, t = 2.18, p = 0.044).
After that, we assessed whether acute synaptic disruption imbalance predicted chronic language outcomes using GLM models, including sex and lesion volume as covariates. {numref}`tab3-chronic-scores` reports the estimated percentage change in chronic scores per 0.1-unit increase in acute ratio. Although the results did not reach statistical significance (p > 0.05), this may be due to the relatively small sample size (n = 15), which limits statistical power.

::::{table} Table 3 – Percentage change in chronic clinical scores per 0.1 unit increase in acute neurotransmitter ratio
:widths: auto
:align: center
:class: tight-table
:name: tab3-chronic-scores

| **System**     | **Synaptic Ratio** | **Repetition [%]** | **Naming [%]** | **Comprehension [%]** | **Composite [%]** |
|----------------|--------------------|--------------------|----------------|-----------------------|-------------------|
| **Cholinergic** | Pre-α4B2  | (5,74) | (10,64) | (4,97) | (6,67) |
|                | Pre-M1     | 5,33   | (8,73)  | 1,64   | 0,49   |
|                | Post-VAchT | (11,32)| 24,21   | (2,55) | (0,001) |
| **Dopaminergic** | Pre-D1    | 4,30   | 7,71   | 1,08   | 4,08   |
|                | Pre-D2     | (3,11) | (2,42) | (1,10) | (2,20) |
|                | Post-DAT   | (1,34) | (5,71) | 0,04   | (2,10) |
| **Serotonergic** | Pre-5HT1a | 1,59   | (5,53) | 0,57   | (0,62) |
|                | Pre-5HT1b | 1,59   | (3,72) | 0,62   | (0,15) |
|                | Pre-5HT2a | 1,63   | (4,17) | 0,71   | (0,19) |
|                | Pre-5HT4  | 1,19   | (5,39) | 0,08   | (1,01) |
|                | Pre-5HT6  | 1,28   | (4,67) | 0,58   | (0,50) |
|                | Post-5HTT | (1,56) | 5,30   | (0,56) | 0,51   |

::::

The cholinergic system, particularly the post-VAChT ratio, was the strongest predictor of chronic language outcomes. While it conferred notable benefits for naming, it was associated with a detrimental effect on repetition, and minor effects on comprehension and the composite score. Moderate associations were also observed for the pre-α4β2 and pre-M1 ratios across several outcomes, with pre-α4β2 generally linked to reduced scores and pre-M1 showing a negative effect mainly on naming. In the dopaminergic system, pre-D1 and pre-D2 showed modest but opposite trends, while serotonergic markers exhibited overall moderate to weak associations, with pre-synaptic ratios favoring repetition but negatively impacting naming score.

Mann–Whitney U tests showed chronic scores exceeded acute scores for the whole sample,  reaching statistical significance for comprehension (meanV1 = 5.49; meanV3 = 8.41; p = 0.019) and the composite score (meanV1= 15.79; meanV3 = 23.24; p = 0.028).

Correlation between pre- and post-synaptic ratios in acute and chronic phases (n=17) were strong for serotonergic ratios, pre-M1, pre-D2, and post-DAT (r > 0.55; p < 0.05; mean post-hoc power = 0.786). Also, early pre-M1 positively correlated with late serotonergic presynaptic ratios, while early pre-D2 showed negative correlations with late serotonergic presynaptic ratios and pre-M1 [](#fig4).

:::{figure} #fig4cell
:label: fig4
:name: fig-cross-correlation-analysis
:placeholder: ./static/tmp.jpg

Interactive correlation heatmaps showing the relationship between pre- and post-synaptic ratios. 
Users can select different sessions (V1, V2, V3) and sex filters (men, women, all) to explore the data interactively.
:::

Correlations between acute pre-synaptic ratios and chronic clinical outcomes were generally low and non-significant, likely due to the small sample size (n = 17; 8 men, 9 women; see Annex for details). To assess generalizability, we compared all these findings with a larger independent cohort from the Aphasia Recovery Cohort Dataset. 


**Figure 5 with two dataset but plotly animation without widget**
*legende : Panels and Abbreviations as in Fig. 1. Men (blue) and women (yellow) group data are overlaid for comparison. Top row: 17 chronic-phase subjects (8 men, 9 women); Bottom row: 181 subjects from the Aphasia Recovery Cohort Dataset (115 men, 66 women; OpenNeuro ds004884, v1.0.0).*

In our small cohort, women generally exhibited greater neurotransmitter damage in both location and tract maps, whereas the larger cohort showed the opposite pattern.  Overall damage percentages were roughly similar across cohorts (Fig. 5). Synaptic ratios also differed: the small cohort displayed positive ratios for pre-serotoninergic, particularly high imbalance in women, and pre-A4B2 systems, while other ratios showed opposite-signed trends for each sex. Women showed a similar tendency as the larger cohort in pre-M1 and post-VAChT, while men aligned in pre-D1 and post-DAT. By contrast, the larger cohort showed more homogeneous tendencies across sexes, with negative values for pre-serotoninergic, pre-cholinergic, and post-dopaminergic ratios, and stronger synaptic imbalance in men.
Statistical testing supported these sex differences in the larger cohort. Significant sex effects were found for several serotonergic markers, including presynaptic ratios 5HT1a (Mann–Whitney U = 2942.5, p = 0.012, z-score = -2.51), 5HT1b (U = 2753.5, p = 0.002, z-score =-3,07), 5HT2a (U = 2785.5, p = 0.003, z-score =-2,98), 5HT4 (U = 3078.5, p = 0.035, z-score =-2,11), 5HT6 (U = 3052.5, p = 0.029, z-score =-2,19), and post-synaptic ratio 5HTT (Mann–Whitney U = 4763, p = 0.004, z-score =2,85) as well as for the dopaminergic pre-D2 (U = 3038, p = 0.026, z-score =-2,23) and the cholinergic pre-M1 (Student’s t-test t=-1,99 , p=0,047). Across these systems, men consistently exhibited higher presynaptic disruption values than women.
Behavioral performance mirrored these differences: in the small cohort, men achieved higher mean composite scores (26.79 vs 19.90 out of 30, t = 2,77, p = 0.015). whereas in the larger cohort, women outperformed men on WAB total scores (70.89 vs 58.79 out of 100, U = 2892.5, p = 0.008, z-score = -2,66). 
Correlations between neurotransmitter ratios and language outcomes revealed no significant associations in the small cohort. In contrast, the larger cohort showed significant correlations for all subjects (e.g., pre-D1/WAB = 0.18; post-DAT/WAB = -0.22), and sex-specific correlations emerged in men (pre-5HT1a/WAB = -0.21; pre-5HT6/WAB = -0.21) and women (pre-A4B2/WAB = -0.34; pre-D2/WAB = 0.28; post-DAT/WAB = -0.32). Within-system correlations highlighted distinct patterns for post-cholinergic and pre-D2: in the smaller cohort, pre-D2 correlated strongly and negatively with pre-serotoninergic and pre-cholinergic ratios, while in the larger cohort it showed moderate-to-strong positive correlations with pre-serotoninergic ratios and pre-M1. Across cohorts, pre-5HT4 showed the weakest correlations overall, except for its strong association with pre-D2 in the larger cohort. Stratification by sex revealed generally lower correlation values but more significant associations detected in women in the larger cohort (Fig.6.).
Finally, post-hoc statistical power for significant correlations was high across all groups: small cohort – 0.896 overall, 0.889 men, 0.912 women; large cohort – 0.962 overall, 0.972 men, 0.939 women.


**Figure 6 with two dataset but plotly animation without widget**

*legende : Top row: larger cohort, showing correlations for all subjects (Left: 181 subjects), men only (Middle: 115 subjects), and women only (Right: 66 subjects). Bottom row: smaller cohort, showing all subjects (Left: 17 subjects), men only (Middle: 8 subjects), and women only (Right: 9 subjects).*

# Discussion

***whether and how biological sex influences neurotransmitter receptor and transporter dynamics during the acute phase of post-stroke aphasia:***

Our results indicate that biological sex influences neurotransmitter receptor and transporter dynamics during the acute phase of post-stroke aphasia. Statistical testing revealed a significant sex difference for the pre-5HT1A ratio, indicating more damage in the transporter 5HTT than in this receptor, with women showing higher values than men, whereas other sex effects did not reach statistical significance, likely due to limited sample size. Notably, the 5-HT1A receptor is known to be involved in the modulation of depressive symptoms and stress responses [@Tahiri2024], suggesting that sex-specific differences in this receptor could have functional consequences beyond language outcomes. Also, women exhibited greater lesion-related damage across neurotransmitter systems, particularly serotonergic transporter (5HTT) pathways. This relative damage to transporters compared to receptors could thereby create a neurobiological vulnerability for mood disorders. The mechanism is hypothetically twofold: initially, post-stroke damage to 5-HTT impairs serotonin reuptake  and leads to increased synaptic serotonin availability; subsequently, dysregulation of 5-HT1A receptors, possibly including upregulation or altered sensitivity through negative feedback, leads to a functional deficit in serotonergic neurotransmission which is a well-established endophenotype of major depression [@Albert2013]. This specific neuropathological profile may thus contribute to the higher incidence of post-stroke depression documented in women compared to men (reference). In contrast, men tended to show a predominance of transporters over receptors damage in dopaminergic systems and the reverse in cholinergic systems, suggesting distinct sex-specific neurochemical vulnerabilities after stroke.

Stratified correlation analyses revealed stronger interdependencies between neurotransmitter systems damage in women, suggesting a more integrated neurochemical network architecture. This pattern was less evident in men. Thus, a lesion disrupting one system in men may have more localized effects, while in women, stronger cross-system coupling could allow the disruption to cascade, amplifying the impact on acute language performance. This sex difference aligns with established brain connectivity concepts where women typically show stronger inter-hemispheric connectivity, facilitating integration, while men show stronger intra-hemispheric connectivity, supporting modular processing [@Ingahalikar2013]. 

Beyond simple lesion magnitude, the organization of neurotransmitter systems also differs by sex. Interestingly, females showed greater lateralization of dopaminergic receptors, for example with the right striatum displaying higher D1 receptor density than the left [@Andersen2000]. Also, an asymmetry was found for D1R location density and white matter projection maps in general [@Alves2025]. In our cohort, the pre-D1 ratio was close to equilibrium in women during the acute phase (0.01) and remained low in the chronic phase (-0.02), whereas men had slightly higher pre-D1 ratios in both phases (0.05 in acute; 0.09 in chronic). This suggests that damage to DAT and D1 receptors was not significantly different for both sexes, potentially resulting in a limited impact on dopaminergic neurotransmission, particularly given that the lesions were located in the left hemisphere. 

GLM analyses also suggested sex-specific patterns in the acute post-stroke phase, although these effects did not reach statistical significance. In women, it was associated with little or no effect on language scores, suggesting that D1 receptors may not strongly influence acute language performance in women. In men, pre-D1 showed a slight association with improved repetition performance, indicating a potential sex difference in dopaminergic modulation. Notably, the GLM indicated a trend for a positive association between pre-α4β2 and repetition scores in men, accompanied by a moderate to high negative correlation with naming and comprehension scores this pattern was not observed in women. This may reflect an acute facilitatory role of α4β2 receptors for the phonological and articulatory processes underlying repetition, but potentially at the expense of semantic and lexical processes or perhaps reflecting a maladaptive compensatory mechanism for these other tasks. Indeed, the α4β2 nicotinic receptor is well known to support verbal memory, attention and learning [@Sabri2018]. This suggests that, during the acute phase, predominant damage to cholinergic transporters relative to nicotinic receptors may exert a larger influence on language performance in men. Moreover, sex-specific trends were also observed in serotonergic disruption ratios: presynaptic imbalances were generally predicted to benefit women’s language outcomes and be neutral or negative in men, whereas post-5HTT imbalances showed the opposite trend. These sex-specific patterns in serotonergic vulnerability are consistent with baseline differences in serotonin biology. Females have higher whole blood 5-HT levels [@Gur1990], higher 5-HT transporter availability in the diencephalon and brainstem [@Rodriguez1988], and higher 5-HT1A receptor numbers than males [@Baxter1987;@Staley2006]. In contrast, males synthesize serotonin significantly faster than females, reaching 52% higher mean synthesis rates [@Andreason1994]. This fundamental difference in serotonin turnover may underlie our finding that a 0.1-unit increase in transporter over receptor damage ratio could lead to greater impairments in language outcomes for men: faster serotonin synthesis may require proportionally more transporter function to maintain optimal neurotransmission, whereas women, who generally have higher baseline transporter availability, may be less affected by a comparable degree of transporter damage. This disparity underscores that the functional impact of a neurochemical lesion may be modulated by biological sex. Taken together, these findings suggest the need for nuanced, task-dependent, and potentially personalized approaches to modulating cholinergic, dopaminergic, and serotonergic systems, and warrant further investigation in sex-stratified controlled trials considering individual neurochemical profiles.

These acute-phase sex-specific neurochemical vulnerabilities set the stage for divergent long-term recovery trajectories. We next investigated whether these early neurochemical imbalances could predict chronic language outcomes.

***whether these early neurochemical patterns can help predict long-term language recovery:***

Our longitudinal models confirmed significant behavioral recovery in language outcomes over time, particularly for repetition, comprehension, and composite scores. However, a sex-specific trajectory was uncovered for naming, where men improved significantly more than women by the chronic phase. Paradoxically, this clinical improvement co-occurred with a worsening damage across system and a trend toward greater presynaptic ratio imbalances in cholinergic and serotonergic systems (except pre-5HT4 and pre-5HT1a), indicating a shift toward greater transporter damage relative to receptors. This apparent paradox suggests that behavioral recovery can progress despite persistent neurochemical dysregulation, likely through compensatory mechanisms such as dopaminergic re-equilibration or recruitment of alternative networks. However, the fact that serotonergic and cholinergic systems remain imbalanced over time may indicate a biological limit to full recovery, potentially predisposing patients to residual language deficits or affective disturbances. A key limitation of this study is the absence of reference values for transporter-to-receptor ratios in healthy individuals, stratified by sex and age. Without such normative baselines, it remains uncertain whether the observed imbalances reflect maladaptive dysfunction or, conversely, adaptive reorganization processes that support functional neurotransmission.
Although no associations reached statistical significance in our GLM model, likely due to the limited sample size, several consistent trends emerged across systems. Among them, the cholinergic system stood out: the post-VAChT ratio was the strongest predictor of chronic outcomes, showing a paradoxical pattern of facilitating naming performance while hindering repetition. Similarly, pre-α4β2 and pre-M1 ratios were associated with detrimental effects on multiple outcomes, highlighting a possible key critical role of early cholinergic integrity for language recovery. Dopaminergic predictors revealed modest but directionally distinct effects: pre-D1 tended to support recovery across domains, whereas pre-D2 predicted poorer outcomes, in line with their differential contributions to reward-based learning and executive modulation. The opposite polarity observed between pre-D1 and pre-D2 disruption ratio aligns with established models of dopamine-dependent synaptic plasticity, whereby D1 receptor activation promotes long-term potentiation (LTP) while D2 receptor stimulation facilitates long-term depression (LTD) [@Calabresi2007]. In contrast, serotonergic markers showed weak or inconsistent associations, with presynaptic ratios modestly favoring repetition but negatively impacting naming. This suggests that early serotonergic disruption may be less predictive of chronic outcomes, despite its persistent dysregulation over time.
The correlational analyses provided additional insight. Strong positive correlation of serotonergic, pre-M1, pre-D2, and post-DAT ratios across acute and chronic phases suggests that initial disruptions in these systems persist and could shape longer-term trajectories. Interestingly, early pre-M1 correlated positively with late serotonergic ratios, while pre-D2 correlated negatively, pointing toward potential cross-system interactions that may influence compensatory dynamics.
Taken together, these findings indicate that while our predictive models were underpowered, certain neurotransmitter systems, particularly cholinergic and dopaminergic damage, may provide early biomarkers of long-term recovery trajectories. The significant improvement in comprehension and composite scores across the cohort further underscores that recovery is possible even in the context of persistent dysregulation, but its trajectory may depend on the balance between adaptive and maladaptive plasticity in these systems. A larger sample will be necessary to validate these trends and establish whether specific acute synaptic imbalances can serve as reliable predictors of language outcomes post-stroke.

***Cohort comparison: ***

Building upon our longitudinal findings, a critical question for clinical translation is the generalizability of these sex-specific neurochemical patterns. To assess this, we compared our results with a large, independent cohort from the Aphasia Recovery Cohort Dataset.
This external validation revealed a fundamental insight: the influence of biological sex on neurochemical disruption is not absolute but is powerfully modulated by cohort composition, and likely by age. In fact, the larger cohort consisted of younger participants (men 57.3 ± 9.7, women 59.4 ± 12.5; age range 27–80 years), whereas the smaller cohort was older (men 68.0 ± 12.7, women 72.9 ± 14.1; age range 47–95 years). This difference in age between the two cohorts was statistically significant (Student’s t = -4.41, p < 0.001) and likely contributes to the divergent outcomes, measured by WAB or composite score, observed between the groups. In the smaller, older chronic cohort, women exhibited greater overall damage, aligning with the acute-phase vulnerability observed in our primary analysis, and men tended to show higher language scores. Conversely in the larger, younger cohort, the pattern was reversed: men showed consistently higher presynaptic disruption across multiple serotonergic, dopaminergic, and cholinergic markers and women showed better WAB score. 
This interaction between sex and age is consistent with both clinical and experimental literature. Extensive research indicates that post-stroke recovery is often more challenging for women, largely due to their older mean age at stroke onset **(reference)**. However, this sex-based disadvantage is not uniform across all age groups. Experimental studies in rodents have shown that young, ovary-intact females experience smaller infarcts and less severe stroke outcomes compared with age-matched males or older females, while aged females have the poorest outcomes, including larger strokes, increased edema, and enhanced blood–brain barrier breakdown [@Manwani2011]. This pattern mirrors observations in human populations, where younger women may exhibit superior recovery post-stroke compared to men, but this advantage diminishes or reverses with advanced age. Our results align with this established pattern. Thus, the age difference likely explains the sex-specific recovery patterns in our cohorts, which may also influence the observed neurotransmitter ratio differences. In younger women, a receptor-over-transporter damage imbalance may be associated with better language recovery, consistent with the key role of serotonergic neurotransmission in females and their higher scores in this cohort, although this interpretation requires further confirmation.
Consequently, the stark contrast between the two cohorts does not invalidate our findings but rather underscores that sex differences in post-stroke neurochemistry are not static; they are dynamic and likely shaped by the aging process. In addition to age, lesion topography appears to exert a crucial influence. The larger cohort presented a substantial imbalance with injuries biased toward the middle cerebral artery territory. Moreover, the aphasia subtype distribution differed markedly between cohorts. In the smaller cohort, cases were distributed across 9 anomic aphasia, 3 Wernicke, 2 transcortical motor, 1 transcortical sensory, 1 mixed transcortical, and 1 non-aphasic subject in the chronic phase. By contrast, in the larger cohort, the majority of cases were classified as Broca’s (n = 70) or anomic (n = 51), with additional representation of conduction (n = 20), global (n = 10) and Wernicke (n = 6). These disparities in lesion location and aphasia type are likely to contribute substantially to the divergent neurochemical profiles and recovery trajectories observed across cohorts.
Beyond simple comparisons of damage magnitude and synaptic ratios, our correlation analyses revealed a critical influence of cohort characteristics. While our smaller cohort showed no significant correlations between synaptic ratios and language scores, the larger cohort demonstrated several significant associations, both globally and sex stratified. Globally, a relative excess of DAT damage over D2 receptors was associated with better recovery. In men, greater 5HTT damage relative to 5-HT4 and 5-HT6 receptors predicted poorer outcomes, whereas in women, a relative excess of cholinergic and dopaminergic transporter damage over α4β2 and D2 receptors was associated with poorer and better language recovery, respectively. Also, two trends emerged within  neurotransmitter ratio correlations for each cohort. In the smaller cohort, neurotransmitter systems appeared more tightly interconnected and interdependent, as reflected by higher correlation between systems, a tendency more pronounced in men and in global analyses. This pattern could allow a disruption in one system to cascade more rapidly through others, masking isolated, significant correlations with the composite score. In contrast, the larger cohort may exhibit more modular neurochemical function, allowing specific receptor-transporter imbalances to directly influence behavioral outcomes, as reflected by lower inter-systems correlations overall, yet with more significant associations in women compared to the smaller group.
Furthermore, the functional impact of any imbalance is shaped by lesion location, as receptor/transporter density varies regionally and exhibits hemispheric asymmetries [@Alves2025]. Consequently, a lesion in a region with a high density of a specific receptor will have a disproportionately larger effect on that system's function, independently of the overall lesion volume. Thus, both age and neuroanatomical context likely determine how neurotransmitter disruptions influence recovery.
Several limitations of our study must be considered. First, our analysis relied on normative neurotransmitter maps, which do not account for individual variability. The absence of a healthy control group prevents the establishment of reference transporter-to-receptor ratios, making it difficult to definitively classify the observed imbalances as purely maladaptive or potentially compensatory. Next, the use of a single, sex-combined white matter projection map, although necessary, may obscure inherent sex differences in structural connectivity, as well as the sex-specific distribution and predominance of neurotransmitter system densities. A major limitation in comparing cohorts lies in their fundamental dissimilarity. The larger OpenNeuro cohort was not only younger but also disproportionately comprised individuals with Broca’s or anomic aphasia due to lesions in the middle cerebral artery territory, whereas the smaller cohort included heterogeneous aphasia types with a predominance of anomic aphasia. cThese disparities in age distribution, clinical and lesion characteristics are likely major contributors to the divergent neurochemical profiles observed, limiting direct comparability and highlighting the challenge of generalizing findings across different post-stroke populations.
In conclusion, the comparison with an external cohort confirms that sex differences in post-aphasia neurochemistry are robust but context dependent. Age and lesion location could possibly alter the direction and magnitude of these differences. This emphasizes that a simplistic binary view of sex effects is insufficient. Future research and clinical trials must adopt a multi-dimensional perspective that considers the role of sex, age, and neurochemical profile to truly personalize predictions and interventions for stroke recovery. Our study provides initial evidence and a methodological framework for this nuanced approach, which, with further analysis, could pave the way for personalized medication and therapy for each PSA patient.

# References