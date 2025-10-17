---
numbering:
  heading_2: false
  figure:
    template: Fig. %s
---


# Introduction

Stroke remains a major global public health issue, profoundly affecting individuals' quality of life through a wide range of consequences, including aphasia, motor and sensory deficits, behavioral changes, and even death (Brain Injury Canada, 2024). It is among the most devastating non-communicable diseases (NCDs), ranking second in global mortality and third in combined mortality and disability. Globally, by age 25 one in four adults is expected to experience a stroke in their lifetime, and more than half of these events will occur before the age of 70. In 2021, nearly 12 million people experienced a first-ever stroke, of which 65.3% were ischaemic, and 52.6% occurred in men (Feigin et al, 2025). Despite the slightly higher incidence in men, women who survive a stroke often experience more severe long-term disability. This difference is partly attributed to the older average age at which women suffer strokes and to the loss of estrogen's neurovascular protection after menopause. Knowing that estrogen and progesterone enhance vasodilatation effects, whereas testosterone is believed to have opposed vascular effects (Haast et al., 2012).

Ischaemic stroke results from an obstruction of cerebral blood flow, usually due to a thrombus or embolus, while haemorrhagic stroke is caused by bleeding from a ruptured vessel. Ischaemic stroke is the most common form of stroke. In fact, the present study focuses exclusively on ischaemic stroke, particularly those resulting in aphasia since it affects approximately 1/3 of stroke patients (Pedersen et al., 1995). Aphasia is a disorder that impairs the production and comprehension of language, as well as reading and writing, due to brain damage. While stroke recovery has been widely studied, sex-specific mechanisms underlying aphasia recovery remain underexplored, especially in the acute phase (<72 hours post-stroke). 
Recent advances in molecular neuroimaging offer novel tools to explore these mechanisms. Hansen et al. recently published a neurotransmitter atlas of normative receptor and transporter densities maps, which was later used by Alves et al. to develop an MRI white matter atlas of neurotransmitter circuits representing the axonal projections of acetylcholine, dopamine, noradrenaline, and serotonin receptors and transporters. Their method allows to chart how stroke damages neurotransmitter systems, which distinguishes pre and postsynaptic disruption. Their method offers a promising approach to customize stroke treatment based on individual profiles.

Nevertheless, there is still limited understanding of how biological sex modulates early neurotransmitter dynamics following stroke. In particular, the role of key neurotransmitters involved in language and memory, such as the ones used by Alves et al. to develop their tool and also glutamate, and γ-aminobutyric acid (GABA), remains underexplored in the context of sex-specific recovery trajectories after stroke. These neurotransmitters are all relevant to cognitive and linguistic functions. Identifying sex-linked neurochemical differences in these systems could pave the way for more personalized therapeutic strategies

The objective of this study is twofold: (1) to determine whether and how biological sex influences neurotransmitter receptor and transporter dynamics during the acute phase of post-stroke aphasia; and (2) to assess whether these early neurochemical patterns can help predict long-term language recovery. Ultimately, this work aims to contribute to more personalized stroke rehabilitation approaches, including the tailored use of receptor agonists or transporter inhibitors, recognizing that men and women may respond differently to the same pharmacological intervention.


# Materials and methods

## Participants

Forty-eight individuals with aphasia (PWA) were recruited from the Neurology Unit of the Hôpital du Sacré-Cœur de Montréal (HSCM), part of the CIUSSS du Nord-de-l’Île-de-Montréal. Sixteen participants were later excluded due to the following reasons: brain tumors, right or bilateral stroke, left-handedness, MRI intolerance, multiple strokes, or voluntary withdrawal/refusal to continue participation. Ultimately, fifteen participants completed all three timepoints up to the chronic phase.
Inclusion criteria for PWA were: (1) first-ever left-hemispheric ischemic stroke in the middle cerebral artery (MCA) territory; (2) presence of aphasia affecting speech production and/or comprehension in the acute phase; (3) native French speaker; (4) aged 18 to 85; and (5) right-handed. Exclusion criteria included: (1) major psychiatric illness; (2-3) history of traumatic brain injury or intracranial surgery; (4) alcoholism or drug abuse; (5) learning disability; (6) uncorrected hearing or vision problems; (7) MRI contraindications (e.g., metallic implants or claustrophobia); (8) aphasia due to a subthalamic stroke; (9) pronounced subcortical arteriosclerosis. No exclusion was made based on aphasia severity or lesion size in the acute phase. Participants enrolled in active speech-language therapy at the time of recruitment were also excluded.
MRI acquisition and lesion processing

Participants underwent MRI scans at three timepoints: (1) ≤3 days post-stroke (acute phase), (2) 10–14 days (subacute phase), and (3) 6–12 months (chronic phase). Longitudinal T1-weighted images were processed using FreeSurfer to create within-subject templates. Diffusion-weighted and T1-weighted images were processed using the TractoFlow pipeline (Theaud et al., 2020), generating diffusion tensor metrics: fractional anisotropy (FA), axial diffusivity (AD), and radial diffusivity (RD).
Lesion segmentation was performed semi-automatically using the Clusterize toolbox on MD maps in the acute and subacute phases, and on RD(AD?) maps for the chronic phase. All lesion segmentations were manually reviewed and corrected by an experienced researcher in tracing lesions in PWA. Binary lesion masks were then created at each timepoint in RAS orientation (1 mm isotropic resolution). These masks and corresponding anatomical images were transformed into MNI152 2 mm space using FSL’s FLIRT (nearest-neighbor interpolation, no smoothing, zero padding). The NeuroTmap pipeline (Alves et al., 2025) was applied to compute neurotransmitter-specific lesion’s metrics, including sum of receptor and transporter’s location density map voxels or white matter projection map voxels intersected by the lesion, and pre- and postsynaptic ratios of the studied neurotransmitters systems. The NeuroT-Map tool and associated scripts are publicly available on GitHub at: https://github.com/Pedro-N-Alves/NeuroT-Map?tab=readme-ov-file. 

## Language Assessment

At each timepoint, participants underwent a comprehensive language evaluation designed specifically for PWA by Dr. Brambati and collaborators (Drs. Rochon, Leonard and Marcotte). The battery included:

- Naming: DO-80, (Deloche et al., 1997) Boston naming test (Kaplan et al., 1983)
- Verbal fluency:  Montréal Évaluation de la Communication (MEC) (Joanette et al., 2004). 
- Word and pseudoword repetition: Montréal-Toulouse-86 (MT-86) (Nespoulous et al., 1992)
- Sentence comprehension: MT-86 (Nespoulous et al., 1992), Token test (Renzi et al., 1978)
- Spontaneous speech: Western Aphasia Battery (Kertesz, 2006)
- Dysarthria: Robertson dysarthria profile (Robertson, 1987)
- Semantics: Pyramid and Palm Tree Test (Howard et al., 1992)
- Executive Function: Ruff Figural Fluency Test (Ruff, 1986)
- Visual Neglect: Bells Test (Gauthier et al., 1989)

These tests have been found to be acceptable, reliable, and valid measures for PWA (Wallace et al., 2017). All assessments were conducted by a certified speech-language pathologist. Audio-video recordings were used to ensure reliability. Three core language subscores were derived: naming, repetition, and comprehension. Based on the previous work of Osa García et al., each subscore was scaled from 0 to 10 based on task-specific maximums, yielding a total aphasia severity index, named the Composite Score, ranging from 0 to 30.

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
Global and sex-stratified GLM analyses including age and lesion volume covariates showed no significant associations between synaptic ratios and language outcomes (naming, repetition, comprehension, composite score), although sex-specific trends were apparent (Table 1). These nonsignificant results (p >0.05), likely reflect the limited sample size.



**TABLE 1**

Table 1 summarizes the estimated effects of a 0.1 increase in pre- or post-synaptic damage imbalance on language performance (naming, repetition, comprehension, and composite score), stratified by sex and neurotransmitter system. In the cholinergic system, pre-α4β2 imbalance was estimated to enhance repetition, particularly in men, but reduce naming and comprehension scores in men, whereas pre-M1 showed negative effects in men and modest benefits in women. Post-VAChT effects were overall estimated as unfavorable, yet sex-specific: predicted improvements in naming and comprehension for men and declines across tasks for women. In the dopaminergic system, pre-D2 was estimated to support repetition in men but impair comprehension, with women showing consistent negative associations; post-DAT exhibited the reverse pattern for women and men exhibited an unfavorable pattern for all scores except comprehension. In the serotonergic system, presynaptic imbalances were generally predicted to benefit women and be neutral or negative in men, while post-5HTT showed the opposite trend.
We then examined correlations between pre- and post-synaptic ratios in the acute phase (n = 38). Several strong positive associations emerged across neurotransmitter systems (e.g., pre-M1 with pre-5HT1b/2a, r > 0.8, p < 0.05). Post-hoc power was high (mean = 0.904). Stratified analyses revealed sex-related differences: women exhibited more and stronger correlations, including strong positive associations between post-DAT and serotonergic presynaptic ratios, and strong negative associations between pre-D2 and both pre-M1 and serotonergic presynaptic ratios. These patterns were not observed in men. The mean post-hoc statistical power for all significant correlations remained high in both subgroups (0.948 in men, 0.927 in women) [](#fig2).


:::{figure} #fig2cell
:label: fig2
:name: fig-correlation-analysis
:placeholder: ./static/tmp.jpg

Interactive correlation heatmaps showing the relationship between pre- and post-synaptic ratios across location and projection maps in the acute phase separately for All participants, Men, and Women. Pearson’s r was used for normally distributed pairs (Shapiro-Wilk test, p > 0.05), Spearman’s rₛ otherwise. Colors indicate correlation (–1 = blue, +1 = red); only FDR-significant correlations (p < 0.05) are shown in bright colors, non-significant in grey. Panels: all participants (left, n=38), men (center, n=23), women (right, n=15). 
Users can select different sessions (V1, V2, V3), systems to analysed (Synaptic ratio, Loc, Tract, Clinical outcomes) and group filters (Aphasic, Non-Aphasic) to explore the data interactively.
:::

We then applied linear mixed-effects modeling for each bounded clinical language outcome (0–10 for naming, repetition, and comprehension; 0–30 for the composite), with fixed effects for time (acute, subacute and chronic phases), sex (reference: women in the acute phase), and their interaction, while adjusting for lesion volume. A random intercept accounted for within-subject variability, and residual diagnostics (QQ plots, Shapiro-Wilk tests) supported the model assumptions (Table 2).

**Table 2**

Table 2 showed naturally that for each clinical score, lesion volume was negatively associated with most scores (p < 0.001; p < 0.05 for repetition). Women improved in repetition over time (β = 2,177, p = 0.021). Naming showed a significant time × sex interaction at V3 (β = 4.651, p = 0.003), with men improving more than women in chronic phase. Comprehension and composite scores improved in women (p < 0.001 and p < 0.05 at V3, respectively), with a non-significant trend for greater composite score improvement in men (β = 6.664, p = 0.053).

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
After that, we assessed whether acute synaptic disruption imbalance predicted chronic language outcomes using GLM models, including sex and lesion volume as covariates. Table 3 reports the estimated percentage change in chronic scores per 0.1-unit increase in acute ratio. Although the results did not reach statistical significance (p > 0.05), this may be due to the relatively small sample size (n = 15), which limits statistical power.

**TABLE 3**

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